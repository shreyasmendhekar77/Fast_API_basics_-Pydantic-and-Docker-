
# model validator - which can combine multiple fields for the t validation purpose -
# example- we want the add the patient data such that , if age is greater than 60 then the emergency phone number should be provied 

from pydantic import Field,field_validator,BaseModel,EmailStr,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool 
    allergies :List[str] =None
    contact_details : Dict[str,str] =None

    @model_validator(mode='after')
    def valid_emergency_contact(cls,model):
        if model.age >60 and 'emergency' not in model.contact_details:
            raise ValueError('Patient age is more than 60, it must have emergency contact')
        return model



def print_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)


patient_info = {'name': 'John','email':'abc@hdfc.com','age': '62', 'weight': 56,'married': True
               ,'contact_details':{'emergency':'23232323'}  }
data=Patient(**patient_info)
print_data(data)
    


