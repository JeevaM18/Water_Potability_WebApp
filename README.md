# Water Potability Prediction Using Machine Learning

**Overview**

This project is a machine learning-based solution to predict the potability of water based on its physicochemical properties. Using a Random Forest Classifier trained on a comprehensive dataset, the system evaluates parameters like pH, hardness, turbidity, and others to determine whether water is potable or not. A user-friendly web interface, built with Flask, allows users to input water quality attributes and receive real-time predictions.
________________________________________
**Features**

•	Predicts whether water is Potable or Not Potable based on key water quality parameters.

•	Handles real-time inputs with a user-friendly Flask-based web interface.

•	Includes data preprocessing with feature scaling for consistent predictions.

•	Robust Random Forest Classifier model for reliable accuracy.
________________________________________
**Dataset**

The dataset used for training and evaluation includes physicochemical attributes of water samples:

•	Attributes: pH, Hardness, Solids, Chloramines, Sulfate, Conductivity, Organic Carbon, Trihalomethanes, Turbidity.

•	Target Variable: Potability (1: Potable, 0: Not Potable).
________________________________________
**Technologies Used**

•	Programming Language: Python

•	Libraries:

o	Machine Learning: scikit-learn

o	Web Framework: Flask

o	Data Processing: pandas, numpy

•	Frontend: HTML, CSS

•	Deployment: Local Flask server
________________________________________
**Installation**
1.	Clone the repository:
bash
Copy code
git clone https://github.com/JeevaM18/Water_Potability_WebApp.git
cd water-potability-prediction
2.	Install the required dependencies:
bash
Copy code
pip install -r requirements.txt
3.	Ensure the random_forest_model.pkl and scaler.pkl files are present in the project directory.
4.	Run the Flask app:
bash
Copy code
python app.py
5.	Open your browser and visit:
arduino
Copy code
http://127.0.0.1:5000
________________________________________
**Usage**
1.	Enter the water quality attributes in the provided form on the web interface.
2.	Click the "Predict Potability" button.
3.	View the result (Potable or Not Potable) on the result page.
________________________________________
**Project Structure**
graphql

Copy code

water_potability_app/

├── app.py                      # Flask application code

├── random_forest_model.pkl     # Trained Random Forest model

├── scaler.pkl                  # StandardScaler used for preprocessing

├── templates/

│   ├── form.html               # Input form for water attributes

│   └── result.html             # Result page for predictions

├── static/

│   └── style.css               # CSS for styling the web app

├── requirements.txt            # Python dependencies
________________________________________
**Screenshots**

Input Form:

![{CA59107E-477C-4CC9-8C49-49163840FB89}](https://github.com/user-attachments/assets/bd5f0077-8e76-4c0a-8400-f3b358772b45)


Prediction Result:

![{DEF88319-B46A-4FCA-9789-E472D55A64F6}](https://github.com/user-attachments/assets/4713921f-bf89-4bb0-91c5-8fc929f210dd)


•	Displays whether the water is potable or not.
________________________________________
**Future Enhancements**

•	Expand the dataset for better generalization.

•	Add more parameters for water quality evaluation.

•	Deploy the application on a cloud platform for wider accessibility.
________________________________________
**Contributors**

•	Jeeva M

•	Kumaraswamy G
________________________________________
Feel free to contribute by submitting issues or pull requests! 😊
