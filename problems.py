#identify a number whether it is positive or negative or zero
num=int(input("Enter number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

#2.even or odd
num=int(input("Enter number: "))
if num % 2 == 0:
    print("Even")
elif num % 2 != 0:
    print("Odd")
else:
    print("Zero")

#3.largest of two numbers
a=int(input("enter first number:"))
b=int(input("enter second number:"))
if a > b:
    print("First number is larger")
elif a < b:
    print("Second number is larger")
else:
    print("Both are equal")


#college admission
marks=int(input("enter marks:"))
entrance = input("Did you pass entrance exam? (yes,no)")
if marks >= 60 and entrance == "yes":
    print("Eligible for admission")
else:print("Not Eligible")


#login system(error)
# Login system
username = input("Enter username: ")
password = input("Enter password: ")

if username == "admin" and password == "admin":
    print("Login Successful")
else:
    print("Login not successful")



#Driving Eligibiliy 
age=int(input("Enter your age:"))
license=input("Do you have license? (yes,no): ")
if license=="yes":
    print("You can drive")
else:
    print("License is required")

#movie ticket pricing
age =int(input("enter age"))
if(age<5):
    print("free ticket")
elif(age>=5 and age<=12):
    print("100 rupees")
elif(age>=13 and age<=59):
    print("200 rupees")
elif(age>=60):
    print("120 ")

#leap year 
year = int(input("Enter a year: "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("Not a Leap Year")
    else:
        print("Leap Year")
else:
    print("Not a Leap Year")


#employee management system
#performance > 90 and exp > 5 = 20% hike
#performance > 90 and exp < 5 = 10% hike
#performance > 80  = 10% hike
#performance > 70 = 5%hike
performance=int(input("enter a performance"))
experience=int(input("enter a experience"))
if performance > 90 and exp > 5:
    print("20% hike")
elif performance > 90 and exp < 5:
    print("10% hike")
elif performance > 80:
    print("10% hike")
elif performance > 70:
    print("5% hike")
else:
    print("Zero")