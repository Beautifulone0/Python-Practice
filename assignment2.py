# Cohort 2 Week 2 (Day 2) Assignment
# Solve the questions below. Focus on loops, conditions, lists, and strings.

# • 1. Create a list of 5 fruits and print only the ones that are NOT 'Apple'.
fruits = ["Apple", "Banana", "Orange", "Grapes", "Mango"]
for fruit in fruits:
    if fruit != "Apple":
        print(fruit)
print("\n\n")
# • 2. Loop through a list of drinks and print 'I love this drink!' when the item is 'Juice'.
drinks = ["Water", "Juice", "Soda", "Tea", "Coffee"]
for drink in drinks:
    if drink == "Juice":
        print("I love this drink!")
print("\n\n")
# • 3. Create a string with your favorite word and print each letter on a new line.
favourite_word = "Fufilled"
for letter in favourite_word:
    print(letter)
print("\n\n")
# • 4. Modify your loop so that it skips printing the letter 'e'.
for letter in favourite_word:
    if letter == "e":
        continue
    print(letter)
print("\n\n")
# • 5. Write a loop that prints numbers from 5 to 15.
for f in range(5, 16):
    print(f)
print("\n\n")
# • 6. Print only numbers divisible by 3 between 1 and 30.
for n in range(1, 31):
    if n % 3 == 0:
        print(n)
print("\n\n")
# • 7. Create a list of names and print only names longer than 4 characters.
names = ["Faith", "Jessica", "Bob", "Jane","Michael"]
for name in names:
    if len(name) > 4:
        print(name)
print("\n\n")
# • 8. Loop through a word and count how many times the letter 'o' appears.
word = "Woolly"
number_of_o = 0
for letter in word:
    if letter == "o":
        number_of_o += 1
print(f"The letter 'o' appears {number_of_o} times in the word '{word}'.")
print("\n\n")
# • 9. Write a loop that prints numbers from 10 down to 1.
for i in range(10, 0, -1):
    print(i)
print("\n\n")
# • 10. Create a list of 5 items and stop the loop completely when you reach the third item.
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
for i, item in enumerate(items):
    if i == 2:
        break
    print(item)

for x in range(1, 10, 34):
    print(x)