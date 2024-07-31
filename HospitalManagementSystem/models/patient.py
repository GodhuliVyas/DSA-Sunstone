class Patient:
    def __init__(self, patient_id, name, age):
        self.id = patient_id
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Patient(ID: {self.id}, Name: {self.name}, Age: {self.age})"
