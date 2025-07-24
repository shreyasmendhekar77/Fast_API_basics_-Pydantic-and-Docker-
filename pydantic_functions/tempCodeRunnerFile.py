# type validation is absent in python code so  
# we have to explicitly write the if else code for type checking at each time 

#Pydantic solves this problem by providing a way to define data models with type annotations.

# Example of type validation using Pydantic

from pydantic import BaseModel, Field
from typing import List,Optional,Dict


class patient(BaseModel):
    name: str 
    age: int 
    weight: float
    married: Optional[bool]
    allergies: List[str]
    constacts: Dict[str, str]

patient_info = {'name': 'John', 'age': '30', 'weight': '70.5', 'married': True,
                'allergies': ['pollen', 'nuts'], 'constacts': {'email':
                'none@gmail.com',}}



def insert_data(type_validation: patient):
    print(type_validation.name)
    print(type_validation.age)
    print(type_validation.weight)
    print(type_validation.married)
    print(type_validation.allergies)
    print(type_validation.constacts)
    # Here we can write the code to insert data into the database
    print('insertion done')

insert_data(patient(**patient_info))

# patients_info={'name':'ron','age': 43}

# insert_data(type_validation(**patients_info))