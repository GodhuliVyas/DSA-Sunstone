import tkinter as tk
from tkinter import messagebox
from views.patient_management_gui import PatientManagementGUI
from views.appointment_management_gui import AppointmentManagementGUI
from views.inventory_management_gui import InventoryManagementGUI

class HospitalManagementSystemApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("600x400")

        self.main_menu()

    def main_menu(self):
        self.clear_window()

        label = tk.Label(self.root, text="Hospital Management System", font=("Arial", 24))
        label.pack(pady=20)

        patient_button = tk.Button(self.root, text="Patient Management", command=self.patient_management)
        patient_button.pack(pady=10)

        appointment_button = tk.Button(self.root, text="Doctor Appointments", command=self.appointment_management)
        appointment_button.pack(pady=10)

        inventory_button = tk.Button(self.root, text="Inventory Management", command=self.inventory_management)
        inventory_button.pack(pady=10)

        exit_button = tk.Button(self.root, text="Exit", command=self.root.quit)
        exit_button.pack(pady=10)

    def patient_management(self):
        PatientManagementGUI(self.root, self.main_menu)

    def appointment_management(self):
        AppointmentManagementGUI(self.root, self.main_menu)

    def inventory_management(self):
        InventoryManagementGUI(self.root, self.main_menu)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalManagementSystemApp(root)
    root.mainloop()
