class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Name cannot be empty.")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative.")
        self._age = value

    def view_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Patient(Person):
    def __init__(self, name, age, medical_record):
        super().__init__(name, age)
        self._medical_record = medical_record

    @property
    def medical_record(self):
        return self._medical_record

    @medical_record.setter
    def medical_record(self, value):
        self._medical_record = value

    def view_record(self):
        return f"Patient Record: {self.medical_record}"


class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age)
        self._position = position

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    def view_info(self):
        return f"Staff Name: {self.name}, Age: {self.age}, Position: {self.position}"


class Hospital:
    def __init__(self, name, location):
        self._name = name
        self._location = location
        self._departments = []

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location

    @property
    def departments(self):
        return self._departments

    def add_department(self, department):
        self._departments.append(department)
        print(f"Department '{department.name}' added to {self.name}.")

    def view_departments(self):
        print("All departments:")
        for department in self._departments:
            print(f"Department Name: {department.name}")


class Department:
    def __init__(self, name):
        self._name = name
        self._patients = []
        self._staff = []

    @property
    def name(self):
        return self._name

    @property
    def patients(self):
        return self._patients

    @property
    def staff(self):
        return self._staff

    def add_patient(self, patient):
        self._patients.append(patient)
        print(f"Patient '{patient.name}' added to {self.name} department.")

    def add_staff(self, staff_member):
        self._staff.append(staff_member)
        print(f"Staff '{staff_member.name}' added to {self.name} department.")


print("Welcome to the hospital")
hospital = Hospital(input("Enter hospital name: "), input("Enter hospital location: "))

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
                input("Enter medical record: ")
            )
            print("Choose department:")
            for i in range(len(hospital.departments)):
                print(f"{i + 1}: {hospital.departments[i].name}")
            number = int(input("Enter department number: "))
            hospital.departments[number - 1].add_patient(patient)

    elif choice == "3":
        if len(hospital.departments) == 0:
            print("Please add a department first.")
        else:
            staff = Staff(
                input("Enter staff name: "),
                int(input("Enter staff age: ")),
                input("Enter position: ")
            )
            print("Choose department:")
            for i in range(len(hospital.departments)):
                print(f"{i + 1}: {hospital.departments[i].name}")
            number = int(input("Enter department number: "))
            hospital.departments[number - 1].add_staff(staff)

    elif choice == "4":
        hospital.view_departments()

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