'''A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
Ask user for their salary and year of service and print the net bonus amount.'''
# salary = int(input("Enter the Salary of the Employee: "))
# year = int(input("Enter the number of years"))
# Bonus = (salary*5)/100
# if year>=5:
#     print("Your Salary is increased by 5%: ", Bonus + salary)
# else:
#     print("Your Salary remains the same: ",salary)

'''Take values of length and breadth of a rectangle from user and check if it is square or not.'''
# lenght = int(input("Enter The Lenght of the Rectangle: "))
# breadth = int(input("Enter The Breadth of the Retangle: "))
# if lenght==breadth:
#     print("The Given Figure is a Square")
# else:
#     print("The Given Figure is a Rectangle")

'''Take two int values from user and print greatest among them.'''

# a = int(input("Enter the Value of A: "))
# b = int(input("Enter the Value of B: ")) 
# if a>b:
#     print("A is Greater than B")
# else:
#     print("B is Greater than A")

'''A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
Ask user for quantity
Suppose, one unit will cost 100.
Judge and print total cost for user
'''

# quanity = int(input("Enter the Quantity: "))
# unit = 100
# Mrp = quanity*unit
# discount = (Mrp*10)/100
# if Mrp>=1000:
#     print("Your Discounted MRP is: ",Mrp-discount)
# else:
#     print("Your Total MRP is: ",Mrp)

'''A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 45 to 50 - D
d. 50 to 60 - C
e. 60 to 80 - B
f. Above 80 - A'''

# Marks = int(input("Enter the Marks: "))
# if Marks<=25:
#     print("Your Grade is F")
# elif Marks>= 25 and Marks<45:
#     print("Your Grade is E")
# elif Marks>= 45 and Marks<50:
#     print("Your Grade is D")
# elif Marks>= 50 and Marks<60:
#     print("Your Grade is C")
# elif Marks>= 60 and Marks<80:
#     print("Your Grade is B")
# elif Marks>= 80 and Marks<100:
#     print("Your Grade is A")

'''Take input of age of 3 people by user and determine oldest and youngest among them.'''

# person1 = int(input("Enter the Age of The 1st Person: "))
# person2 = int(input("Enter the Age of The 2nd Person: "))
# person3 = int(input("Enter the Age of The 3rd Person: "))
# if person1>person2 and person1>person3:
#     print("Person 1 is the Oldest")
# elif person2>person1 and person2>person3:
#     print("Person 2 is the Oldest")
# elif person3>person2 and person3>person1:
#     print("Person 3 is the Oldest")

# if person1<person2 and person1<person3:
#     print("Person 1 is the Youngest")
# elif person2<person1 and person2<person3:
#     print("Person 2 is the Youngest")
# elif person3<person2 and person3<person1:
#     print("Person 3 is the Youngest")
# else:
#     print("All are Equal")

'''Write a program to print absolute value of a number entered by user. E.g.-
	INPUT: 1        OUTPUT: 1	
	INPUT: -1        OUTPUT: 1'''

# number = int(input("Enter the Number: "))
# if number<0:
#     print(number*-1)
# else:
#     print(number)

'''A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held			-		7856
Number of classes attended.		-		856			80%
And print
percentage of class attended
Is student is allowed to sit in exam or not'''

# class_held = int(input("Number of class held: "))
# class_attented = int(input("Number of class attented: "))
# Percentage = (class_attented/class_held)*100
# if Percentage >= 75:
#     print("Student is allowed to sit in the Exam")
# else:
#     print("Student is not allowed to sit in the Exam")

'''Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria : 
Unit Price First 100 units 3.5 rs  per unit
Next 100 units Rs 5 per unit 
After 200 units Rs 10 per unit 


1000<   meter charge= costing 10%
		tax = costing 9%

1000>   meter charge= costing 20%
		tax = costing 18%'''

# unit = int(input("Enter the Number of Units: "))
# meterc1 = unit/10
# taxc1 = (unit*9)/100
# meterc2 = (unit*20)/100
# taxc2 = (unit*18)/100
# if unit>0 and unit<100:
#     print("Total Electricity Bill: ",unit*3.5)
# elif unit>= 100 and unit<200:
#     print("Your Electricity Bill is: ",unit*5)
# elif unit>=200:
#     print("Your Electricity Bill is: ",unit*10)

# if unit<1000:
#     print("The Final Bill After Taxes is: ",unit+meterc1+taxc1)
# elif unit>1000:
#     print("The Final Bill After Tax is: ", unit+meterc2+taxc2)

'''Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria: 
Cost price (in Rs) 			Tax 
100000 				15 % 
> 50000 and <= 100000 		10% 
<= 50000 			5% '''

# bikec = int(input("Enter The Price of The Bike: "))
# tax1 = (bikec*5)/100.0
# tax2 = (bikec*10)/100.0
# tax3 = (bikec*15)/100.0

# if bikec<=50000:
#     print("Your Total Bike Cost is: ",tax1+bikec)
# elif bikec>50000 and bikec<=100000:
#     print("Your Total Bike Cost: ",tax2+bikec)
# elif bikec>100000:
#     print("Your Total Bike Cost: ",tax3+bikec)




