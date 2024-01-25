choice = 0
class Exam(object):
    def __init__(self):
        self.sname=None
        self.collegename = 0
        self.classname = 0
        self.rollno = 0
        self.login()
    def login(self):
        print("===========================")
        
        username = input("Enter Your Username: ")
        password = input("Enter Your Password: ")

        print("===========================")
        print()

        if username == password:
            print("Login Successfully")
        else:
            print("Login Failed")

    print()
    def getdata(self):
        self.sname = input("Enter Your Name: ")
        self.collegename = input("Enter Your College Name: ")
        self.classname = input("Enter Your Class Name: ")
        self.rollno = input("Enter Your Rollno: ")
        print()
        print("Choose any branch for giving Exam")
        print("1. Mechanical Engeerning")
        print("2. Information Technology")
        print("3. Computer Science")
        print("4. Civil Engeerning")
        print()
        choice = int(input("Enter Your Choice: "))
        if choice ==1:
            self.mechanical()
        elif choice==2:
            pass
        elif choice==3:
            pass
        elif choice==4:
            pass
        else:
            print("You have entered the wrong choice")
        
    def mechanical(self):
        print("1. First Semster")
        print("2. Second Semster")
        print("Enter Your Semster Number: ")

        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            print("Math")
        elif choice==2:
            pass 
        
    def information(self):
        print("1. First Semster")
        print("2. Second Semster")
        choice = int(input("Enter Your Choice"))
        if choice == 1:
            pass
        elif choice==2:
            pass
    
    def computer(self):
        print("1. First Semster")
        print("2. Second Semster")
        choice = int(input("Enter Your Choice"))
        if choice == 1:
            pass
        elif choice==2:
            pass
    
    def civil(self):
        print("1. First Semster")
        print("2. Second Semster")
        choice = int(input("Enter Your Choice"))
        if choice == 1:
            pass
        elif choice==2:
            pass
    
obj = Exam()
obj.login()
obj.getdata()

class Calculation(object):
    def __init__(self):
        self.stat=0
        self.dmgt=0
        self.cg=0
        self.toc=0
        self.math=0
        self.total=0
        self.percentage=0
        self.ps = 0
        print()
        print("Do You Want to Put Examination Marks Enter Yes/No: ")
        print()
        Yes = input("Enter Yes/No: ")
        if Yes== "yes":
            self.calculatemarks()
        else:
            print("Thank you for Visting Here")
        print()

    def calculatemarks(self):
        self.stat = int(input("Enter Marks Of Statistics: "))
        self.dmgt = int(input("Enter Marks Of DMGT: "))
        self.cg = int(input("Enter Marks Of CG: "))
        self.toc = int(input("Enter Marks Of Toc: "))
        self.math = int(input("Enter Marks Of Maths: "))
        print()

        if self.stat>= 40 and self.dmgt>=40 and self.cg>=40 and self.toc>=40 and self.math>=40:
            self.ps = "pass"
            print("You Pass")
        else:
            self.ps = "Fail"
            print("You Fail")

        self.total = self.stat+self.dmgt+self.cg+self.toc+self.math
        self.percentage = self.total/5.0

obj1 = Calculation()

class Assessment(Exam,Calculation):
    def __init__(self):
        Exam.__init__(self)
        Calculation.__init__(self)

    def result(self):
        print("==========================================================")
        print("                                                          ")
        print("            College Name: ",self.collegename,"             ")

        print("|           Student Name: ",self.sname,"                  |")
        print("|           ROLL NO      : ",self.rollno,"                |")
        print("==========================================================")
        print("                                                          ")
        print(" Subject Name   :     Total  Marks   :  Obtained Marks   :")
        print(" Statistic      : ",  "    100       :" ,self.stat)
        print(" DMGT           : ",  "    100       :" ,self.dmgt)
        print(" CG             : ",  "    100       :" ,self.cg)
        print(" TOC            : ",  "    100       :" ,self.toc)
        print(" Maths          : ",  "    100       :" ,self.math)
        print("==========================================================")
        print("                                                          ")
        print("Result Status   :",                      self.ps,"        " )
        print("Total Marks     :",       "500",         self.ps,"         ")
        print("Obtained Marks  :",                      self.total,"      ")
        print("Percentage      :",     self.percentage,    "              ")
        print("===========================================================")

obj2 = Assessment()
obj2.result()



