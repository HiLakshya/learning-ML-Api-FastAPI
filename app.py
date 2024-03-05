from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.serving import run_simple
from pydantic import BaseModel
import pickle

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

class ModelInput(BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

# Loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

# Creating an API
@app.route('/diabetes_prediction', methods=['POST'])
def diabetes_pred():
    try:
        input_parameters = ModelInput(**request.json)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

    Pregnancies = input_parameters.Pregnancies
    Glucose = input_parameters.Glucose
    BloodPressure = input_parameters.BloodPressure
    SkinThickness = input_parameters.SkinThickness
    Insulin = input_parameters.Insulin
    BMI = input_parameters.BMI
    DiabetesPedigreeFunction = input_parameters.DiabetesPedigreeFunction
    Age = input_parameters.Age

    input_list = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        return "The patient does not have diabetes"
    else:
        return "The patient has diabetes"

@app.route('/status', methods=['GET'])
def status():
    return jsonify({'status': 'The server is up and running'})

if __name__ == '__main__':
    run_simple('0.0.0.0', 8000, app, use_reloader=True)
