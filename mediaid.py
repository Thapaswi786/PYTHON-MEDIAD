class MedicalDataManagement:
    def __init__(self):
        self.patients = {}

    def add_patient(self):
        """Gets input from the user to add a new patient."""
        patient_id = input("Enter Patient ID: ")
        name = input("Enter Name: ")
        age = input("Enter Age: ")
        gender = input("Enter Gender: ")
        contact = input("Enter Contact: ")
        ailment = input("Enter Ailment: ")
        prescription = input("Enter Prescription: ")

        self.patients[patient_id] = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Contact": contact,
            "Ailment": ailment,
            "Prescription": prescription,
            "Lab Tests": {}
        }
        print(f"\nPatient {name} added successfully!\n")

    def delete_patient(self):
        """Deletes a patient based on user input."""
        patient_id = input("Enter Patient ID to delete: ")
        if patient_id in self.patients:
            del self.patients[patient_id]
            print(f"\nPatient {patient_id} deleted successfully!\n")
        else:
            print("\nPatient not found!\n")

    def update_patient(self):
        """Gets input from the user to update an existing patient."""
        patient_id = input("Enter Patient ID to update: ")
        if patient_id in self.patients:
            print("\nLeave blank if no change is needed.")
            name = input("Enter Name: ") or self.patients[patient_id]["Name"]
            age = input("Enter Age: ") or self.patients[patient_id]["Age"]
            gender = input("Enter Gender: ") or self.patients[patient_id]["Gender"]
            contact = input("Enter Contact: ") or self.patients[patient_id]["Contact"]
            ailment = input("Enter Ailment: ") or self.patients[patient_id]["Ailment"]
            prescription = input("Enter Prescription: ") or self.patients[patient_id]["Prescription"]

            self.patients[patient_id] = {
                "Name": name,
                "Age": age,
                "Gender": gender,
                "Contact": contact,
                "Ailment": ailment,
                "Prescription": prescription,
                "Lab Tests": self.patients[patient_id]["Lab Tests"]
            }
            print(f"\nPatient {patient_id} updated successfully!\n")
        else:
            print("\nPatient not found!\n")

    def add_lab_test(self):
        """Gets input from the user to add lab test results."""
        patient_id = input("Enter Patient ID: ")
        if patient_id in self.patients:
            test_name = input("Enter Lab Test Name: ")
            result = input("Enter Lab Test Result: ")
            self.patients[patient_id]["Lab Tests"][test_name] = result
            print(f"\nLab test '{test_name}' added for Patient {patient_id}.\n")
        else:
            print("\nPatient not found!\n")

    def view_patient(self):
        """Gets input from the user to display patient details."""
        patient_id = input("Enter Patient ID to view: ")
        if patient_id in self.patients:
            print("\nPatient Details:")
            for key, value in self.patients[patient_id].items():
                print(f"{key}: {value}")
            print("\n")
        else:
            print("\nPatient not found!\n")

    def menu(self):
        """Displays menu options for user interaction."""
        while True:
            print("\nMedical Data Management System")
            print("1. Add Patient")
            print("2. Update Patient")
            print("3. Delete Patient")
            print("4. Add Lab Test")
            print("5. View Patient")
            print("6. Exit")

            choice = input("\nEnter your choice: ")

            if choice == "1":
                self.add_patient()
            elif choice == "2":
                self.update_patient()
            elif choice == "3":
                self.delete_patient()
            elif choice == "4":
                self.add_lab_test()
            elif choice == "5":
                self.view_patient()
            elif choice == "6":
                print("\nExiting program... Goodbye!\n")
                break
            else:
                print("\nInvalid choice! Please try again.\n")


medical_db = MedicalDataManagement()
medical_db.menu()