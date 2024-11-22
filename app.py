from flask import Flask, render_template, request
import pickle
import numpy as np

# Load the trained model and scaler
with open('random_forest_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

app = Flask(__name__)

# Route for the form page
@app.route('/')
def index():
    return render_template('form.html')

# Route for prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input values from form, preserving decimal values
        ph = float(request.form['ph'])
        hardness = float(request.form['hardness'])
        solids = float(request.form['solids'])
        chloramines = float(request.form['chloramines'])
        sulfate = float(request.form['sulfate'])
        conductivity = float(request.form['conductivity'])
        organic_carbon = float(request.form['organic_carbon'])
        trihalomethanes = float(request.form['trihalomethanes'])
        turbidity = float(request.form['turbidity'])

        # Prepare input data for model
        input_data = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity, organic_carbon, trihalomethanes, turbidity]])

        # Apply scaling
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)[0]
        result = "Potable" if prediction == 1 else "Not Potable"
    
    except ValueError:
        result = "Invalid input. Please enter valid numbers."

    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
