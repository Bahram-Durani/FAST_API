from altair import value
from pydantic import BaseModel, EmailStr, computed_field
from typing import List, Dict, Optional, Annotated

class Patient(BaseModel):
    name: str
    email: EmailStr
    age: int
    weight: float
    height: float
    married: bool
    allergies: List[str]
    contact_details: Dict[str, str] 


    @computed_field       # decorator 
    @property
    def calculate_bmi(self) -> float:    # the o/p should be in float   
        bmi = round(self.weight/(self.height ** 2),2)      # round to 2 decimal places
        return bmi


def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)     
    print(patient.allergies)
    print('BMI', patient.calculate_bmi)
    print(patient.contact_details)
    print('updated')

patient_data = {'name': 'Bahram',   
                'email':'bagram@gmail.com',
                'age': 30, 
                'weight': 75.2,
                'height': 1.75,
                 'married': True, 
                 'allergies' : ['pollen' , 'dust'],
                 'contact_details' : {'phone' : '2353462'}}

patient1 = Patient(**patient_data)

# insert_patient_data(patient1)
update_patient_data(patient1)

    