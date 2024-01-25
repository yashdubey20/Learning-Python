# Exception Handling
# Run Time Error
'''try:
    print(2/0)
except ZeroDivisionError as message: # ZeroDivisionError is class
    print("The Description of Error", message)
print(a/b)'''

# Handling
'''a = int(input("Enter The First No"))
b = int(input("Enter The Second No"))
try:
    print(a/b)
except:
    print("Can't Divide by Zero")'''

# Class of Handling
'''try:
    print(2/0)
except ZeroDivisionError as message: # ZeroDivisionError is class
    print("The Description of Error", message)'''

# Special Symbol
'''try:
    a = int(input("Enter The First No: "))
    b = int(input("Enter The Second No: "))
    print(a/b) 
except ZeroDivisionError as message: # ZeroDivisionError is class
    print("Please Ensure you Cannot divide a Number by Zero", message) # if entered 0
except ValueError as message:
    print("Enter only Integer", message)''' # if special symbol is entered    

# Two Exception in single class

'''try:
    a = int(input("Enter The First No: "))
    b = int(input("Enter The Second No: "))
    print(a/b) 
except (ValueError, ZeroDivisionError) as message:
    print(message)'''

# Default Except Block

'''try:
    a = int(input("Enter The First No: "))
    b = int(input("Enter The Second No: "))
    print(a/b) 
except (ValueError, ZeroDivisionError) as message:
    print(message)
except:
    print("This is default part of except block")'''
# Note: default except block cannot be the first except statement

# Using Else
'''try:
    a = int(input("Enter The First No: "))
    b = int(input("Enter The Second No: "))
    print(a/b) 
except (ValueError, ZeroDivisionError) as message:
    print("Enter Correct Number" ,message)
else:
    print("Everything is ok")'''

# Finally Block

'''try:
    a = int(input("Enter The First No: "))
    b = int(input("Enter The Second No: "))
    print(a/b) 
except (ValueError, ZeroDivisionError) as message:
    print("Enter Correct Number" ,message)
finally:
    print("Finally Block will always run wheather there is a error or not")'''

# Nested Try Except Block: We can Write a try block inside a try block
'''try:
    a = int(input("Enter the First Number: "))
    b = int(input("Enter the Second Number: "))
    try:
        print(a/b)
    except ZeroDivisionError as msg:
        print(msg)

except ValueError as msg:
    print(msg)'''

# Taking All Together
'''try:
    a = int(input("Enter The First No: "))
    b = int(input("Enter The Second No: "))
    print(a/b) 
except (ValueError, ZeroDivisionError) as message:
    print(message)
else:
    print("There are No Error in Try block")
finally:
    print("Finally block will always executed no matter what")'''

# User Defined Exception

bank_bal = 2000
if bank_bal>1000:
    raise Exception("Your Account is above limit")
else:
    print("Your Amount is Not sufficent")


       
