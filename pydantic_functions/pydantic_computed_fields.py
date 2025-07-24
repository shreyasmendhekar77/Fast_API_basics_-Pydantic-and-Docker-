# computed fields - to compute the value based on the given data in the model

from pydantic import Field,field_validator,BaseModel,EmailStr,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool 
    allergies :List[str] =None
    contact_details : Dict[str,str] =None

    @computed_field
    @property
    def calculate_BMI(self)->float:
        bmi= round(self.weight /(self.height **2),2)
        
        return bmi





def print_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print("BMI -",patient.calculate_BMI)


patient_info = {'name': 'John','email':'abc@hdfc.com','age': '32', 'weight': 56,'height':1.6,'married': True,
                 }
data=Patient(**patient_info)
print_data(data)
    


