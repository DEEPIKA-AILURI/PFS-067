a=10
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a//b)
print(a%b)
print(a**b)



a=5
a+=5
print(a)

a=5
a-=5
print(a)




a=5
a*=5
print(a)




a=5
a/=5
print(a)


a=5
b=5
print(a>=b)


#and
age=25
salary=50000
print(age >= 18 or salary >= 100000)


#not
x=False
print(not x)

#shopping
price=1000
quantity=3
total=price*quantity
if total >= 30000:
    discount = total * 0.10
else:
    discount=0
    final_price=total-discount
    print(final_price)