class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def view_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self.medical_record = medical_record

    def view_record(self):
        return f"Patient Record: {self.medical_record}"


class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self.position = position

    def view_info(self):
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Hospital:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.departments = []

    def add_department(self, department):
        self.departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")

    def view_departments(self):
        print("All departments:")
        for department in self.departments:
            print(f"Department Name: {department.name}")


class Department:
    def __init__(self, name):
        self.name = name
        self.patients = []
        self.staff = []

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")


print("Welcome to the hospital!")
hospital = Hospital(input("Enter hospital name: "),input("Enter hospital location: "))

while True:
    print("\nChoose an operation:")
    print("1: Add Department")
    print("2: Add Patient")
    print("3: Add Staff")
    print("4: View Departments")
    print("5: View Patients")
    print("6: View Staff")
    print("7: Exit")

    choice = input("Enter your choice: ")
    if choice == "1":
        department = Department(input("Enter department name: "))
        hospital.add_department(department)

    elif choice == "2":
        if len(hospital.departments) == 0:
            print("Please add a department first.")
        else:
            patient = Patient(
                input("Enter patient name: "),
                int(input("Enter patient age: ")),
                input("Enter medical record: "))
            print("Choose department:")
            for i in range(len(hospital.departments)):
                print(i + 1, hospital.departments[i].name)
            number = int(input("Enter department number: "))
            hospital.departments[number - 1].add_patient(patient)

    elif choice == "3":
        if len(hospital.departments) == 0:
            print("Please add a department first.")
        else:
            staff = Staff(input("Enter staff name: "),int(input("Enter staff age: ")),input("Enter position: "))
            print("Choose department:")
            for i in range(len(hospital.departments)):
                print(i + 1, hospital.departments[i].name)
            number = int(input("Enter department number: "))
            hospital.departments[number - 1].add_staff(staff)

    elif choice == "4":hospital.view_departments()

    elif choice == "5":
        for department in hospital.departments:
            print("\nDepartment:", department.name)
            for patient in department.patients:
                print(patient.view_info())
                print(patient.view_record())

    elif choice == "6":
        for department in hospital.departments:
            print("\nDepartment:", department.name)
            for staff in department.staff:
                print(staff.view_info())
    elif choice == "7":

        print("Goodbye!")
        break
    else:
        print("Invalid choice!")