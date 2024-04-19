from fastapi import APIRouter

from schema.appointment import AppointmentsCreate, appointments
from services.appointment import AppointmentService

appointment_router = APIRouter()

@appointment_router.post('', status_code=201)
def create_appointment(payload: AppointmentsCreate):
    data = AppointmentService.create_appointment(payload)
    return {'message': 'success', 'data': data}

@appointment_router.get('', status_code=200)
def get_appointments():
    return {'message': 'success', 'data': appointments}

@appointment_router.get('/{appointment_id}')
def get_appointment_by_id(appointment_id: int):
    data = AppointmentService.get_appointment_by_id(appointment_id)
    return {'message': 'success',  'data': data}

@appointment_router.put('/{appointment_id}')
def edit_appointment(appointment_id: int, payload: AppointmentsCreate):
    data = AppointmentService.edit_appointment(appointment_id, payload)
    return {'message': 'success', 'data': data}

@appointment_router.delete('/{appointment_id}', status_code=200)
def delete_appointment(appointment_id: int):
    AppointmentService.delete_appointment(appointment_id)
    return {'Appointment deleted successfully.'}