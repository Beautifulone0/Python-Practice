# Week 3 [Day 1] Assignment
# Instructions: Solve the following questions using for loops and nested for loops. Think carefully about logic and conditions.
# • 1. Create a list of 6 random numbers. Using a for loop with range(len()), print each number with its index. Then print only numbers greater than 10.
rand_Num = [2, 5, 8, 11, 14, 15]
for f in range(len(rand_Num)):
  print(f, rand_Num[f])

print("\nNumbers greater than 10:")
for f in rand_Num:
  if f > 10:
    print(f)
# • 2. Using range(), generate numbers from 1 to 50. Print only numbers that are divisible by 4 but NOT divisible by 8.

print("\nNumbers from 1 to 50 that are divisible by 4 but NOT divisible by 8:")
for num in range(1, 51):
 if num % 4 == 0 and num % 8 != 0 :
   print(num)

# • 3. Given two lists: colors = ['blue', 'green', 'yellow'] and objects = ['car', 'house', 'shirt'], use a nested loop to combine them. Skip any combination where the color is 'green'.
colors = ['blue', 'green', 'yellow']
objects = ['car', 'house', 'shirt']

print("\nCombinations of colors and objects (excluding 'green'):")
for c in colors:
    for o in objects:
        if c == "green":
            continue
        print(c, o)
# • 4. Using nested loops, print a pattern of stars (*) in a square shape of size 5x5. Then modify it to print only the diagonal stars.
print("\nSquare pattern of stars:")
for stars in range(5):
    for star in range(5):
        print("*", end=" ")
    print()
print("\nDiagonal pattern of stars:")
for diagonal in range(5):
  for stars in range(5):
    if diagonal == stars:
      print("*", end=" ")
    else:      
      print(" ", end=" ")
  print()
# • 5. Given two lists: scores1 = [10, 20, 30] and scores2 = [5, 15, 25], use nested loops to print the sum of each pair. Then print only sums that are greater than 30
scores1 = [10, 20, 30]
scores2 = [5, 15, 25]

for s in  range(len(scores1)):
  for f in range(len(scores2)):
    sum = scores1[s] + scores2[f]
    print(f"the sum of {scores1[s]} and {scores2[f]} = {sum}")
print("\nSums greater than 30:")
for s in  range(len(scores1)):
  for f in range(len(scores2)):
    sum = scores1[s] + scores2[f]
    if sum > 30:
      print(f"the sum of {scores1[s]} and {scores2[f]} = {sum} ")