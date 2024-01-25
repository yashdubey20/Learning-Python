# Operator	Description	Example	Try it
# and 	Returns True if both statements are true	x < 5 and  x < 10	
# or	Returns True if one of the statements is true	x < 5 or x < 4	
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)

#LOGICAL AND
# a = int(input("Enter the First Paper "))
# b = int(input("Enter the Second Paper "))
# c = int(input("Enter the Third Paper "))
# d = int(input("Enter the Fourth Paper "))

# if a>=30 and b>=40 and c>=50 and d>=50:
#     print("You pass")
# else:
#     print("You Fail")

# total = a+b+c+d
# perc = total/5.0
# print("Your Total is= ",total)
# print("Your Percentage is= ", perc)

#LOGICAL OR
# ch = input("Enter any one char: ")
# if ch=='a' or ch=='A'or ch=='e'or ch=='E'or ch=='i'or ch=='I'or ch=='o'or ch=='O' or ch=='u' or ch=='U':
#     print("This is a Vowel")
# else:
#     print("This is a constant")

p1 = int(input("Enter Percentage "))
if p1>=40 and p1<60:
    print("Your Grade is C")
elif p1>=60 and p1<=80:
    print("Your Grade is B")
elif p1>=80 and p1<=100:
    print("Your Grade is A")
else:
    print("You Fail")
    
# DO ASCII VALUE 