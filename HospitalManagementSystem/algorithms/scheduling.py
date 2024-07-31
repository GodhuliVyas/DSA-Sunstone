#Scheduling Algorithms: Implement algorithms for managing doctor appointments and time slot allocation.


class AppointmentScheduler:
    def __init__(self):
        self.schedule = {}

    def schedule_appointment(self, doctor_id, patient_id, time_slot):
        if doctor_id not in self.schedule:
            self.schedule[doctor_id] = {}
        if time_slot not in self.schedule[doctor_id]:
            self.schedule[doctor_id][time_slot] = patient_id
            return True
        else:
            return False

    def get_doctor_schedule(self, doctor_id):
        return self.schedule.get(doctor_id, {})

    def cancel_appointment(self, doctor_id, time_slot):
        if doctor_id in self.schedule and time_slot in self.schedule[doctor_id]:
            del self.schedule[doctor_id][time_slot]
            return True
        else:
            return False
