import tkinter as tk
from tkinter import messagebox
from data_structures.trees import AppointmentTree
from models.appointment import Appointment

appointment_tree = AppointmentTree()

class AppointmentManagementGUI:
    def __init__(self, root, back_callback):
        self.root = root
        self.back_callback = back_callback
        self.clear_window()

        self.label = tk.Label(root, text="Appointment Management", font=("Arial", 24))
        self.label.pack(pady=20)

        self.add_button = tk.Button(root, text="Add Appointment", command=self.add_appointment)
        self.add_button.pack(pady=10)

        self.search_button = tk.Button(root, text="Search Appointment", command=self.search_appointment)
        self.search_button.pack(pady=10)

        self.list_button = tk.Button(root, text="List All Appointments", command=self.list_all_appointments)
        self.list_button.pack(pady=10)

        self.back_button = tk.Button(root, text="Back", command=self.back_callback)
        self.back_button.pack(pady=10)

    def add_appointment(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="Add Appointment", font=("Arial", 18))
        self.label.pack(pady=10)

        self.id_label = tk.Label(self.root, text="Appointment ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        self.patient_label = tk.Label(self.root, text="Patient ID:")
        self.patient_label.pack()
        self.patient_entry = tk.Entry(self.root)
        self.patient_entry.pack()

        self.doctor_label = tk.Label(self.root, text="Doctor ID:")
        self.doctor_label.pack()
        self.doctor_entry = tk.Entry(self.root)
        self.doctor_entry.pack()

        self.date_label = tk.Label(self.root, text="Date (YYYY-MM-DD):")
        self.date_label.pack()
        self.date_entry = tk.Entry(self.root)
        self.date_entry.pack()

        self.time_label = tk.Label(self.root, text="Time (HH:MM):")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.root)
        self.time_entry.pack()

        self.submit_button = tk.Button(self.root, text="Submit", command=self.save_appointment)
        self.submit_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def save_appointment(self):
        appointment_id = int(self.id_entry.get())
        patient_id = int(self.patient_entry.get())
        doctor_id = int(self.doctor_entry.get())
        date = self.date_entry.get()
        time = self.time_entry.get()
        appointment = Appointment(appointment_id, patient_id, doctor_id, date, time)
        appointment_tree.insert(appointment)
        messagebox.showinfo("Success", "Appointment added successfully.")

    def search_appointment(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="Search Appointment", font=("Arial", 18))
        self.label.pack(pady=10)

        self.id_label = tk.Label(self.root, text="Appointment ID:")
        self.id_label.pack()
        self.id_entry = tk.Entry(self.root)
        self.id_entry.pack()

        self.search_button = tk.Button(self.root, text="Search", command=self.perform_search)
        self.search_button.pack(pady=10)

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def perform_search(self):
        appointment_id = int(self.id_entry.get())
        appointment = appointment_tree.search(appointment_id)
        if appointment:
            messagebox.showinfo("Appointment Found", f"Appointment ID: {appointment.appointment_id}\nPatient ID: {appointment.patient_id}\nDoctor ID: {appointment.doctor_id}\nDate: {appointment.date}\nTime: {appointment.time}")
        else:
            messagebox.showerror("Appointment Not Found", "No appointment found with the given ID.")

    def list_all_appointments(self):
        self.clear_window()
        self.label = tk.Label(self.root, text="All Appointments", font=("Arial", 18))
        self.label.pack(pady=10)

        appointments = appointment_tree.in_order_traversal()
        if appointments:
            for appointment in appointments:
                appointment_label = tk.Label(self.root, text=f"ID: {appointment.appointment_id}, Patient ID: {appointment.patient_id}, Doctor ID: {appointment.doctor_id}, Date: {appointment.date}, Time: {appointment.time}")
                appointment_label.pack()
        else:
            messagebox.showinfo("No Appointments", "No appointments found.")

        self.back_button = tk.Button(self.root, text="Back", command=self.__init__)
        self.back_button.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
