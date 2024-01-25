import csv
f = open("minip.csv", "a",newline="")
a = csv.writer(f)
a.writerow(["studentid", "name", "rollno", "emailid", "address", "mobileno", "p1","p2","p3","p4","p5","total","percentage","result"])
studentid = input("Enter your student id: ")
name = input("Enter your Name: ")
rollno = int(input("Enter your Rollno: "))
emailid = input("Enter your emailid: ")
address = input("Enter your address: ")
mobileno = int(input("Enter your mobileno: "))
p1 = int(input("Enter your p1: "))
p2 = int(input("Enter your p2: "))
p3 = int(input("Enter your p3: "))
p4 = int(input("Enter your p4: "))
p5 = int(input("Enter your p5: "))
total = p1+p2+p3+p4+p5
percentage = (total*100)/5.0
if p1>40 and p2>40 and p3>40 and p4>40 and p5>40:
    result = "pass"
    print("Record has been saved successfully")
else:
    result = "Fail"
    print("You Fail")

a.writerow([studentid, name,rollno,emailid,address,mobileno,p1,p2,p3,p4,p5,total,percentage,result])

# DO WITH LOOPS

'''import csv
f = open("minip.csv", "a",newline="")
a = csv.writer(f)
a.writerow(["studentid", "name", "rollno", "emailid", "address", "mobileno", "p1","p2","p3","p4","p5","total","percentage","result"])
rec = int(input("Enter the Number of Recors"))
for i in range(rec):
    studentid = input("Enter your student id: ")
    name = input("Enter your Name: ")
    rollno = int(input("Enter your Rollno: "))
    emailid = input("Enter your emailid: ")
    address = input("Enter your address: ")
    mobileno = int(input("Enter your mobileno: "))
    p1 = int(input("Enter your p1: "))
    p2 = int(input("Enter your p2: "))
    p3 = int(input("Enter your p3: "))
    p4 = int(input("Enter your p4: "))
    p5 = int(input("Enter your p5: "))
    total = p1+p2+p3+p4+p5
    percentage = (total*100)/500.0
if p1>40 and p2>40 and p3>40 and p4>40 and p5>40:
    result = "pass"
    print("Record has been saved successfully")
else:
    result = "Fail"
    print("You Fail")

a.writerow([studentid, name,rollno,emailid,address,mobileno,p1,p2,p3,p4,p5,total,percentage,result])

#DO REST AT HOME READ UPDATE DELETE'''

