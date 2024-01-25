# 2.TUPLE
# *WHAT IS DIFF BETWEEN LIST & TUPLE*
# mytuple = ("Yash", "Harshal", "Vishal", "Tejas", "Name1", 77, "Dubey", 60.22 ) 
# print(mytuple)
# print(type(mytuple))
# mytuple[2] = "Yash"
# print(mytuple)

# SET DATATYPE
# Duplicate data not allowed {Represented by}
myset = {"Yash", "Harshal", "Vishal", "Tejas", "Name1", 77, "Dubey", 60.22 } 
print(myset)
myset.add(90)
print(myset)
myset.update(range(1,10,2))
myset.discard(3) #Value 3 is not present in the set
print(myset)
#use remove func when u are 100% sure value is present
myset.remove(3)
print(myset)
