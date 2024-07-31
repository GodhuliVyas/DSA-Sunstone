class Appointment:
    def __init__(self, appointment_id, patient_id, doctor_id, date, time):
        self.appointment_id = appointment_id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

    def __str__(self):
        return f"ID: {self.appointment_id}, Patient ID: {self.patient_id}, Doctor ID: {self.doctor_id}, Date: {self.date}, Time: {self.time}"
