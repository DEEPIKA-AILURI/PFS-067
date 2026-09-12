card_number = 12
correct_pin = 1234
balance = 5000

card = int(input("Enter card number: "))
pin = int(input("Enter PIN: "))
amount = int(input("Enter withdrawal amount: "))

if card != card_number:
    print("Invalid card")

elif pin != correct_pin:
    print("Wrong PIN")

elif amount > balance:
    print("Insufficient balance")

else:
    balance = balance - amount
    print("Withdrawal successful")
    print("Remaining balance:", balance)