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

        self.name_label = tk.Label(self.root, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self.root)
        self.name_entry.pack()

        self.age_label = tk.Label(self.root, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self.root)
        self.age_entry.pack()

        self.address_label = tk.Label(self.root, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(self.root)
        self.address_entry.pack()

        self.phone_label = tk.Label(self.root, text="Phone:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self.root)
        self.phone_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.save_patient)
        self.submit_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def save_patient(self):
        patient_id = int(self.id_entry.get())
        name = self.name_entry.get()
        age = int(self.age_entry.get())
        #address = self.address_entry.get()
        #phone = self.phone_entry.get()
        patient = Patient(patient_id, name, age)
        patient_tree.insert(patient_id, patient)  # Fix here: provide both key and value
        messagebox.showinfo("Success", "Patient added successfully.")

    def search_patient(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="Search Patient", font=("Arial", 18))
        self.label.pack(pady=10)

        self.id_label = tk.Label(self.root, text="Patient ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        self.search_button = tk.Button(self.root, text="Search", command=self.perform_search)
        self.search_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def perform_search(self):
        patient_id = int(self.id_entry.get())
        patient = patient_tree.search(patient_id)
        if patient:
            messagebox.showinfo("Patient Found", f"ID: {patient.patient_id}\nName: {patient.name}\nAge:")
        else:
            messagebox.showerror("Patient Not Found", "No patient found with the given ID.")

    def list_all_patients(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="All Patients", font=("Arial", 18))
        self.label.pack(pady=10)

        patients = patient_tree.in_order_traversal()
        if patients:
            for patient in patients:
                patient_label = tk.Label(self.root, text=f"ID: {patient.patient_id}, Name: {patient.name}, Age: {patient.age}")
                patient_label.pack()
        else:
            messagebox.showinfo("No Patients", "No patients found.")

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
