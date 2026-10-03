# Oop-Object Oriented Programming.
#It is a programming approach where we organize our program around objects rather than only functions and variables.
# Student:
# Data:-(name,age,roll no)
# Behaviour:-(study(),attend_classes(),write_exam(),display())
# in oops we combine data + behaviour into object.
# class-blueprint of an object
#There is no memory allocation.
# object-instances of class (or) actual thing created from bleprint.
#There is a memory allocation.
# class Student:
#     pass
# student1 = Student() #student1 ->object
# student1.name = "Deepu"
# student1.age = 22
# student1.marks = 99
# print(student1.name)
# print(student1.age)
# print(student1.marks)
#attributes are the data/properties associated with an objects
# class Student:
#     def study(self):
#         print("Student is Studying")

# class Student:
#     def study(self):
#         print("Student is studying")


# Student1 = Student()
# Student1.study()

#Constructor-it is a special method that is used automatically called when an object is created.
#__init__
# class Student:
#     def _init_(self):
#         print("Student is studying")
# student1=Student()

#constructor with attributes
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print(self.name,self.age,self.marks)
Student1=Student("Deepika",22,95)
print(Student1.name)
print(Student1.age)
print(Student1.marks)
#self represents current object.

class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def display(self):
        print(self.name,self.age,self.marks)
Student1=Student("Deepika",22,95)
Student1.display()

#Encapsulation
#Encapsulation means bundling data and methods together inside a class and controlling how that data is accessed or modified.
class BankAccount:
    def __init__(self,balance):
        self.balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self,amount):
        self.balance -= amount
    def get_balance(self):
        return self.balance
ba=BankAccount(50000)
ba.deposit(10000)
ba.withdraw(5000)
print(ba.get_balance())
#Double underscore indicates a private-like attribute in python through name managing.
#Getter and Setter Concept
#private data
#Getter->read data
#Setter->modify data safely
class Student:
    def __init__(self,marks):
        self.__marks=marks
    def get_marks(self):
        return self.__marks
    def set_marks(self,marks):
        if 0 <= marks <=100:
            self.__marks = marks
        else:
            print("Invalid marks")
student = Student(80)
print(student.get_marks())
student.set_marks(90)
print(student.get_marks())