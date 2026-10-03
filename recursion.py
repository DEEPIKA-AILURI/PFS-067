#Lambda Functions

#Anonymous-Without name
#small anonymus functions
#Single line Functions

#Lamda syntax:
#lambda arguments : expression
def square(x):
    print(x*x)
square(5)

#Lambda:
#Lambda with one parameter
square=lambda x : x * x
print(square(6))

#Lambda with Multiple Parameters
add=lambda x,y,z:x+y+z
print(add(27,30,13))

#Lambda with if-else
check=lambda x: "Even" if x % 2 == 0 else "Odd"
print(check(7))
print(check(10))

#when should be use lambda?
#Small functions temporarily,especially with:
#map(),filter(),sorted(),reduce()
#map()-It applies function to every element
#example for map()
nums=[1,2,3,4,5]
squares=list(map(lambda x:x*x,nums))
print(squares)

#map without lambda
def square(x):
    return x * x
numbers=[1,2,3,4,5]
result=map(square,numbers)
print(list(result))


#Filter()-It is used when we want to select only elements that satisfy a condition
#Syntax:filter(function,iteration)
#only required data will be return
nums=[1,2,3,4,5,6]
result=filter(lambda x : x % 2 == 0,nums)
print(list(result))

#reduce()-It repeatedly applies a function to elements and reduces entire sequence to one final value.
#From functools import reduce(without using import they will not be worked)
from functools import reduce
numbers=[1,2,3,4]
result=reduce(lambda a,b:a*b,numbers)
print(result)

nums=[10,40,20,30]
result=sorted(nums)
print(result)

#names length will return small to big
names=["Deepika","Divya","kovidh","heman"]
result=sorted(names, key=len)
print(result)

#sorting numbers according to Absolute values
nums=[-10,-8,2,7,-13,21]
result=sorted(nums,key=abs)
print(result)

#Sorting words by last character
names=["Deepu","Divya","Krishna","Nani"]
result=sorted(names,key=lambda x: x[-1])
print(result)

#Sorting Tuple by marks
students = [
    ("r",85),
    ("D",88),
    ("S",34),
    ("K",90),
    ("P",77),
]
result=sorted(students,key=lambda x:x[-1])
print(result)


