# type validation is absent in python code so  
# we have to explicitly write the if else code for type checking at each time 

#Pydantic solves this problem by providing a way to define data models with type annotations.

# Example of type validation using Pydantic

from pydantic import BaseModel, Field,EmailStr,AnyUrl
from typing import List,Optional,Dict,Annotated


class patient(BaseModel):
    # name: str = Field(...,max_length=50, description="Name of the patient, must be a string with max length 50" )
    # same with annotated 
    name: Annotated[str, Field(..., max_length=50, description="Name of the patient, must be a string with max length 50",examples=["John Doe", "Jane Smith"])]
    Email: EmailStr
    linkedin: AnyUrl
    age: int 
    weight: Annotated[float, Field(...,ge=0,le=100,strict=True,description="Weight in kg, must be a positive number and cannot be string")]
    # married: Optional[bool] =False
    married: Annotated[bool, Field(default=False, description="Marital status of patient, default is False")]
    allergies: Annotated[Optional[List[str]], Field(default=None, description="List of allergies, optional field")]
    contacts: Dict[str, str]

patient_info = {'name': 'John','Email':'abc@gmail.com','linkedin':'http://linkedin.com/232' ,'age': 32, 'weight': 56,'married': True,
                 'contacts': {'email':
                'none@gmail.com',}}



def insert_data(type_validation: patient):
    print(type_validation.name)
    print(type_validation.Email)
    print(type_validation.linkedin)
    print(type_validation.age)
    print(type_validation.weight)
    print(type_validation.married)
    print(type_validation.allergies)
    print(type_validation.contacts)
    # Here we can write the code to insert data into the database
    print('insertion done')

insert_data(patient(**patient_info))

# patients_info={'name':'ron','age': 43}

# insert_data(type_validation(**patients_info))