from pydantic import BaseModel

class Patients(BaseModel):
    id: int
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone: str

class PatientsCreateEdit(BaseModel):
    name: str
    age: int
    sex: str
    weight: str
    height: str
    phone: str

patients: dict[int, Patients] = {
    0: Patients(
        id=0, name='patient 0', age=30, sex='M', weight='80', height='180', phone='0800'
    ),
    1: Patients(
        id=1, name='patient 1', age=35, sex='F', weight='60', height='160', phone='0801'
    ),
    2: Patients(
        id=2, name='patient 2', age=20, sex='M', weight='x70', height='170',phone='0802'
    )
}