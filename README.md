# Advertisement-spent-predictor
using the Advertising dataset to predict sales based on advertising budgets across channels like TV, radio, and newspaper.

Awesome, Shubham! Here's a complete, clean, and professional `README.md` file you can include in your GitHub repo for the Advertising Sales Prediction project.

---

### 📄 `README.md`

```markdown
# 📊 Advertising Sales Prediction – Linear Regression Project

## 🧠 Overview

This project demonstrates how to build a simple yet effective machine learning model using **Linear Regression** to predict **product sales** based on advertising budgets across multiple channels: **TV**, **Radio**, and **Newspaper**.

It includes exploratory data analysis, model training, evaluation, and a **Streamlit-based web app** for interactive prediction.

---

## 📁 Project Structure

```

📦 advertising-sales-prediction/
├── Advertising.csv              # Dataset
├── ML\_LR\_session4.ipynb         # Jupyter Notebook for training & EDA
├── model1.pkl                   # Trained Linear Regression model
├── app.py                       # Streamlit app
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation

````

---

## 🗃 Dataset

**Advertising.csv** contains the following columns:

- `TV`: Advertising budget for TV
- `Radio`: Advertising budget for Radio
- `Newspaper`: Advertising budget for Newspaper
- `Sales`: Units sold (target variable)

---

## 🔍 Features

- Data preprocessing and EDA with visualizations
- Training a Multiple Linear Regression model
- R² evaluation of model performance
- Saving and loading the trained model using `joblib`
- Streamlit UI for real-time prediction based on user inputs

---

## 🚀 How to Run the App

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/advertising-sales-prediction.git
cd advertising-sales-prediction
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Run the Streamlit app:**

```bash
streamlit run app.py
```

---

## 📌 User Inputs

In the Streamlit app, the user can input:

* TV advertising budget
* Radio advertising budget
* Newspaper advertising budget

Then click **"Predict"** to get the estimated sales.

---

## 🧰 Tech Stack

* Python
* Pandas, NumPy, Scikit-learn
* Matplotlib, Seaborn
* Streamlit
* Joblib

---

## 📈 Example

> **Input**
> TV: 200
> Radio: 25
> Newspaper: 10
>
> **Output**
> Estimated Sales: `~15.5 units`

---

## 🔮 Future Enhancements

* Use polynomial regression or regularized models
* Include more advertising variables (social, influencer, etc.)
* Deploy Streamlit app using Streamlit Cloud or Render

---

## 🙋‍♂️ Author

**Shubham Sawant**
Product & Data Enthusiast | Python Developer
[LinkedIn]([https://www.linkedin.com/in//](https://www.linkedin.com/in/shubham-sawant-b67412208/)) | [GitHub](https://github.com/Shubham-10000)

---
