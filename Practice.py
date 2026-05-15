print("python practice")
question = "why did python3 practice.py not work?"
print(question)
print("\n")

question
greeting = "hello world"
greeting
text = "She said, \"What time is it?\""
print(text)
 

text
question2 = "why is it that when i call the variable without the print function it doesnt give an output?"
question2

# Practice Day 2
# The String Data Type
# 1. Print a string that uses double quotation marks inside the string.
double_quotation_string = "This is a double quotation string the second quotation begins with a backward Slash \"just like this and also end with a backward slash\""
print(double_quotation_string)
print("\n")
 
# 2. Print a string that uses an apostrophe inside the string.
apostrophe_in_a_string = "she's going on an errand"
print(apostrophe_in_a_string)
print("\n")
 
# 3. Print a string that spans multiple lines with whitespace preserved.
mutliple_lines_with_whitespace_preserved = "this is supposed to be a string with white space preserved\\ but i am confused if its the one with backlash\\ or triple double quotes lets watch and see"
print(mutliple_lines_with_whitespace_preserved)
print("\n")
 
# 4. Print a string that is coded on multiple lines but gets printed on a single line.
multiple_lines_but_gets_printed_on_a_single_line = """this isexpected to print on sa singlr line lets watch and see am going to keep practicing till i am perfect """
print(multiple_lines_but_gets_printed_on_a_single_line)
print("\n")
 
# Concatenation, Indexing, and Slicing
# 1. Create a string and print its length using len().
name = "Faith"
len(name)
print(len(name))
print("\n")
 
# 2. Create two strings, concatenate them, and print the resulting string.
fruit = "Apple"
food = "Pie"
fruit_food = fruit + food
print(fruit_food)
print("\n")
 
# 3. Create two strings, use concatenation to add a space between them, and print the result.
first_name = "Faith"
last_name = "Kalu Onyeani"
full_name = first_name + " " + last_name
print(full_name)
print("\n")
 
# 4. Print the string "zing" by using slice notation to specify the correct range of characters in the string "bazinga".
word = "bazinga"
print(word[2:6])
print("\n")
 
# Day 3
# 1. Write a program that converts the following strings to lowercase:"Animals", "Badger", "Honey Bee", "Honey Badger". Print each lowercase string on a separate line.
living_things = "Animals"
print(living_things.lower())
animal = "Badger"
print(animal.lower())
animal2 = "Honey Bee"
print(animal2.lower())
animal3 = "Honey Badger"
print(animal3.lower())
print("\n")
 
# 2. Repeat exercise 1, but convert each string to uppercase instead of lowercase.
print(living_things.upper())
print(animal.upper())
print(animal2.upper())
print(animal3.upper())
print("\n")
 
# 3. Write a program that removes whitespace from the following strings, then print out the strings with the whitespace removed:
# string1 = " Filet Mignon"
# string2 = "Brisket "
# string3 = " Cheeseburger "
string1 = " Filet Mignon"
print(string1.lstrip())
string2 = "Brisket "
print(string2.rstrip())
string3 = " Cheeseburger "
print(string3.strip())
print("\n")
 
# 4. Write a program that prints out the result of .startswith("be") on each of the following strings:
# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = " bEautiful"
string1 = "Becomes"
print(string1.startswith("be"))
string2 = "becomes"
print(string2.startswith("be"))
string3 = "BEAR"
print(string3.startswith("be"))
string4 = " bEautiful"
print(string4.startswith("be"))
print("\n")

# 5. Using the same four strings from exercise 4, write a program that uses string methods to alter each string so that .startswith("be") returns True for all of them
string1 = "Becomes"
print(string1.lower().startswith("be"))
string2 = "becomes"
print(string2.lower().startswith("be"))
string3 = "BEAR"
print(string3.lower().startswith("be"))
string4 = " bEautiful"
print(string4.lstrip().lower().startswith("be"))
print("\n")

# Output
# 1. Write a program that takes input from the user and displays that input back.
prompt = "How was your day?"
user_input = input(prompt)
print(user_input)
print("\n")
 
# 2. Write a program that takes input from the user and displays the input in lowercase.
prompt2 = "How old are you?"
response = input(prompt2)
print(response.lower())
print("\n")
 
# 3. Write a program that takes input from the user and displays the number of characters in the input.
prompt3 = "Do you love python?"
answer = input(prompt3)
print(len(answer))
print("\n")
 
# Challenge: Pick Apart Your User’s
# Input
# Write a program named first_letter.py that prompts the user for input with the string "Tell me your password:". The program should then determine the first letter of the user’s input, convert that letter to uppercase, and display it back.For example, if the user input is "no", then the program should displaythe following output: The first letter of your password is: N

prompt4 = input("Tell me your password:")
password = prompt4[0].upper()
print("The first letter of your password is:", password)
print("\n")
 

# 1. Create a string containing an integer, then convert that string into an actual integer object using int(). Test that your new object is a number by multiplying it by another number and displaying the result.
boys = "12"
convert = int(boys)
multiply = convert * 2
print (multiply)
print("\n")
# 2. Repeat the previous exercise, but use a floating-point number and float().
girls = "12.5"
convert = float(girls)
multiply = convert * 2
print(multiply)
print("\n")
# 3. Create a string object and an integer object, then display them side by side with a single print function call using str().
num_Of_Boys = boys
num_Of_Girls = girls
print(f"the number 0f boys {num_Of_Boys}, and number of girls {num_Of_Girls}")
print("\n")
# 4. Write a program that uses input() twice to get two numbers from the user, multiplies the numbers together, and displays the result. If the user enters 2 and 4, then your program should print the following text: The product of 2 and 4 is 8.0.
first_Num = input("what is you first num: ")
second_Num = input("what is your second num: ")
response = float(first_Num) * float(second_Num)
print(f"The product of {first_Num} and {second_Num} is {response}")
print("\n")
#Practice day 4
# Integers and Floating point numbers
# 1. Write a program that creates two variables, num1 and num2. Both num1 and num2 should be assigned the integer literal 25000000, one written with underscores and one without. Print num1 and num2 on two separate lines.
num1 = 25000000
num2 = 25_000_000
print(num1)
print(num2)
print("\n")
# 2. Write a program that assigns the floating-point literal 175000.0 to the variable num using E notation and then prints num in the interactive window.
num3 = 175e3
print(num3)
print("\n")
# 3. In IDLE’s interactive window, try to find the smallest exponent N for which 2e<N>, where <N> is replaced with your number, returns inf.
num4 =2e400
print(num4)
print("\n")
# Practice day 5
#round
num = 4.5
print(round(num))
num2= 5.432
print(round(num2, 2))