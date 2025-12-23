# 📊 Customer Churn Prediction App

A machine learning–based **Customer Churn Prediction Web App** built using **Python, Scikit-learn, and Streamlit**.
The app predicts whether a customer is likely to **churn (Yes/No)** based on demographic and service-related inputs.

##🚀 Live Demo 
https://churn--modelfuture-ml-02-9zhmsn48vlhzm8dlqhmmky.streamlit.app

## 🚀 Features

* Predicts **customer churn (Yes / No)**
* Uses **Logistic Regression** model
* Data preprocessing with **StandardScaler**
* Interactive **Streamlit web interface**
* 🎈 Balloons animation on positive prediction
* Easy to use & beginner friendly

## 🧠 Machine Learning Model

* **Algorithm:** Logistic Regression
* **Features Used:**

  * Age
  * Gender
  * Tenure
  * Monthly Charges
* **Target Variable:** Churn (Yes / No)

## 🗂️ Project Structure


churn-prediction-model/
│
├── app.py                   # Streamlit web app
├── model.pkl                # Trained Logistic Regression model
├── scaler.pkl               # StandardScaler used during training
├── customer_churn_data.csv  # Dataset
├── notebook.ipynb           # Model training notebook
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation

## Screenshot 
<img width="861" height="589" alt="image" src="https://github.com/user-attachments/assets/285ba8e4-a2b5-47b2-b5ff-21a793b2b598" />


## 🖥️ App Interface
* Enter:

  * Age
  * Tenure
  * Monthly Charges
  * Gender
* Click **Predict**
* Output:

  * ✅ YES → Customer likely to churn (🎈 balloons)
  * ❌ NO → Customer not likely to churn



## 📦 Requirements

* Python 3.9+
* streamlit
* scikit-learn
* pandas
* numpy
* joblib



## 📈 Future Improvements

* Add churn probability (%)
* Improve accuracy with advanced models
* Add visualizations & charts
* Deploy app on Streamlit Cloud



## 👩‍💻 Author

**Riya Bhargava**
Beginner ML & Python Developer 🚀



## ⭐ Acknowledgements

* Scikit-learn
* Streamlit
* Open-source community



