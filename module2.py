# First Method
'''import module1
module1.square(4)
module1.personal_info()
print(module1.pi)'''

# Second Method
'''import module1 as mod # Mod is shortcut of module1
mod.square(4)
mod.personal_info()
print(mod.pi)'''

#Importing Specfic Functions
'''from module1 import pi,square
print(pi)
square(4)'''

# To import all at once
from module1 import*
print(pi)
square(2)
welcome("Yash", "Dubey")
personal_info()



