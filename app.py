from flask import Flask, request, jsonify, render_template
import pandas as pd 
import numpy as np 
import pickle 

app = Flask(__name__)

# Load the model and data
with open('pipe_new.pkl', 'rb') as f:
    pipe = pickle.load(f)  # This should be your trained model

with open('df_new.pkl', 'rb') as f:
    df = pickle.load(f) 


@app.route("/")
def home(): 
    return render_template('index.html', companies = df['Company'].unique(),
                                         types = df['TypeName'].unique(), 
                                          cpus = df['Cpu_brand'].unique(),
                                          gpus = df['Gpu_brand'].unique(),
                                            oss = df['os'].unique())

@app.route('/predict', methods = ['POST'])
def predict(): 
    try: 
        company = request.form['company']
        type = request.form['type']
        ram = int(request.form['ram'])
        weight = float(request.form['weight'])
        touchscreen = 1 if request.form['touchscreen'] == 'Yes' else 0
        ips = 1 if request.form['ips'] == 'Yes' else 0 
        screen_size = float(request.form['screen_size'])
        resolution = request.form['resolution']
        cpu = request.form['cpu']
        hdd = int(request.form['hdd'])
        ssd = int(request.form['ssd'])
        gpu = request.form['gpu']
        os = request.form['os']

        x_res = int(resolution.split('x')[0])
        y_res = int(resolution.split('x')[1])

        ppi = ((x_res**2) + (y_res**2))**0.5/screen_size

        query = np.array([company, type, ram, weight, touchscreen, ips, ppi,
                          cpu, hdd, ssd, gpu, os]).reshape(1,12)
        
        predicted_price = int(np.exp(pipe.predict(query)[0]))

        return render_template('index.html', prediction_text=f"The predicted price is ₹{predicted_price}",
                               companies=df['Company'].unique(), types=df['TypeName'].unique(),
                               cpus=df['Cpu_brand'].unique(), gpus=df['Gpu_brand'].unique(),
                               oss=df['os'].unique())

    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == "__main__": 
    app.run(debug=True)