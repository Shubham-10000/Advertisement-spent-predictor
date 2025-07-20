# Advertisement-spent-predictor
using the Advertising dataset to predict sales based on advertising budgets across channels like TV, radio, and newspaper.

Great! Based on your files, it looks like you’ve worked on a small but complete **Linear Regression project** using the **Advertising dataset** to predict **sales based on advertising budgets** across channels like TV, radio, and newspaper.

Here’s a clear and concise **GitHub README-style summary** you can use for your repository:

---

## 📊 Advertising Sales Prediction – Linear Regression Project

### 🧠 Project Overview

This project demonstrates a simple yet effective application of **Linear Regression** to predict **product sales** based on advertising spend across three channels: **TV**, **Radio**, and **Newspaper**. The goal is to understand which mediums contribute most to sales and build a predictive model that can forecast future sales based on advertising budgets.

---

### 📁 Files Included

* `Advertising.csv` – The dataset used for training and evaluation.
* `ML_LR_session4.ipynb` – Jupyter Notebook used for data analysis, visualization, model training, and evaluation.
* `model1.pkl` – Saved Linear Regression model using `joblib`.
* `app.py` – A simple **Streamlit web app** that takes user inputs for ad budgets and predicts expected sales.

---

### 🔍 Key Features

* Data preprocessing and exploratory data analysis (EDA)
* Simple and Multiple Linear Regression models
* Model evaluation using R² score and visualizations
* Interactive Streamlit UI to test predictions live
* Model serialization with `joblib` for production deployment

---

### 🚀 How to Run the App

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/yourusername/advertising-sales-prediction.git
   cd advertising-sales-prediction
   ```

2. **Install Requirements:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Streamlit App:**

   ```bash
   streamlit run app.py
   ```

---

### 📌 Inputs for Prediction

* TV advertising budget
* Radio advertising budget
* Newspaper advertising budget

The model outputs the predicted sales in units based on the input values.

---

### 🛠 Tools & Technologies

* Python
* Pandas, Matplotlib, Seaborn, Scikit-learn
* Jupyter Notebook
* Streamlit
* Joblib (for model saving/loading)

---

### 📈 Sample Prediction Flow

> TV: ₹200 | Radio: ₹25 | Newspaper: ₹10
> **Predicted Sales:** \~15.5 units

---

### ✅ Future Improvements

* Include more features like seasonality, region-wise spending
* Try polynomial regression or ridge/lasso
* Deploy app on Streamlit Cloud or Render

---
    

