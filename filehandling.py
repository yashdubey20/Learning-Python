# CREATING A FIE
'''f = open("myfile.txt","w")
print("Name of the File",f.name)
print("File Mode",f.mode)
print("Readable",f.readable())
print("Writeable", f.writable())
print("File has closed",f.closed)'''

# PERFORMING WRITE OPERATIONS
'''f = open("covid.txt","w")
f.write("Mumbai is fully Vacinated")
f.close()
print("File operation is done")'''
# "a"= append mode adds the data it wont be overwritten
'''f = open("covid.txt","a")
f.write("\n Mumbai is fully Vacinated")
f.close()
print("File operation is done")'''

'''f = open("covid.txt","a")
mylist =["Yash", "Valo"]
f.writelines(mylist)
float
f.close()
print("Written work has done successfully")'''

#Learn rest of Function on your own

# WITH STATEMENTS
'''with open("myfile.txt", "w") as f: #f is object
    f.write("Yash\n")
    f.write("Valo\n")
    f.write("OP\n")
    print("file closed: ",f.closed)
print("file closed: ",f.closed)'''

# OPERATION ON CSV FILE (csv file is lighter than excel file)
import csv
f = open("student.csv", "a",newline="")
a = csv.writer(f) # creating writer obj
#a.writerow(["student", "rollno", "classs", "number"])
student = "Yash"
rollno = int(input("Enter your rollno"))
classs = input("Enter your class")
number = 90909090
a.writerow([student,rollno,classs,number])
print("Student record is save")







