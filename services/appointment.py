from fastapi import HTTPException

from schema.appointment import AppointmentsCreate, Appointments, appointments
from schema.doctor import Doctors, doctors
from schema.patient import Patients, patients
from utils.appointment import AppointmentHelpers

class AppointmentService:

    @staticmethod
    def create_appointment(payload: AppointmentsCreate):
        id = len(appointments)
        patient: Patients = patients[payload.patient]
        doctor: Doctors = doctors[payload.doctor]
        appointment = Appointments(
            id=id,
            patient=patient,
            doctor=doctor,
            date=payload.date
        )
        appointments.append(appointment)
        return appointment
    
    @staticmethod
    def get_appointment_by_id(appointment_id: int):
        appointment = AppointmentHelpers.get_appointment_by_id(appointment_id)
        if not appointment:
            raise HTTPException(detail='Appointment not found', status_code=404)
        return appointment
    
    @staticmethod
    def edit_apppointment(appointment_id: int, payload: AppointmentsCreate):
        appointment: Appointments = AppointmentHelpers.get_appointment_by_id(appointment_id)
        if not appointment:
            raise HTTPException(detail='Appointment not found', status_code=404)
        patient: Patients = patients[payload.patient]
        doctor: Doctors = doctors[payload.doctor]

        appointment.patient = patient
        appointment.doctor = doctor
        appointment.date = payload.date
        return appointment
    
    @staticmethod
    def delete_appointment(appointment_id):
        appointment: Appointments = AppointmentHelpers.get_appointment_by_id(appointment_id)
        if not appointment:
            raise HTTPException(detail='Appointment not found', status_code=404)
        del appointments[appointment_id]
