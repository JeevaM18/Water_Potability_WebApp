Water Potability Prediction Using Machine Learning

Overview

This project is a machine learning-based solution to predict the potability of water based on its physicochemical properties. Using a Random Forest Classifier trained on a comprehensive dataset, the system evaluates parameters like pH, hardness, turbidity, and others to determine whether water is potable or not. A user-friendly web interface, built with Flask, allows users to input water quality attributes and receive real-time predictions.

Features

1. Predicts whether water is Potable or Not Potable based on key water quality parameters.
2. Handles real-time inputs with a user-friendly Flask-based web interface.
3. Includes data preprocessing with feature scaling for consistent predictions.
4. Robust Random Forest Classifier model for reliable accuracy.

Dataset

The dataset used for training and evaluation includes physicochemical attributes of water samples:

Attributes: pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity.
Target Variable: Potability (1: Potable, 0: Not Potable).
Technologies Used
Programming Language: Python
Libraries:
Machine Learning: scikit-learn
Web Framework: Flask
Data Processing: pandas, numpy
Frontend: HTML, CSS
Deployment: Local Flask server
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/water-potability-prediction.git
cd water-potability-prediction
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Ensure the random_forest_model.pkl and scaler.pkl files are present in the project directory.

Run the Flask app:

bash
Copy code
python app.py
Open your browser and visit:

arduino
Copy code
http://127.0.0.1:5000
Usage
Enter the water quality attributes in the provided form on the web interface.
Click the "Predict Potability" button.
View the result (Potable or Not Potable) on the result page.
Project Structure
graphql
Copy code
water_potability_app/
├── app.py                     # Flask application code
├── random_forest_model.pkl     # Trained Random Forest model
├── scaler.pkl                  # StandardScaler used for preprocessing
├── templates/
│   ├── form.html               # Input form for water attributes
│   └── result.html             # Result page for predictions
├── static/
│   └── style.css               # CSS for styling the web app
├── requirements.txt            # Python dependencies
Screenshots
Input Form:

A form to enter water quality attributes such as pH, Hardness, and Turbidity.
Prediction Result:

Displays whether the water is potable or not.
Future Enhancements
Expand the dataset for better generalization.
Add more parameters for water quality evaluation.
Deploy the application on a cloud platform for wider accessibility.
Contributors
Jeeva M
Kumaraswamy G
