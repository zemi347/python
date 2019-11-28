# Queston 1: Make a calculator using Python with addition , subtraction , multiplication ,
# division and power.
first_number=input("Enter your Number : ")
second_number=input("Enter your Number : ")
operation=raw_input("Enter your operation : ")
result=0.00
if operation =="+":
    result=first_number + second_number
    print("Your Addition Result is ",result)
elif operation =="-":
    result=first_number - second_number
    print("Your subtraction Result is ",result)
elif operation =="*":
    result=first_number * second_number
    print("Your Multiplication Result is ",result)
elif operation =="/":
    result=first_number / second_number
    print("Your Division Result is ",result)
elif operation =="^":
    result=first_number ** second_number
    print("Your Power Result is ",result)
else: 
    print("your Opeation is Incorrect plz enter correct Opearation")
    print("Addition : +")
    print("subtraction : -")
    print("Multiplication : *")
    print("Division : /")
    print("Power : ^")