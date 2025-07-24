from fastapi import FastAPI,Query,HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field,computed_field
from typing import Annotated ,Literal
import json 

app= FastAPI()

class Patient(BaseModel):
    id : Annotated[str, Field(...,description="Patint ID",examples=['P001','P002'])]
    name:  Annotated[str, Field(...,description='Name of the patient')]
    city: Annotated[str, Field(...,description='City of the patient')]
    age: Annotated[int, Field(...,gt=0,lt=120,description='Age of the patient')]
    gender: Annotated[Literal['male','female','others'],Field(...,description='Gender of the patient')]
    height: Annotated[float, Field(...,description='Height of the patient')]
    weight: Annotated[float, Field(...,description='Weight of the patient')]

    @computed_field
    @property
    def bmi(self) ->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

    @computed_field
    @property
    def verdict(self)->str:

        if self.bmi<18.5:
            return 'Underweight'

        elif self.bmi <25:
            return 'Normal'

        else:
            return 'Overwight'


def load_data():
    with open('patients.json','r') as f:
        data= json.load(f)
    return data
    
def save_data(data):
    with open('patients.json','w') as f:
        json.dump(data,f)


@app.post('/create')
def create_patient(patient:Patient):

    # load the data 
    data=load_data()
    # check the existane of the new patient
    if patient.id in data:
        raise HTTPException(status_code=400,detail='Patient already exists')

    # add the new data
    data[patient.id]=patient.model_dump(exclude=['id'])

    # save to the data
    save_data(data)

    return JSONResponse(status_code=201, content={'Msg':'new data added sucessfully'})


