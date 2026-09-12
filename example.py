num = 969
sum = 0

while num > 0:
    digit = num % 10
    sum = sum + digit
    num = num // 10

print("Sum =", sum)

#MIN using with  while loop
num = 969
minimum = 9

while num > 0:
    digit = num % 10

    if digit < minimum:
        minimum = digit

    num = num // 10

print("Minimum =", minimum)

#max using with while loop

num = 969
maximum = 0

while num > 0:
    digit = num % 10

    if digit > maximum:
        maximum = digit

    num = num // 10

print("Maximum =", maximum)


#palindrome using while loop 
num = 969
original = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if original == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")



  