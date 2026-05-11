#  1. Calculator Project
# Build a calculator program that supports the following operations:
# • Addition
# • Subtraction
# • Multiplication
# • Division
# Requirements:
# • The program must accept input from the user.
# • The calculator should correctly perform the selected operation.
# • Ensure the program works with decimal (float) numbers as well as whole numbers.
# • Handle possible errors such as division by zero

# Calculator Program
num1 = float(input("enter the first number: "))
num2 = float(input("enter the second number: "))
operation = input("do you want to:\n 1.add\n 2.subtract\n 3.multiply\n 4.divide\n")

if operation == "1":
    result = num1 + num2
    if result.is_integer():
        print("The result of addition is:", int(result))
    else:
        print("The result of addition is:", result)

elif operation == "2":
    result = num1 - num2
    if result.is_integer():
        print("The result of the subtraction is:", int(result))
    else:
        print("The result of the subtraction is:", result)
    

elif operation == "3":
    result = num1 * num2
    if result.is_integer():
       print("The result of multiplication is:", int(result))
    else:
        print("The result of multiplication is:", result)

elif operation == "4":
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2
        if result.is_integer():
            print("The result of division is:", int(result))
        else:
            print("The result of division is:", result)
else:
    print("Invalid operation selected. Please choose 1, 2, 3, or 4.")