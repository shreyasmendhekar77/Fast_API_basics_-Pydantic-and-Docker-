# field validator 

# model validator - which can combine multiple fields for the t validation purpose -
# example- we want the add the patient data such that , if age is greater than 60 then the emergency phone number should be provied 

from pydantic import Field,field_validator,BaseModel,EmailStr
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    married: bool 
    allergies :List[str] =None
    contact_details : Dict[str,str] =None

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):

        valid_domain=['hdfc.com','icici.com']
        domain_name = value.split('@')[-1]

        if domain_name not in valid_domain:
            raise ValueError('Not a valid domain')
    
        return value
#  apply the transforamtion on the data
    @field_validator('name')
    @classmethod
    def name_transforamtion(cls,name):

        return name.upper()
        
# field validator can be applied in 2 modes after and Before 
    @field_validator('age',mode='after') # the mode 'Before' check the data before the type casting 
                                         # by defalut the value of mode is 'After' which means that the 
                                         # value checking will happen after the type conversion                            
    @classmethod
    def age_valid(cls,value):
        if 0<value<100:
            return value
        else:
            raise ValueError("Age should in 0 to 100")



def print_data(patient:Patient):
    print(patient.name)
    print(patient.email)
    print(patient.age)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)


patient_info = {'name': 'John','email':'abc@hdfc.com','age': '32', 'weight': 56,'married': True,
                 }
data=Patient(**patient_info)
print_data(data)
    


