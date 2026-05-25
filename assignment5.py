# Python Practice: Functions (No Parameters)
# Instructions: Create functions without parameters for each task below. Each function should perform the task and print the result.
# 1 Write a function that prints 'Hello, World!'
print("\n print hello world")
def greet ():
    print("Hello, World!")
greet()

print("\n print my name")
# 2 Write a function that prints your name.
def my_name ():
    n = "Faith Kalu Onyeani"
    print(f"My Name Is {n}")
my_name()

print("\n prints number from 1 to 10")
# 3 Write a function that prints numbers from 1 to 10.
def numbers ():
   for x in range(1, 11):
    print(x)
numbers()

print("\n even numbers from 1 to 20")
# 4 Write a function that prints all even numbers from 1 to 20.
def even ():
    for x in range(1, 21):
        if x % 2 == 0:
         print(x)
even()

print("\n multiplication table of 5")
# 5 Write a function that prints the multiplication table of 5.
def multiply ():
    m = 5
    for x in range(1, 13):
        print(f"{m} x {x} = {m * x}")
multiply()

print("\n sum of numbers from 1 to 50")
# 6 Write a function that prints the sum of numbers from 1 to 50.
def adds ():
    print(sum(range(1, 51)))
adds()

print("\n even or odd numbers")
# 7 Write a function that prints whether a number (hardcoded inside the function) is even or odd.
def even_odd ():
    e_o = 7
    if e_o % 2 == 0:
        print(f"{e_o} is an even number")
    else:
        print(f"{e_o} is an odd number")
even_odd()

print("\n simple pattern of stars")
# 8 Write a function that prints a simple pattern of stars (*).
def stars():
    for row in range(3):
        for star in range(3):
            print("*", end=" ")
        print()

stars()

print(f"\n Current Year")
from datetime import datetime
# 9 Write a function that prints the current year.
def current_year ():
    year = datetime.now().year
    print(f"the current year: {year}")
current_year()

print("\n Squares of numbers from 1 to 10:")
# 10 Write a function that prints the square of numbers from 1 to 10.
def square_numbers ():
    for n in range(1, 11):
        print(n ** 2)
square_numbers()