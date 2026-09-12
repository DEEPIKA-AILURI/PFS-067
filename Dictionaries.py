student={"ID":1,"Name":"Deepu","course":"Python","place":"Hyderabad","cgpa":95.82
}
print(student["ID"])
print(student["Name"])
print(student["course"])
print(student["place"])
print(student["cgpa"])

# get in dictionary
student={"ID":1,"Name":"satya","course":"Python","place":"Hyderabad","cgpa":95.82
}
print(student["ID"])
print(student["Name"])
print(student["course"])
print(student["place"])
print(student["cgpa"])
print(student.get("salary"))

# Adding a new key
student["number"]="9182257721"
print(student["number"])
print(student)

#update a value
student["number"]="918225890"
print(student)
# i need to print only keys 
print(student.keys())

# items()
for key,value in student.items():
    print(key, value)

#update 
student.update({
    "Name"  : "Deepika",
    "Number" : "9185524"
})
student.pop("Number")
student.clear()
print(student)

#built in methods in dictionary
a={10,20,30,40}
print(len(a))
print(max(a))
print(min(a))
print(sorted(a))

student={"ID":1,"Name":"Deepu","course":"Python","place":"Hyderabad","cgpa":95.82
}
print(len(student))
