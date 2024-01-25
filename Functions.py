# def add(): #called function
#     print(2+2)

# add() #calling function
# add()
# add()

# DEFAULT ARGUMENT 
'''def login():
    while True:
        username = input("Enter the Username")
        password = input("Enter the Password")
        if username == password:
            print("Login succesful")
            break
        else:
            print("Login Failed")
        
login()'''

#POSITONAL ARGUMENT
'''def info(firstname,lastname):
    print("First Name: ", firstname)
    print("Last Name: ", lastname)
info("Yash","Dubey")'''

'''def add(num1,num2):
    return num1+num2
result = add(5,6)
print(result)'''

'''def arth(a,b):
    r = a+b
    g = a-b
    c = a*b #python func can return multiple calue at a time
    return r,g,c

result = arth(5,8) # calling func
print("Result: ", result)'''

# KEYWORD ARGUMENT
'''def func(fname,lname):
    print("Hello",fname)
    print("Hello",lname)

func(fname="Yash",lname="Dubey")'''

'''def func(fname,lname):
    print("Hello",fname)
    print("Hello",lname)
fname = input("Enter fname")
lname = input("Enter lname")
func(fname,lname)'''

#DEFAULT ARUGMENT
'''def func(city = "nagpur"):
    print("I am from ",city)

func("Delhi")
func("LA")
func()'''

# VARIABLE LENGHT ARGUMENT
'''def name(name):
    print(name)

name("Yash", "Overwatch", "Valorant") #To send multiple value at a time'''

# LOCAL & GLOBAL VARIABLE
def info_one():
    global x
    x = 17
    print("X=", x)
    
def info_two():
    print("X=", x)

info_one()
info_two()