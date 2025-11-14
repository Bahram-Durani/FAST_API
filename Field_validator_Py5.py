from altair import value
from pydantic import BaseModel, EmailStr, AnyUrl, Field, field_validator
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    # keep your nice metadata
    name: Annotated[str, Field(
        max_length=50,  
        title='Name of the patient',
        description='Provide name of the patient in less than 50 chars',
        examples=['Nitish', 'Amit']
    )]
    email: EmailStr
    linkedin_url: AnyUrl
    age: int = Field(gt=0, lt=120)
    weight: Annotated[float, Field(gt=0, strict=True)]
    married: Annotated[bool, Field(default=None,
                             description='Is the patient married or not')]
    allergies: Annotated[Optional[List[str]], Field(default=None, max_length=5)]
    contact_details: Dict[str, str]

    @field_validator('email')
    @classmethod
    def email_validator(cls, value):
        valid_domains = ['hdfc.com', 'icici.com']  # abc@hdfc.com
        domain_name = value.split('@')[-1]     # split the email by @ and get the domain part

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        
        return value 

    @field_validator('name')
    @classmethod
    def transform_name(cls, value):
        return value.upper()
    
    @field_validator('age', mode='after')
    @classmethod
    def validate_age(cls, value):
        if 0 < value < 100:     
            return value
        else:
            raise ValueError('Age should be in between 0 and 100')

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)  # fixed attribute name
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print('inserted')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)  # fixed attribute name
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print('updated')

patient_data = {
    'name': 'bahram',
    'age': '24',
    'email': 'xy@hdfc.com',
    'linkedin_url': 'https://www.linkedin.com/in/bahram',  # key fixed
    'weight': 98,   # will be coerced to float
    'married': False,
    'contact_details': {'Email': 'bah13@hdf.com', 'phone': '878734'}
    # 'allergies': ['penicillin']  # optional; add if you like (<= 5 items)
}

patient1 = Patient(**patient_data)

# insert_patient_data(patient1)
update_patient_data(patient1)

