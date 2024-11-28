from patient_library import Patient, PatientManager
import time

def main():
    manager = PatientManager()
    manager.start_icu_consumer()  # Start ICU consumer thread

    while True:
        print("\nOptions:")
        print("1. Add a new patient")
        print("2. View all patients")
        print("3. Remove highest-priority patient")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()
        if choice == "1":
            # Create a new patient
            patient_name = input("Enter the patient's name: ").strip()
            try:
                patient_age = int(input("Enter the patient's age: "))
            except ValueError:
                print("Invalid input. Age must be a number.")
                continue
            patient_sex = input("Enter the patient's sex (Male/Female): ").strip()

            patient = Patient(patient_name, patient_age, patient_sex)
            patient.calculate_esi_priority()

            # Measure time for adding the patient
            start_time = time.perf_counter()
            manager.push(patient)
            end_time = time.perf_counter()
            print(f"Time taken to add patient: {end_time - start_time:.6f} seconds")

        elif choice == "2":
            # Measure time for listing all patients
            start_time = time.perf_counter()
            manager.list_patients()
            end_time = time.perf_counter()
            print(f"Time taken to list patients: {end_time - start_time:.6f} seconds")

        elif choice == "3":
            # Measure time for removing the highest-priority patient
            start_time = time.perf_counter()
            manager.pop()
            end_time = time.perf_counter()
            print(f"Time taken to remove patient: {end_time - start_time:.6f} seconds")

        elif choice == "4":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
