from fastapi import APIRouter, Response

from schema.doctor import doctors, DoctorsCreateEdit
from services.doctor import DoctorService

doctor_router = APIRouter()

@doctor_router.get('/', status_code=200)
def get_doctors():
    data = DoctorService.parse_doctors(doctor_data=doctors)
    return {'message': 'successful', 'data': data}

@doctor_router.get('/{doctor_id}', status_code=200)
def get_doctor_by_id(doctor_id: int):
    data = DoctorService.get_doctor_by_id(doctor_id)
    return {'message': 'successful', 'data': data}

@doctor_router.post('/', status_code=201)
def create_doctor(payload: DoctorsCreateEdit):
    data = DoctorService.create_doctor(payload)
    return {'message': 'Created', 'data': data}

@doctor_router.put('/{doctor_id}', status_code=200)
def edit_doctor(doctor_id: int, payload: DoctorsCreateEdit):
    data = DoctorService.edit_doctor(payload)
    return {'message': 'success', 'data': data}

@doctor_router.delete('/{doctor_id}')
def delete_doctor(doctor_id: int):
    DoctorService.delete_doctor(doctor_id)
    return {'message': 'user deleted successfully.'}