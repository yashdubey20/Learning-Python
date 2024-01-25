# ABSTRACTION
# ABC(abstract base class)
'''from abc import ABC, abstractmethod
class Programming(ABC):
    @abstractmethod
    def training(self): # Abstract Method
        pass
    @abstractmethod
    def placement(self):
        pass

class Ashish(Programming):
    def training(self):
        print("C, C++, java")
    def placement(self):
        print("Java Placement")

class Ankush(Programming):
    def training(self):
        print("Python & Django")
    def placement(self):
        print("Python Placements")

class Prashant(Programming):
    def training(self):
        print("Machine Learning")
    def placement(self):
        print("Data Structure Placements")

obj1 = Ashish()
obj1.training()
obj2 = Ankush()
obj2.training()
obj3 = Prashant()
obj3.training()'''

# Example 1

'''from abc import ABC, abstractmethod


class IRCTC(ABC):  # abstract class
    @abstractmethod
    def bookTicket(self):  # abstract method
        pass

    @abstractmethod
    def showTicket(self):  # abstract method
        pass


class MakeMyTrip(IRCTC):
    def bookTicket(self):
        print("    Welcome to MakeMyTrip")
        self.source = input("Enter a source station name: ")
        self.destination = input("Enter destination station name: ")
        self.date = input("Enter date: ")

    def showTicket(self):
        print("Source is: ", self.source)


class GoIbibo(IRCTC):
    def bookTicket(self):
        print("    Welcome to GOIBIBO")
        self.source = input("Enter source station name: ")
        self.destination = input("Enter destination station name: ")
        self.date = input("Enter date: ")
    def showTicket(self):
        print("Source is: ", self.source)

class Yatra(IRCTC):
    def bookTicket(self):
        print("   Welcome to Yatra.com  ")
        self.source = input("Enter source station name: ")
        self.destination = input("Enter destination station name: ")
        self.date = input("Enter date: ")
    def showTicket(self):
        print("Source is: ", self.source)

m = MakeMyTrip()
m.bookTicket()
m.showTicket()

g = GoIbibo()
g.bookTicket()
g.showTicket()

y = Yatra()
y.bookTicket()
g.showTicket()'''

# Encapsulation
# Example 2 Private Vairable

'''class Base:  # parent class
    def _init_(self):
        print("Parent class constructor called")
        self.a = "YCCE"  # public data member
        self.__c = "IIM"  # private data member

# Creating a derived class / child class


class Derived(Base):  # child class
    def _init_(self):
        # Calling constructor of Base Class
        Base._init_(self)
        print("Calling private member of Base Class.")
        print(self.__c)


# Driver Code
obj1 = Derived()
# print(obj1.a)
# print(obj1.c)
obj = Base()
print(obj.__c)'''

# Protected Variable

'''class Base:
    def _init_(self):
        print("parent class constructor called")
        self._a = 2
        
class Derived(Base):
    def _init_(self):
        Base._init_(self)
        print("Calling protecetd member of base class : ")
        print("self._a")
obj = Derived()'''    

