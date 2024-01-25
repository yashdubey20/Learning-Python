# Project 1

class Hospital:
    nameH = input("Name of The Hosptal is: ")
    address = input("Adress of the Hospital: ")
    city = input("City: ")
    state = input("State: ")
    print("==============================================")

class Patient:
    patientN = input("Name of The Patient: ")
    age = int(input("Age: "))
    bloodg = input("Blood Group: ")
    fname = input("Father of The Patient: ")
    mname = input("Mother of The Patient: ")
    print("==============================================")

class HospitalStaff:
    docN = input("Name of The Doctor: ")
    nurse1 = input("Name of The Nurse: ")
    attendent = input("Name of The Attendent: ")
    print("==============================================")

class Pharmacy(Hospital,Patient,HospitalStaff):
    def total(self):
        self.namep = input("Name of The Pharmacy: ")
        self.medprac = input("Name of The First Medicine: ")
        self.med1 = int(input("Price of Paracetamol: "))
        self.inj = input("Name of The Injection: ")
        self.injp = int(input("Price of The Injection: "))
        self.hosp = int(input("Number of Days in Hospital: "))
        self.hosp1 = int(input("Hospital Bill: "))
        self.totalbill  = self.med1 + self.injp + self.hosp1
        self.discount = (self.totalbill*10)/100
        if self.totalbill>10000:
            print("Your Final Bill After Discount is: ",self.totalbill-self.discount)
        else:
            print("Your Total Bill is: ",self.totalbill)
        print("==============================================")

obj = Pharmacy()
obj.total()

# Can add one more class
# Can represent more nicely by taking 