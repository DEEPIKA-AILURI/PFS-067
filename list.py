deepika = [90,70,60,50,40]
print(deepika)

deepika[0] = 100
print(deepika)

#list can contain different data types
student = [10,"deepika","hyderabad",8.6]
print(student)

#adding elements
#append() - Add the elements
student.append(20)
print(student)

#extend() -to join two lists
a=[10, 20, 30]
b = [40, 50, 60]
a.extend(b)
print(a)
a.pop()
print(a)
a.remove(40)
print(a)
