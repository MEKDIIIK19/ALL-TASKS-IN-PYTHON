
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

operation = input("Choose operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        print("Cannot divide by zero!")
        exit()
else:
    print("Invalid operation!")
    exit()

print("Score:", result)