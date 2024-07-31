#appointment_management.py: Interface for managing doctor appointments.

from algorithms.scheduling import AppointmentScheduler

appointment_scheduler = AppointmentScheduler()

def appointment_management_menu():
    while True:
        print("\nAppointment Management")
        print("1. Schedule Appointment")
        print("2. View Doctor Schedule")
        print("3. Cancel Appointment")
        print("4. Back to Main Menu")
        choice = input("Enter your choice: ")

        if choice == '1':
            schedule_appointment()
        elif choice == '2':
            view_doctor_schedule()
        elif choice == '3':
            cancel_appointment()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

def schedule_appointment():
    doctor_id = int(input("Enter Doctor ID: "))
    patient_id = int(input("Enter Patient ID: "))
    time_slot = input("Enter Time Slot (e.g., 10:00 AM): ")
    if appointment_scheduler.schedule_appointment(doctor_id, patient_id, time_slot):
        print("Appointment scheduled successfully.")
    else:
        print("Time slot is already booked. Please choose another slot.")

def view_doctor_schedule():
    doctor_id = int(input("Enter Doctor ID: "))
    schedule = appointment_scheduler.get_doctor_schedule(doctor_id)
    if schedule:
        print(f"Schedule for Doctor ID {doctor_id}: {schedule}")
    else:
        print("No appointments found.")

def cancel_appointment():
    doctor_id = int(input("Enter Doctor ID: "))
    time_slot = input("Enter Time Slot to cancel (e.g., 10:00 AM): ")
    if appointment_scheduler.cancel_appointment(doctor_id, time_slot):
        print("Appointment cancelled successfully.")
    else:
        print("No appointment found for the given time slot.")
