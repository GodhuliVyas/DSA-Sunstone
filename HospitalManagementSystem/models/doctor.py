class Doctor:
    def __init__(self, doctor_id, name, specialization):
        self.id = doctor_id
        self.name = name
        self.specialization = specialization

    def __repr__(self):
        return f"Doctor(ID: {self.id}, Name: {self.name}, Specialization: {self.specialization})"
