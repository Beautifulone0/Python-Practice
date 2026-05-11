# 1.Percentage App
# Create a program that calculates the percentage of a number.
# Requirements:
# • The program should ask the user to input a number.
# • The program should ask the user to input a percentage value.
# • The program should calculate and display the percentage of the given number.
# • Ensure the program works with decimal (float) values.

num1 = float(input("Enter a number : "))
num2 = float(input("Enter a percentage value :"))

answer = (num2 / 100) * num1
if answer.is_integer() :
    print("The percentage is :", int(answer))
else:
    print("The percentage is :", answer)