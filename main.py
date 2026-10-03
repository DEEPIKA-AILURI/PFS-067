file=open("PFS-67.txt", "r")
data=file.read()
print(data)
file.close()

#readline()-it reads only one line
file=open("PFS-67.txt","r")
data=file.readlines()
print(data)
file.close()

#writing a file
file=open("students.txt","w")
file.write("Deepika\n")
file.close()

#append mode
file=open("PFS-67.txt","a")
file.write("\nAmar")
file.close()

#Difference:
#w-replae exising content
#a-add to existing content

#with open()
with open("PFS-67.txt", "r") as file:
    data=file.read()
    print(data)


#writing using withopen
with open("PFS-67.txt","w") as file:
    file.write("Nani\n")

#Reading line by line
#strip-strip removes the extra new line
with open("PFS-67.txt", "r") as file:
    for line in file:
        print(line.strip())


try:
    with open("ABC.txt", "r") as file:
        data=file.read()
        print(data)
except FileNotFoundError:
    print("File does not exist")


#Real time example:Student Record
name=input("Enter student name:")
age=input("Enter age:")
course=input("Enter course:")
with open("PFS-67.txt", "a")as file:
    file.write(f"Name: {name}\n")
    file.write(f"Age: {age}\n")
    file.write(f"Course: {course}\n")
print("Student details saved successfully.")



balance=10000
#exception block starts
try:
    amount=int(input("Enter withdraw amount:"))
    if amount <= 0:
        raise ValueError("Amount must be positive")
    if amount > balance:
        print("Insufficient balance")
    else:
        balance -= amount
        with open("transactions.txt", "a")as file:
            file.write(f"Withdrawn:{amount}\n")
            file.write(f"Rem bal: {balance}\n")
        print("Success")
        print("Rem bal:", balance)
except ValueError as e:
    print("Error:",e)