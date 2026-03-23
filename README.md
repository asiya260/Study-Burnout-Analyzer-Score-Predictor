# 📚 Study Burnout Analyzer & Score Predictor (Polynomial Regression)

🔗 **Live App:** https://study-burnout-analyzer-score-predictor-hxfuzdogn6ruscnr3hnfmh.streamlit.app/
💻 **GitHub Repo:** https://github.com/asiya260/Study-Burnout-Analyzer-Score-Predictor

---

## 📌 Project Overview

This project is a Machine Learning web application that analyzes the relationship between study hours and student performance using **Polynomial Regression**.

Unlike simple linear models, this project captures the real-world scenario where:

* Studying more improves marks initially 📈
* Overstudying leads to burnout and reduced performance 📉

---

## 🧠 Machine Learning Concept

This project uses **Polynomial Regression**, which is an extension of linear regression used to model **non-linear relationships** between variables. ([GeeksforGeeks][1])

### Key Idea:

* Linear Regression → Straight line
* Polynomial Regression → Curved relationship

This is important because real-life data often follows a **curve instead of a straight line**. ([Learning Lab][2])

---

## 📊 Mathematical Model

The model follows a quadratic equation:

y = b₀ + b₁x + b₂x²

Where:

* **x** = Study hours
* **y** = Predicted marks

---

## 🚀 Features

### 📥 Input

* Study Hours (user-controlled slider)

### 📤 Output

* Predicted marks based on input

---

### ⚠️ Burnout Detection

* Identifies **optimal study hours**
* Warns user if they exceed it:

  > “You might be overstudying. Performance may drop!”

---

### 📈 Visualization

* Graph showing:

  * Actual data points
  * Polynomial curve
* Clearly demonstrates **non-linear behavior**

---

## 🛠️ Technologies Used

* Python
* Streamlit
* NumPy
* Scikit-learn
* Matplotlib

---

## ▶️ How to Run Locally

1. Clone the repository:

```
git clone https://github.com/asiya260/Study-Burnout-Analyzer-Score-Predictor.git
```

2. Navigate to the folder:

```
cd Study-Burnout-Analyzer-Score-Predictor
```

3. Install dependencies:

```
pip install -r requirements.txt
```

4. Run the app:

```
streamlit run app.py
```

---

## 📂 Project Structure

```
Study-Burnout-Analyzer-Score-Predictor/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 🎯 Key Learning Outcomes

* Understanding **non-linear relationships in data**
* Implementing **Polynomial Regression using Scikit-learn**
* Visualizing model behavior using graphs
* Building and deploying ML apps using Streamlit

---

## ⚠️ Limitations

* Uses a small sample dataset
* Accuracy can be improved with real-world data
* Higher polynomial degree may cause overfitting

---

## 🚀 Future Improvements

* Add more inputs (sleep, stress, distractions)
* Improve UI/UX design
* Store user data for better predictions
* Add performance comparison (Linear vs Polynomial)

---

## 🙌 Conclusion

This project demonstrates how Machine Learning can model real-life patterns like **study vs performance trade-off**.

It highlights the importance of choosing the right model:

* Linear Regression fails in curved data
* Polynomial Regression provides better accuracy

---

⭐ This project is a simple yet powerful demonstration of applying ML concepts to real-world student behavior.

[1]: https://www.geeksforgeeks.org/machine-learning/python-implementation-of-polynomial-regression/?utm_source=chatgpt.com "Implementation of Polynomial Regression"
[2]: https://learninglabb.com/what-is-polynomial-regression-in-machine-learning/?utm_source=chatgpt.com "What is Polynomial Regression in Machine Learning?"
