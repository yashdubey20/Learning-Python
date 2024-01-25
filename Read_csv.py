'''import csv

print('Available choices: \n1. Insert data \n2. Read data \n3. Exit')
choice = int(input('Enter your choice: '))

res = 'yes'
while res == 'yes':
    if choice == 1:
        f = open("student.csv", "a", newline="")
        a = csv.writer(f)
        a.writerow(["id", "name", "rollno", "emailid", "total", "percent"])

        student_details = {'id': 0, 'name': '', 'rollno': '', 'emailid': '', 'total': 0, 'percent': 0}
        marks = []

        rec = int(input('Enter number of records: '))
        i = 0
        while i < rec:
            # student details
            student_details['id'] = int(input('Enter student ID: '))
            student_details['name'] = input('Enter student name: ')
            student_details['rollno'] = input('Enter student roll no.: ')
            student_details['emailid'] = input('Enter student email ID: ')

            # students marks
            for j in range(1, 6):
                marks.append(int(input(f'Enter marks for p{j} out of 100: ')))

            # total and percentage
            student_details['total'] = sum(marks)
            student_details['percent'] = (student_details['total'] * 100) / 500

            # inserting data in csv file
            a.writerow([student_details['id'], student_details['name'], student_details['rollno'], student_details['emailid'], student_details['total'], student_details['percent']])

            i += 1

        print('Data inserted successfully..')
        res = input('Do you want to continue(yes/no): ')
    elif choice == 2:
        f = open("student.csv", "r")
        r = csv.reader(f)
        for rec in r:
            print(rec)
        
        res = input('Do you want to continue(yes/no): ')
    else:
        print('Entered invalid choice.')
        res = input('Do you want to continue(yes/no): ')'''

# READING A BINARY FILE
f1 = open("yash1.jpeg","rb") # rb is reading binary
f2 = open("valo.jpeg", "wb") # wb is writing binary
data = f1.read()
f2.write(data)