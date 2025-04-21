from flask import Flask, render_template
import pandas as pd 
import numpy as np 
import pickle 

app = Flask(__name__)

pipe = pickle .load(open('pipe.pkl','rb'))
df = pickle.load(open('df.pkl','rb'))

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

    except:

if __name__ == "__main__": 
    app.run(debug=True)