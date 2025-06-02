from datetime import datetime
from tabulate import tabulate
from dateutil import parser
import json
import os

class Patient:
    def __init__(self, patient_id, name, age, gender, contact):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.gender = gender
        self.contact = contact
        self.medical_history = []
        self.appointments = []

    def add_medical_record(self, diagnosis, prescription, doctor, date):
        record = {
            'date': date,
            'diagnosis': diagnosis,
            'prescription': prescription,
            'doctor': doctor
        }
        self.medical_history.append(record)

    def schedule_appointment(self, date, doctor, reason):
        appointment = {
            'date': date,
            'doctor': doctor,
            'reason': reason
        }
        self.appointments.append(appointment)

class MedicalSystem:
    def __init__(self):
        self.patients = {}
        self.load_data()

    def add_patient(self, name, age, gender, contact):
        patient_id = f"P{len(self.patients) + 1:03d}"
        patient = Patient(patient_id, name, age, gender, contact)
        self.patients[patient_id] = patient
        self.save_data()
        return patient_id

    def get_patient(self, patient_id):
        return self.patients.get(patient_id)

    def display_patient_info(self, patient_id):
        patient = self.get_patient(patient_id)
        if patient:
            print("\nPatient Information:")
            print(f"ID: {patient.patient_id}")
            print(f"Name: {patient.name}")
            print(f"Age: {patient.age}")
            print(f"Gender: {patient.gender}")
            print(f"Contact: {patient.contact}")
        else:
            print("Patient not found!")

    def display_medical_history(self, patient_id):
        patient = self.get_patient(patient_id)
        if patient and patient.medical_history:
            print("\nMedical History:")
            headers = ["Date", "Diagnosis", "Prescription", "Doctor"]
            data = [[record['date'], record['diagnosis'], record['prescription'], record['doctor']] 
                   for record in patient.medical_history]
            print(tabulate(data, headers=headers, tablefmt="grid"))
        else:
            print("No medical history found!")

    def display_appointments(self, patient_id):
        patient = self.get_patient(patient_id)
        if patient and patient.appointments:
            print("\nAppointments:")
            headers = ["Date", "Doctor", "Reason"]
            data = [[appointment['date'], appointment['doctor'], appointment['reason']] 
                   for appointment in patient.appointments]
            print(tabulate(data, headers=headers, tablefmt="grid"))
        else:
            print("No appointments found!")

    def save_data(self):
        data = {}
        for patient_id, patient in self.patients.items():
            data[patient_id] = {
                'name': patient.name,
                'age': patient.age,
                'gender': patient.gender,
                'contact': patient.contact,
                'medical_history': patient.medical_history,
                'appointments': patient.appointments
            }
        with open('medical_data.json', 'w') as f:
            json.dump(data, f, indent=4)

    def load_data(self):
        if os.path.exists('medical_data.json'):
            with open('medical_data.json', 'r') as f:
                data = json.load(f)
                for patient_id, patient_data in data.items():
                    patient = Patient(
                        patient_id,
                        patient_data['name'],
                        patient_data['age'],
                        patient_data['gender'],
                        patient_data['contact']
                    )
                    patient.medical_history = patient_data['medical_history']
                    patient.appointments = patient_data['appointments']
                    self.patients[patient_id] = patient

def main():
    system = MedicalSystem()
    
    while True:
        print("\n=== Medical Data Management System ===")
        print("1. Add New Patient")
        print("2. View Patient Information")
        print("3. Add Medical Record")
        print("4. Schedule Appointment")
        print("5. View Medical History")
        print("6. View Appointments")
        print("7. Exit")
        
        choice = input("\nEnter your choice (1-7): ")
        
        if choice == '1':
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            gender = input("Enter patient gender (M/F): ")
            contact = input("Enter patient contact: ")
            patient_id = system.add_patient(name, age, gender, contact)
            print(f"Patient added successfully! Patient ID: {patient_id}")
            
        elif choice == '2':
            patient_id = input("Enter patient ID: ")
            system.display_patient_info(patient_id)
            
        elif choice == '3':
            patient_id = input("Enter patient ID: ")
            patient = system.get_patient(patient_id)
            if patient:
                diagnosis = input("Enter diagnosis: ")
                prescription = input("Enter prescription: ")
                doctor = input("Enter doctor's name: ")
                date = input("Enter date (YYYY-MM-DD): ")
                patient.add_medical_record(diagnosis, prescription, doctor, date)
                system.save_data()
                print("Medical record added successfully!")
            else:
                print("Patient not found!")
                
        elif choice == '4':
            patient_id = input("Enter patient ID: ")
            patient = system.get_patient(patient_id)
            if patient:
                date = input("Enter appointment date (YYYY-MM-DD): ")
                doctor = input("Enter doctor's name: ")
                reason = input("Enter appointment reason: ")
                patient.schedule_appointment(date, doctor, reason)
                system.save_data()
                print("Appointment scheduled successfully!")
            else:
                print("Patient not found!")
                
        elif choice == '5':
            patient_id = input("Enter patient ID: ")
            system.display_medical_history(patient_id)
            
        elif choice == '6':
            patient_id = input("Enter patient ID: ")
            system.display_appointments(patient_id)
            
        elif choice == '7':
            print("Thank you for using the Medical Data Management System!")
            break
            
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main() 