## 🖥️ Laptop Price Predictor using Machine Learning

This project leverages machine learning techniques to predict laptop prices based on key hardware and brand specifications. It uses a trained regression model and serves predictions through a Flask web interface.

---

### 📌 Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Model](#model)
- [Tech Stack](#tech-stack)
- [How to Run](#how-to-run)
- [Demo](#demo)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)

---

### 📖 Overview

Accurate laptop price prediction is a valuable tool for both customers and retailers. This project uses machine learning algorithms to estimate laptop prices based on brand, processor, screen resolution, RAM, GPU, and other features. The final model is deployed using a Flask web application for easy interaction.

---

### 📂 Dataset

The dataset used in this project contains information about various laptop models and their specifications such as:

- Brand
- Type
- RAM
- Weight
- Touchscreen / IPS Display
- Screen Size and Resolution
- CPU & GPU
- HDD / SSD
- Operating System
- Price

> 📌 *Note: The dataset has been cleaned and preprocessed for training.*

---

### ✅ Features

- Preprocessed and cleaned dataset
- Feature engineering (e.g., calculating PPI from resolution and screen size)
- One-hot encoding for categorical variables
- Log transformation for the price variable
- Model training using regression
- Web interface using Flask for real-time predictions

---

### 🤖 Model

The model pipeline is trained using a regression algorithm. The final model is serialized using `pickle` for deployment.

- **Target Variable**: `Price (log-transformed)`
- **Algorithms Explored**: Linear Regression, Random Forest, etc.
- **Final Model**: Selected based on RMSE and R² metrics

---

### 💠 Tech Stack

- **Language**: Python
- **Libraries**: pandas, numpy, scikit-learn, pickle
- **Web Framework**: Flask
- **Frontend**: HTML (Jinja2 Templates)

---

### 🚀 How to Run

#### 1. Clone the Repository

```bash
git clone https://github.com/your-username/laptop-price-predictor.git
cd laptop-price-predictor
```

#### 2. Install Requirements

```bash
pip install -r requirements.txt
```

#### 3. Start the Flask App

```bash
python app.py
```

Open your browser and go to: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

### 📁 Project Structure

```
.
├── app.py                   # Flask web app
├── pipe.pkl                 # Trained ML model
├── df.pkl                   # Preprocessed DataFrame
├── templates/
│   └── index.html           # Web UI
├── static/                  # (Optional) CSS/JS files
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

---

### 🗈️ Screenshots

![Form UI](https://via.placeholder.com/600x350?text=Form+Input+UI)
*Web form for entering laptop specifications*

---

### 💡 Future Improvements

- Support for batch predictions via CSV upload
- RESTful API for model access via JSON
- Improved UI using Bootstrap or React
- Model versioning and comparison dashboard

---

### 🤝 Contributing

Contributions, issues and feature requests are welcome!  
Feel free to check the [issues page](https://github.com/your-username/laptop-price-predictor/issues).

---

### 📄 License

This project is licensed under the [MIT License](LICENSE).

---

### 📬 Contact

For any queries or suggestions, feel free to connect:

- **GitHub**: [shivshankarsajeev](https://github.com/shivshankarsajeev)

