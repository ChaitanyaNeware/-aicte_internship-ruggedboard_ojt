class Student:
    def getStudentDetails(self):
        self.name = input("Enter Name : ")
        self.history =int(input("Enter History Marks : "))
        self.science = int(input("Enter Science Marks : "))
        self.maths = int(input("Enter Maths Marks : "))

    def printResult(self):
        self.percentage = (int)( (self.history + self.science + self.maths) / 300 * 100 ); 
        print(self.percentage)

S1=Student()
S1.getStudentDetails()

print("Result : ")
S1.printResult()

