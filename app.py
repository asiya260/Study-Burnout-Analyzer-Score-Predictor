import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

st.title("📚 Study Burnout Analyzer (Polynomial Regression)")

# -------------------------------
# Sample Data (non-linear pattern)
# -------------------------------
study_hours = np.array([1, 2, 3, 4, 5, 6, 7, 8]).reshape(-1, 1)
marks = np.array([30, 45, 60, 75, 85, 80, 70, 55])

# Polynomial Transformation
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(study_hours)

model = LinearRegression()
model.fit(X_poly, marks)

# -------------------------------
# User Input
# -------------------------------
st.subheader("Enter Your Study Details")

hours = st.slider("Study Hours", 1, 10, 4)

# Prediction
input_poly = poly.transform([[hours]])
prediction = model.predict(input_poly)

st.success(f"Predicted Marks: {int(prediction[0])}")

# -------------------------------
# Optimal Point (Peak)
# -------------------------------
x_range = np.linspace(1, 10, 100).reshape(-1, 1)
y_range = model.predict(poly.transform(x_range))

optimal_hours = x_range[np.argmax(y_range)][0]

st.info(f"Optimal Study Hours: {round(optimal_hours,2)} hrs")

if hours > optimal_hours:
    st.warning("⚠️ You might be overstudying. Performance may drop!")

# -------------------------------
# Graph
# -------------------------------
fig, ax = plt.subplots()
ax.scatter(study_hours, marks)
ax.plot(x_range, y_range)
ax.set_xlabel("Study Hours")
ax.set_ylabel("Marks")
ax.set_title("Study Hours vs Marks (Polynomial Curve)")

st.pyplot(fig)