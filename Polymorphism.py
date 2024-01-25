# Example Polymorphism

'''class Principal:
    def role(self):
        print("I am the Princpal")

class Dean:
    def role(self):
        print("I am the Dean")

class Hod:
    def role(self):
        print("I am the Hod")

class Teacher:
    def role(self):
        print("I am the Teacher")    

def func(obj):
    obj.role()

campus = [Principal(), Dean(),Hod(),Teacher()]   
for obj in campus:
    func(obj)'''


# Operator Overloading

'''class Deposit:
    def __init__(self):
        self.cash = self.cash

d1 = Deposit(1000)
d2 = Deposit(2000)
print(d1+d2)'''

# Operator Overloading # Magic Method
# __add__ method is a amagic method

'''class Deposit:
    def __init__(self,cash):
        self.cash = cash
    def __add__(self,other):
        return self.cash + other.cash
    
d1 = Deposit(1000)
d2 = Deposit(2000)
print("The Deposited Amount is: ",d1+d2)'''

# Method Overloading
# In python Method overloading is not possible

'''class Add:
    def add(self,a):
        print(a)
    def add(self,a,b):
        print(a+b)
    def add(self,a,b,c): # O/P: b & c values are missing
        print(a+b+c)  # it will consider last function

obj = Add()
obj.add(10)
obj.add(12,23)
obj.add(10,20,30)'''
    
# Solution

'''class Add:
    def __init__(self):
        print("There is no Argument")
    def __init__(self,a):
        print("Passing One Argument")
    def __init__(self,a,b):
        print("Passing Two Arguments")

obj = Add(3,6)'''

# Method Overloading Concept

'''class Father:
    def bike(self):
        print("Harley Devidson")
    
    def laptop(self):
        print("Laptop with 2GB RAM and 500GB HDD I3") # It will be over written

class Aman(Father):
    def laptop(self): # It will overwrite Father Laptop Func
        print("Tis Wont do")
        print("Laptop with 8GB RAM & I7")
        super().laptop() # Solution

obj = Aman()
obj.bike()
obj.laptop()'''

# Constructor Overwriting
class Father:
    def __init__(self):
        print("Father")

class Child(Father):
    def __init__(self):
        print("Child")
        super().__init__()

obj = Child()