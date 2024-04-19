from schema.appointment import appointments

class AppointmentHelpers:

    @staticmethod
    def get_appointment_by_id(appointment_id: int):
        for appointment in appointments:
            if appointment.id == appointment_id:
                return appointment
        return None