class Student:
    def my_function(self):
        self.name  = input("Enter Your Name: ")
        self.marks = int(input("Enter Your Marks: "))
        print(self.name)
        print(self.marks)

std1=Student()
std1.my_function()
