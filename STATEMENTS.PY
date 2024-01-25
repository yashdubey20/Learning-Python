# # BREAK LOOPING LEVEL (Ruk ke aage badh jayega)
# for i in range(1,10):
#     if i==5:
#         break
#     print(i)

# name = input("Enter your Name: ")
# i=0
# for x in name:
#     if x=='n':
#         print("The charchter present at index no", i, "value=: p",x)
#     break
# i=i+1

# for i in range(1,10):
#     if i==5:
#         continue #(Chodh ke aage badh jayega)
#     print(i)

# mycart=[10,20,200,300,800,60,700]
# for i in mycart:
#     if i>400:
#         print("This my purchased cart")
#     continue
# print(i)

# j=6
# for i in range(1,6):
#     print(i*1," ", j-i)

for i,j in zip(range(1,6),range(5,0,-1)): #zip use for multiple variable
    if i==3 and j==3:
        continue
    print(i," ",j)

    
    