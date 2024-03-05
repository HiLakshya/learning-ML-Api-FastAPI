from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction  :float
    Age : int

#loading the saved model
diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

#creating an api

@app.post('/diabetes_prediction')
def diabetes_pred(input_paramters : model_input):
    input_data = input_paramters.json()
    input_dictionary = json.loads(input_data)

    Pregnancies = input_dictionary['Pregnancies']
    Glucose = input_dictionary['Glucose']
    BloodPressure = input_dictionary['BloodPressure']
    SkinThickness = input_dictionary['SkinThickness']
    Insulin = input_dictionary['Insulin']
    BMI = input_dictionary['BMI']
    DiabetesPedigreeFunction = input_dictionary['DiabetesPedigreeFunction']
    Age = input_dictionary['Age']   

    input_list= [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        return "The patient does not have diabetes"
    else:
        return "The patient has diabetes"


@app.get('/status')
def status():
    return {'status': 'The server is up and running'}

#uvicorn ml_api:app --reload