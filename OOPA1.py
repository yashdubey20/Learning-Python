# CLASS
'''class New:
    x = 10 # data member inside of a class
    def display(self): # data member function of a class
        print("Hello Python")

obj = New()
obj.display()
print(obj.x)'''

# Constructor
# Python class is having a default constructor
# By using Construtor we initalize the object

'''class Newclass:
    def __init__(self):
        print("Constructor gets called auatomatically and will execute first")

    def show(self):
        print("Function")

obj = Newclass()      
obj.show()'''

# Constructor with Variables
'''class Hod:
    def __init__(self):
        self.name = "Yash"
        self.age = 20
        self.empid = 38

    def info(self):
        print("My Name is: ",self.name)
        print("My Age is: ",self.age)
        print("My Empid is: ",self.empid)

obj = Hod()
obj.info()'''

# Class Variable: instance,local & static
# Class Method: class,static & instance

# Declaring instance variable inside a constructor by using self Variable

'''class Student:
    def __init__(self):
        self.fname = "Yash"
        self.lname = "Dubey" #Instance Variable
        self.rollno = 38
        self.branch = "Comp"
        self.mb = 00000000

obj = Student()
print(obj.__dict__)'''

'''class Student:
    def __init__(self):
        self.fname = "Yash"
        self.lname = "Dubey" #Instance Variable
        self.rollno = 38
        self.branch = "Comp"
        self.mb = 00000000

obj = Student()
print(obj.__dict__)'''

'''class Student:
    def __init__(self):
        self.fname = "Yash"
        self.lname = "Dubey" #Instance Variable
        self.rollno = 38
        self.branch = "Comp"
        self.mb = 00000000

obj = Student()
print(obj.__dict__)'''

'''class Student:
    def __init__(self):
        self.fname = "Yash"
        self.lname = "Dubey" #Instance Variable
        self.rollno = 38
        self.branch = "Comp"
        self.mb = 00000000

obj = Student()
print(obj.__dict__)'''

'''class Student:
    def __init__(self):
        self.fname = "Yash"
        self.lname = "Dubey" #Instance Variable
        self.rollno = 38
        self.branch = "Comp"
        self.mb = 00000000
    def getdata(self): # Instance Method
        self.yash = 88888888

obj = Student() # Untill and Unless we call the Method it will not added to the object
obj.getdata()
print(obj.__dict__)'''

# Declaring instance variable outside a class by using object

'''class Student:
    def __init__(self):
        self.fname = "Yash"
        self.lname = "Dubey" #Instance Variable
        self.rollno = 38
        self.mb = 00000000
    def getdata(self): # Instance Method
        self.yash = 88888888

obj = Student() 
obj.getdata()
obj.branch = "Comp" # Adding instance variable by using object
print(obj.__dict__)'''

# Accessing and Deleting Instance Variable from the Class

class Student:
    def __init__(self):
        self.fname = "Yash"
        self.lname = "Dubey" #Instance Variable
        self.rollno = 38
        self.mb = 00000000
    def getdata(self): # Instance Method
        self.yash = 88888888

obj = Student() 
obj.getdata()
obj.branch = "Comp" # Adding
del obj.rollno #Deleting 
print(obj.fname) #Accessing
print(obj.__dict__)








        