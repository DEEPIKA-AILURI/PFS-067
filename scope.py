#Scope:scope is the region of a program where a variable can be accessed.
# 1)Local scope
# 2)Global scope
#1)Local scope-A variable created inside a function called as local scope.
#local scope
# def display():
#     name="Deepika"
#     age=22
#     print(name)
#     print(age)
# display()

#Diff functions can have variables with same name
# def first():
#     x=20
#     print(x)
# first()

# def second():
#     x=30
#     print(x)
# second()


#global scope-variables declared outside the function has global scope
#better to use global scope only
# name="Deepika"
# age=22
# def display():
#     name="Divya"
#     print(name)
#     print(age)
# display()
# print(name)

# x=100
# def display():
#     global x
#     x=200
# display()
# print(x)

#Pass by Value and Pass by Reference
# def display(x):
#     x=20
# a=10
# display(a)
# print(a)#10

# pass by value:A copy of the value is passed to the function ,changes made inside the  function do not affect the original value.
# def change(x):
#     x=20
#     print("Inside func:",x)
# a=10
# change(a)
# print("Outside func:",a)
# #explanation:a->10
# calling the function change(a)
# x receives a reference to the same integer
# object
# x=20
#before:a value is 10
#after x value is 20
#a=10,x=20
# def add_10(x):
#     x+=10
#     print("Inside func:",x)
# nums=50#1
# add_10(nums)#2 calling function
# print("Outside func:",nums)

#pass by reference
# def add_element(data):
#     data.append(40)
# values=[10,20,30]
# add_element(values)
# print(values)

#Recursion:Function calling itself 
# for i in range(5,0,-1):
#     print

# def count_down(n):
#     #Base case
#     if n==0:
#         return
#     #recursive case
#     print(n)
#     count_down(n-1)
# count_down(5)

#Factorial of a number using recursion
def fact(n):
    #base case
    if n<=1:
        return 1
    #recursive case
    return n*fact(n-1)
print(fact(5))

#fibnocci series
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(5))
