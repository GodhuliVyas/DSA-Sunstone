#main_menu.py: Main menu to navigate through different functionalities.


from views.patient_management import patient_management_menu
from views.appointment_management import appointment_management_menu
from views.inventory_management import inventory_management_menu

def main_menu():
    while True:
        print("Hospital Management System")
        print("1. Patient Management")
        print("2. Doctor Appointments")
        print("3. Inventory Management")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            patient_management_menu()
        elif choice == '2':
            appointment_management_menu()
        elif choice == '3':
            inventory_management_menu()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
