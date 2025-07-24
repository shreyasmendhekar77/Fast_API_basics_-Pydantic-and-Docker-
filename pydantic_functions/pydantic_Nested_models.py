# Nested model in pydantic

from pydantic import BaseModel

class Address(BaseModel):

    city: str
    state: str
    pin : str


class Patient(BaseModel):

    name: str
    gender: str
    age: int
    address: Address

address_dict={'city':'pune','state':'Maharashtra','pin':'400022'}

adress1=Address(**address_dict)

Patient_dict= {'name':'Nitish','gender':'male','age':23,'address':adress1}

patient1=Patient(**Patient_dict)

print(patient1)