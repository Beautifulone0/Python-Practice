# Build a multiplication table generator (Week 3)
number = int(input("Enter a number to generate its multiplication table: "))
print(f"Multiplication Table for {number}:")
for i in range(1, 13):
    print(f"{number} x {i} = {number * i}")


number = int(input("Enter a number: "))

i = 1
while i <= 12:
    print(f"{number} x {i} = {number * i}")
    i += 1
