Name =""
Age = 0
PhoneNumber = 0
name1 = ""
city = ""
state= ""
Maths=0
Physics=0
Chemistry=0
total=0
Average=0
def personal_info():
    while True:
        username = input("Enter the Username: ")
        password = input("Enter the Password: ")
        if username == password:
            print("Login succesful")
            break
        else:
            print("Login Failed") 
personal_info()
def login():
            global Name
            global Age
            global PhoneNumber
            Name = input("Enter Your Name")
            Age = int(input("Enter Your Age"))
            PhoneNumber= int(input("Enter Your Number"))
login()

def college_info():
    global name1
    global city
    global state
    name1 = input("Enter the Name of the college: ")
    city = input("Enter the Name of the city: ")
    state = input("Enter the name of the state: ")
college_info()

def get_marks():
    global Maths, Physics, Chemistry, total, Average
    Maths = int(input("Enter the marks of Maths"))
    Physics = int(input("Enter the marks of Physics"))
    Chemistry = int(input("Enter the marks of chemistry"))
    total = Maths+Physics+Chemistry
    Average = total/3.0
    print("Total Marks= ",total)
    print("Total Avg= ",Average)
get_marks()


print("=========================================")
print("        Name of The Person: ", Name)
print("         Age of The Person: ",Age)
print("           Contact Info: ",PhoneNumber)
print("=========================================")
print("        Name of The College: ", name1)
print("        Name of The City: ", city)
print("        Name of The State: ", state)
print("=========================================")
print("           Enter Your Marks               ")
print("          Your Maths Marks are: ",Maths)
print("          Your Physics Marks are: ",Physics)
print("          Your Chemistry Marks are: ",Chemistry)
print("            Your Total is: ", total)
print("              Your Average is: ",Average)
print("=========================================")









    
         
