# SET DATATYPE
# Duplicate data not allowed {Represented by}
# myset = {"Yash", "Harshal", "Vishal", "Tejas", "Name1", 77, "Dubey", 60.22 } 
# print(myset)
# myset.add(90)
# print(myset)
# myset.update(range(1,10,2))
# myset.discard(3) #Value 3 is not present in the set
# print(myset)
#use remove func when u are 100% sure value is present
# myset.remove(3)
# print(myset)

# myset = {10,20,30,40}
# yorset = {"Yash", "Dubey"}
# newset = myset.union(yorset) #merge
# print(newset)

# myset = {10,20,30,40}
# yorset = {10,30,60}
# newset = myset.union(yorset) #merge
# print(newset)

# myset = {10,20,30,40}
# yorset = {10,30,60}
# print(myset.difference(yorset))

# FROZENSET
myset = {10,20,30,40}
fs = frozenset(myset) #Type cast
print(type(fs))
print(fs)


