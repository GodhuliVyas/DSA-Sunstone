import tkinter as tk
from tkinter import messagebox
from data_structures.trees import PatientTree
from models.patient import Patient

patient_tree = PatientTree()

class PatientManagementGUI:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = back_callback
        self.clear_window()

        self.label = tk.Label(root, text="Patient Management", font=("Arial", 24))
        self.label.pack(pady=20)

        self.add_button = tk.Button(root, text="Add Patient", command=self.add_patient)
        self.add_button.pack(pady=10)

        self.search_button = tk.Button(root, text="Search Patient", command=self.search_patient)
        self.search_button.pack(pady=10)

        self.list_button = tk.Button(root, text="List All Patients", command=self.list_all_patients)
        self.list_button.pack(pady=10)

        self.back_button = tk.Button(root, text="Back", command=self.back_callback)
        self.back_button.pack(pady=10)

    def add_patient(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="Add Patient", font=("Arial", 18))
        self.label.pack(pady=10)

        self.id_label = tk.Label(self.root, text="Patient ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        self.name_label = tk.Label(self.root, text="Patient Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.age_label = tk.Label(self.root, text="Patient Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.save_patient)
        self.submit_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def save_patient(self):
        patient_id = int(self.id_entry.get())
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        patient = Patient(patient_id, name, age)
        patient_tree.insert(patient)
        messagebox.showinfo("Success", "Patient added successfully.")

    def search_patient(self):
        # Similar to add_patient, create a form for searching patients
        pass

    def list_all_patients(self):
        # Implement logic to list all patients
        pass

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
