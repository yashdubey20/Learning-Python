# WHILE LOOP
'''i = 1
while i<6:
    print(i)
    i=i+1'''
# When you know the range you use for loop but when u dont know the range us while loop
'''i=0
while i<6:
    i = i+1
    if i == 3:
        continue 
    print(i)'''

'''i=0
while i<6:
    i = i+1
    if i == 3:
        break
    print(i)'''

'''name=" "
while name!="yash": #!=Not equal to
    name=input("Enter your Name")
print("Thanks for Entering a valid Name")'''

print('Available choices: \n1. Add \n2. Subtract \n3. Multiply \n4. Divide')
choice = int(input('Enter your choice: '))
res = "yes"
while res == 'yes':
    choice = int(input('Enter your choice: '))
    if choice == 1:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        result = num_1 + num_2
        print(f"Result: {result}")
        res = input('Do you want to continue(yes/no): ')
    elif choice == 2:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        result = num_1 - num_2
        print(f"Result: {result}")
        res = input('Do you want to continue(yes/no): ')
    elif choice == 3:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        result = num_1 * num_2
        print(f"Result: {result}")
        res = input('Do you want to continue(yes/no): ')
    elif choice == 4:
        num_1 = int(input("Enter first number: "))
        num_2 = int(input("Enter second number: "))
        result = num_1 // num_2
        print(f"Result: {result}")
        res = input('Do you want to continue(yes/no): ')
    else:
        print("Try again! Enter valid choice...")
        res = input('Do you want to continue(yes/no): ')

# PAIRS (DO THIS LATER)
mylist = [2,3,4,4,2,5,2,1,5,5,4,4]
