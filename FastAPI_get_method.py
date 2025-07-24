from fastapi import FastAPI,Query
from fastapi.exceptions import HTTPException
from fastapi import Path
import json 

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data


@app.get("/")
def hello():
    return {"message": "Hello, World!"}


@app.get('/about')
def about():
    return {"message": "This is a simple FastAPI application."}


@app.get('/data')
def get_data():
    try:
        data = load_data()
        return {"data": data}
    except Exception as e:
        return {"error": str(e)}

# Get patient by ID
@app.get('/data/{patient_id}')
def get_patient(patient_id: str= Path(..., description='ID of mentioned patient is the DB',example='P001')):
     data=load_data()
     
     if patient_id in data:
         return {"patient": data[patient_id]}
    
        #  return {"error": "Patient not found"}
    # exception http code for data not found
    # return {"error": "Patient not found"}, 404 
     raise HTTPException(status_code=404, detail="Patient not found")
     
# query parameter example
@app.get('/sort')
def sort_patients(sort_by: str =Query(..., description='Sort patients by height, Weight and BMI')
                   , order: str=Query('asc',description=' sort the patient data by ACS or DESC')):
    valid_fields = ['height', 'weight', 'bmi']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid sort field. Choose from height, weight, or bmi.")
    
    if order not in ['asc', 'desc']:
        raise HTTPException(status_code=400, detail="Invalid order. Choose 'asc' or 'desc'.")
    
    data=load_data()

    sorted_data = sorted(data.values(), key=lambda x: x.get(sort_by,0), reverse=(order == 'desc'))

    return sorted_data


    