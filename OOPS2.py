# STATIC VARIABLES
'''class New:
    self.name = 10

    def __init__(self):
        self.name = "Yash"

obj = New()
obj1 = New()
obj2 = New()'''

# Example 1
'''class College:
    collegenames = "Modern Name" # Static Variable

    def __init__(self):
        self.studentname = "Yash"

princple = College()
teacher = College()
accountant = College()
print("Prinicpal = ",princple.collegenames,"   ",princple.studentname)
print("Teacher = ",teacher.collegenames,"   ",teacher.studentname)
print("Accountant = ",accountant.collegenames,"   ",accountant.studentname)

College.collegenames = "HBD" # Second way to add a static variable
princple.studentname = "Yash Dubey"

print("Prinicpal = ",princple.collegenames," | ",princple.studentname)
print("Teacher = ",teacher.collegenames," | ",teacher.studentname)
print("Accountant = ",accountant.collegenames," | ",accountant.studentname)'''

# Example 2
'''class Student:
    def __init__(self,name,rollno,mob):
        self.name= name
        self.rollno= rollno
        self.mob = mob
    def display(self):
        print(self.name," ",self.rollno,"",self.mob)
        
stud = Student("Yash", 1001, 4646)
stud.display()'''

# Static Method
class Student:
    @staticmethod
    def get_personal_detail(firstname,lastname):
        print("Your personal detail:" , firstname,lastname)

    @staticmethod
    def contact_details(mob,rollno):
        print("Your contact details= ", mob,rollno)

Student.get_personal_detail("Yash", "Dubey")
Student.contact_details(7506703222,38)
