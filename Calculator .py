#Calculator
greet = "Hello! Welcome to Python Calculator"
func = "We can do Add, Subtract, Multiple, Divide:"
print(greet)
print(func)

#Inputs
num1  = int(input("Enter the First Number:"))
num2  = int(input("Enter Second Number:"))
operation = input("Enter which operation you want: +,-,*,/: ")

#perform calculation
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == "/":
    if num2 == 0:
        print("cant divide by zero")
    else:
        result = num1 / num2
    print(f"{num1} / {num2} = {result}")

else:
    print("Invalid operations! Please choose  one of them:  +, -, *, /")




