def welcome(fname,lname):
    print("First Name: ",fname)
    print("Last Name: ",lname)
welcome("Yash", "Dubey")

def square(n):
    print(n*n)

pi= 3.14

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
        