class Hospital():
    # Constructor
    def __init__(self, name, address):
        self.doctors = []
        self.patients = []
        self.name = name
        self.address = address
    # Add New Doctor 
    def add_doctor(self, new_doctor_name):
        return self.doctors.append(new_doctor_name)
    # Remove Doctor 
    def remove_doctor(self, remove_doctor):
        return self.doctors.remove(remove_doctor)
    # Display Doctors Detail
    def get_doctor(self):
        return self.doctors
    
    # Add New Patient 
    def add_patient(self, new_patient_name):
        return self.patients.append(new_patient_name)
    # Remove Patient
    def remove_patient(self, remove_patient):
        return self.patients.remove(remove_patient)
    # Display Patient Detail
    def get_patient(self):
        return self.patients

class Doctor():
    # Constructor
    def __init__(self, dname, field):
        self.dname = dname
        self.field = field    

class Patient():
    # Constructor
    def __init__(self, pname, diesease):
        self.pname = pname
        self.diesease = diesease

hosp1 = Hospital("Shamsi Hospital", "Shamsi Society Malir Halt")
doctor1 = Doctor("Fareed", "Skin Specialist")
patient1 = Patient("Saeed", "Heart Diesease")

doctor2 = Doctor("Rasheed", "Heart Seargeon")
patient2 = Patient("Anwar", "Skin Diesease")

doctor3 = Doctor("Shakeel", "Dental ")
patient3 = Patient("Anwar", "Teeth Diesease")


hosp1.add_doctor(doctor1.dname)
hosp1.add_doctor(doctor2.dname)
hosp1.add_doctor(doctor3.dname)
hosp1.add_doctor(doctor1.field)
hosp1.add_doctor(doctor2.field)
hosp1.add_doctor(doctor3.field)

# Hospital.add_doctor(doctor1)
# Hospital.add_patient(patient1)

# Hospital.add_doctor(doctor2)
# Hospital.add_patient(patient2)

# Hospital.add_doctor(doctor3)
# Hospital.add_patient(patient3)

print(Hospital.get_doctor)
print(Hospital.get_patient)

