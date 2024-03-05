# Diabetes Prediction API

This FastAPI application provides an API endpoint for predicting whether a patient has diabetes based on input parameters. The model used for prediction is loaded from a saved file (`diabetes_model.sav`).

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required dependencies from `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure that the saved model file (`diabetes_model.sav`) is in the same directory as the FastAPI script.

2. Run the FastAPI server using the following command:
   ```bash
   uvicorn your_script_name:app --reload
   ```
   Replace `your_script_name` with the actual name of your FastAPI script.

3. Once the server is running, you can access the API at `http://127.0.0.1:8000`.

### Endpoint

- **Prediction Endpoint**: 
  - **URL**: `http://127.0.0.1:8000/diabetes_prediction`
  - **Method**: POST
  - **Input**: Provide input parameters in the request body as a JSON object. Refer to the `model_input` class for parameter details.
  - **Output**: Returns a prediction indicating whether the patient has diabetes.

- **Status Endpoint**: 
  - **URL**: `http://127.0.0.1:8000/status`
  - **Method**: GET
  - **Output**: Returns the status of the server.

## Example

Use a tool like Postman to make POST requests to the `/diabetes_prediction` endpoint with input parameters in the request body.

Example input:
```json
{
   "Pregnancies": 5,
   "Glucose": 120,
   "BloodPressure": 70,
   "SkinThickness": 30,
   "Insulin": 80,
   "BMI": 23.5,
   "DiabetesPedigreeFunction": 0.5,
   "Age": 35
}
```