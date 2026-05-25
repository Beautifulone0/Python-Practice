# 1. Write a function called cube() that takes one number parameter and returns the value of that number raised to the third power. Test the function by calling your cube() function on a few different numbers and displaying the results.
def cube ( n ):
    num = n ** 3
    return num 

print(cube(2))
print(cube(3))
print(cube(4))

# 2. Write a function called greet() that takes one string parameter called name and displays the text "Hello <name>!", where <name> is replaced by the value of the name parameter.
def greet (name, age):
    return f"Hello My name is {name} and I am {age} years old!"

print(greet("Faith", 30))
print(greet("Bob", 25))
print(greet("Charlie", 35))

print("\n if your function has the print() funtion inside it, you dont need another print() when calling it")

def greet (name):
    print(f"Hello {name}!")

greet("Alice")
greet("Bob")
greet("Charlie")

# 6.3 Challenge: Convert Temperatures
# Write a program called temperature.py that defines two functions:
# 1. convert_cel_to_far(), which takes one float parameter representing degrees Celsius and returns a float representing the same temperature in degrees Fahrenheit using the following formula:F = C * 9/5 + 32
# 2. convert_far_to_cel(), which takes one float parameter representing degrees Fahrenheit and returns a float representing the same temperature in degrees Celsius using the following formula: C = (F - 32) * 5/9
# The program should do the following:
# 1. Prompt the user to enter a temperature in degrees Fahrenheit andthen display the temperature converted to Celsius
# 2. Prompt the user to enter a temperature in degrees Celsius and thendisplay the temperature converted to Fahrenheit
# 3. Display all converted temperatures rounded to two decimal places
# Here’s a sample run of the program:
# Enter a temperature in degrees F: 72
# 72 degrees F = 22.22 degrees C
# Enter a temperature in degrees C: 37
# 37 degrees C = 98.60 degrees F

def convert_temperatures ():
    print("\n Celsius to Fahrenheit")
    c = float(input(f"enter a temperature in degree celsius: "))
    cel = c * 9/5 + 32
    print(f"{c} degrees Celsius = {round(cel, 2)} degrees Fahrenheit")

    print("\n Fahrenheit to Celsius")  
    f = float(input(f"enter a temperature in degree fahrenheit: "))
    far = (f - 32) * 5/9 
    print(f"{f} degrees Fahrenheit = {round(far, 2)} degrees Celsuis")
    

convert_temperatures()
