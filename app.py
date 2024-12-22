import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Set page title and layout
st.set_page_config(page_title="Attendance Impact on Exam Performance", layout="wide")

# Title of the dashboard
st.title("Attendance Impact on Exam Performance")

# File upload section
st.sidebar.header("Upload Your Data")
uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the uploaded CSV file
    data = pd.read_csv(uploaded_file)

    # Display the first few rows of the dataset
    st.write("### Dataset Preview")
    st.dataframe(data.head())

    # Ensure the dataset has the necessary columns
    if 'Attendance_Percentage' in data.columns and 'Exam_Score' in data.columns:
        
        # Correlation Analysis
        st.write("### Correlation Analysis")
        correlation = data[['Attendance_Percentage', 'Exam_Score']].corr()
        st.write("Correlation Matrix:")
        st.dataframe(correlation)

        # Display Scatter plot
        st.write("### Scatter Plot of Attendance vs Exam Score")
        fig, ax = plt.subplots()
        ax.scatter(data['Attendance_Percentage'], data['Exam_Score'], alpha=0.5)
        ax.set_xlabel("Attendance Percentage")
        ax.set_ylabel("Exam Score")
        ax.set_title("Scatter Plot: Attendance vs Exam Score")
        st.pyplot(fig)

        # Perform Linear Regression
        X = data['Attendance_Percentage'].values.reshape(-1, 1)
        y = data['Exam_Score'].values

        # Fit the model
        model = LinearRegression()
        model.fit(X, y)

        # Get the model coefficients
        intercept = model.intercept_
        slope = model.coef_[0]

        # Predict and calculate R-squared
        y_pred = model.predict(X)
        r_squared = r2_score(y, y_pred)

        # Display regression results
        st.write(f"### Linear Regression Results")
        st.write(f"Intercept: {intercept:.2f}")
        st.write(f"Slope: {slope:.2f}")
        st.write(f"R-squared: {r_squared:.3f}")

        # Display regression line on scatter plot
        st.write("### Regression Line")
        fig, ax = plt.subplots()
        ax.scatter(data['Attendance_Percentage'], data['Exam_Score'], alpha=0.5, label='Data Points')
        ax.plot(data['Attendance_Percentage'], y_pred, color='red', label='Regression Line')
        ax.set_xlabel("Attendance Percentage")
        ax.set_ylabel("Exam Score")
        ax.set_title("Regression Line: Attendance vs Exam Score")
        ax.legend()
        st.pyplot(fig)

        # Predict Exam Score for a New Data Point
        st.write("### Predict Exam Score for New Data Point")

        # Input field for the new attendance percentage
        attendance_input = st.number_input("Enter Attendance Percentage", min_value=0.0, max_value=100.0, step=0.1)

        if attendance_input is not None:
            # Predict the exam score for the new input
            predicted_score = model.predict([[attendance_input]])[0]
            st.write(f"Predicted Exam Score for {attendance_input}% Attendance: {predicted_score:.2f}")

            # Visualize the prediction
            st.write("### Prediction Visualization")
            fig, ax = plt.subplots()
            ax.scatter(data['Attendance_Percentage'], data['Exam_Score'], alpha=0.5, label='Data Points')
            ax.plot(data['Attendance_Percentage'], y_pred, color='red', label='Regression Line')
            ax.scatter(attendance_input, predicted_score, color='green', s=100, label='New Prediction', zorder=5)
            ax.set_xlabel("Attendance Percentage")
            ax.set_ylabel("Exam Score")
            ax.set_title("Prediction Visualization: New Data Point")
            ax.legend()
            st.pyplot(fig)

        # Conclusion and Insights
        st.write("### Conclusion and Insights")
        st.write("""
        - Based on the linear regression model, there is a positive relationship between **Attendance Percentage** and **Exam Score**. As attendance increases, the exam score tends to increase as well.
        - **R-squared** value indicates that the model explains a portion of the variance in exam scores based on attendance. A higher R-squared value would indicate a stronger relationship between the two variables.
        - **Prediction**: The app allows you to predict a student's exam score based on their attendance percentage. You can input any value for attendance and get an estimated exam score.
        """)
        
    else:
        st.warning("The uploaded CSV file must contain 'Attendance_Percentage' and 'Exam_Score' columns.")
else:
    st.info("Please upload a CSV file containing 'Attendance_Percentage' and 'Exam_Score' columns.")
