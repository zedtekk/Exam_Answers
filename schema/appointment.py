from datetime import datetime
from pydantic import BaseModel

from schema.doctor import Doctors, doctors
from schema.patient import Patients, patients

class Appointments(BaseModel):
    id: int
    patient: Patients
    doctor: Doctors
    date: datetime

class AppointmentsCreate(BaseModel):
    patient: int
    doctor: int
    date: datetime

appointments: list[Appointments] = [
    Appointments(
        id=0, patient=patients[0], doctor=doctors[0], date= datetime(2024, 4, 22)
    )
]