# Interface for managing patient records.

from data_structures.trees import PatientTree
from models.patient import Patient

patient_tree = PatientTree()

def patient_management_menu():
    while True:
        print("\nPatient Management")
        print("1. Add Patient")
        print("2. Search Patient")
        print("3. List All Patients")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_patient()
        elif choice == '2':
            search_patient()
        elif choice == '3':
            list_all_patients()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def add_patient():
    patient_id = int(input("Enter Patient ID: "))
    name = input("Enter Patient Name: ")
    age = int(input("Enter Patient Age: "))
    patient = Patient(patient_id, name, age)
    patient_tree.insert(patient)
    print("Patient added successfully.")

def search_patient():
    patient_id = int(input("Enter Patient ID to search: "))
    patient = patient_tree.search(patient_id)
    if patient:
        print(f"Patient found: {patient}")
    else:
        print("Patient not found.")

def list_all_patients():
    # Implement a method to traverse the tree and list all patients
    pass
