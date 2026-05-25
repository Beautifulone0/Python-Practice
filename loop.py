# # # Write a Python program using a while loop that asks the user to enter a password continuously until they enter the correct password or run out of attempts. The correct password should be python123, and the user should only have 3 attempts. If the user enters the correct password, print "Access Granted". If the password is incorrect, print "Wrong Password" along with the number of attempts left. After 3 failed attempts, print "Account Locked"

# # password = "python123"
# # attempts = 3

# # while attempts > 0:
# #     prompt = input("enter a password: ")
# #     if prompt == password:
# #         print ("Access Granted")
# #         break
       
# #     else: 
# #         attempts -= 1
# #     if attempts > 0:
# #           print(f"Wrong Password {attempts} attempts left")
# #     else:
# #        print("Account Locked")

# # # 1. Number Guessing Game

# # # Write a Python program using a while loop that keeps asking the user to guess a secret number.
# # # The secret number is 7
# # # The user has only 5 attempts
# # # If the user guesses correctly, print: "Congratulations! You've guessed the secret number!"
# # # If the user guesses incorrectly, print: "Wrong guess. Try again." along with the number of attempts left. If the user runs out of attempts, print: "Game Over! The secret number was 7."

# # secret_no = 7
# # no_of_attempts = 5

# # while no_of_attempts > 0:
# #      user = int(input("Guess Secret Number: "))
# #      if user == secret_no:
# #         print("Congratulations! You've guessed the secret number!")
# #         break
# #      else:
# #         no_of_attempts -= 1
# #         if no_of_attempts > 0:
# #          print(f"Wrong guess. Try again. {no_of_attempts} attempts left")
# #         else:
# #          print("Game Over! The secret number was 7.")

# # #2. ATM PIN Checker

# # # Write a Python program using a while loop that asks the user to enter an ATM PIN.

# # # The correct PIN is 4321
# # # The user has 3 attempts
# # # If the PIN is correct, print: "Transaction Approved"
# # # If the PIN is incorrect, print: "Incorrect PIN. Try again." along with the number of attempts left. If the user runs out of attempts, print: "Card locked. Please contact your bank."

# # pin = 4321
# # trial = 3

# # while trial > 0:
# #   user = int(input("Enter Your ATM Pin: "))
# #   if user == pin:
# #     print("Transaction Approved")
# #     break
# #   else:
# #     trial -=1
# #     if trial > 1:
# #         print(f"Incorrect PIN. Try again. {trial} attempts left")
# #     else:
# #         print("Card locked. Please contact your bank.")


# # #3. Countdown Timer
# # # Write a Python program using a while loop that counts down from 10 to 1.
# # # After the loop finishes, print: "Liftoff!"


# # timer = 10

# # while timer > 0:
# #     print(timer)
# #     timer -= 1

# # print("Liftoff!")

# # # My main struggle areas right now are:
# # # input() and data types (str vs int)
# # # loop conditions
# # # updating variables inside loops
# # # indentation
# # # knowing when to use break

# # # Write a Python program using a while loop.

# # # Requirements:
# # # Correct username is "faith"
# # # Correct password is "python"
# # # User has 3 attempts
# # # Ask for both username and password
# # # If both are correct:
# # # Login Successful
# # # Otherwise:
# # # Invalid Details, and show attempts left, After 3 failed attempts: Account Suspended.

# # correct_user = "faith"
# # correct_password = "python"
# # trys = 3

# # while trys > 0:
# #     user_name = input("Enter username: ")
# #     user_password = input("Enter password: ")
# #     if user_name == correct_user and user_password == correct_password:
# #         print("Login Successful")
# #         break
# #     else:
# #         trys -= 1
# #         if trys > 0:
# #             print(f"Invalid Details, {trys} trys left")
# #         else:
# #             print("Account Suspended")

# # # 2. Number Counter

# # # Write a Python program that:
# # # Starts from 1
# # # Uses a while loop
# # # Prints numbers up to 10

# # counter = 1

# # while counter <= 10:
# #     print(counter)
# #     counter += 1

# # # 3. Even Numbers
# # # Write a Python program using a while loop that prints all even numbers from 2 to 20.

# # even = 2

# # while even <= 20:
# #     if even % 2 == 0:
# #         print(even)
# #         even += 1


# # # 4. Guess the Correct Age

# # # Write a Python program using a while loop.
# # # Requirements:
# # # Correct age is 25
# # # User has 4 attempts
# # # If the guess is correct:
# # # Correct Age!
# # # If incorrect: Wrong Age and show attempts left. After all attempts finish:No more attempts.

# # correct_age = 25
# # no_of_trial = 4 

# # while no_of_trial > 0:
# #     response = int(input("Enter correct age: "))
# #     if response == correct_age:
# #         print("Correct Age!")
# #         break
# #     else:
# #         no_of_trial -= 1
# #         if no_of_trial > 0:
# #             print(f"Wrong Age {no_of_trial} number of trial left")
# #         else:
# #             print("No more attempts")


# # # 5. Countdown Challenge

# # # Write a Python program that:
# # # Starts counting down from 15
# # # Stops at 1
# # # After the loop prints:
# # # Done!

# # countdown = 15

# # while countdown > 0:
# #     print(countdown)
# #     countdown -= 1
# # print("Done!")


# # # 6. Input Validation

# # # Write a Python program using a while loop that keeps asking the user to enter a number greater than 10.
# # # If the number is less than or equal to 10, print: Number too small, If the number is greater than 10, print: Valid Number and stop the loop.

# # greater_number = 1
# # while greater_number > 0:
# #     greater = int(input("Enter a number greater than 10: "))
# #     if greater <= 10:
# #         print(" Number too small")
# #     else:
# #         print("Valid Number ")
# #         break



# # # 7. PIN Retry System

# # # Write a Python program.
# # # Requirements: Correct PIN is 9090, User has 5 attempts If correct: Access Allowed If wrong: Wrong PIN Show attempts left each time. Use break correctly.

# # correct_pin = 9090
# # attempts = 5

# # while attempts > 0:
# #     user_input = int(input("Enter Pin"))
# #     if user_input == correct_pin:
# #         print("Access Allowed")
# #         break
# #     else:
# #         attempts -= 1
# #         if attempts > 0:
# #           print(f"Wrong Pin {attempts} attempts left.")
# #         else:
# #           print("Try again")


# # 1. Write a for loop that prints out the integers 2 through 10, each on a new line, using range().
# for number in range(2, 11):
#     print(number)
# # 2. Write a while loop that prints out the integers 2 through 10. (Hint: You’ll need to create a new integer first.)
# i = 2
# while i <= 10:
#     print(i)
#     i +=1

# 3. Write a function called doubles() that takes a number as its input and doubles it. Then use doubles() in a loop to double the number 2 three times, displaying each result on a separate line. Here’s some
# sample output:
# 4
# 8
# 16
# 154

def doubles (n):
    return n * 2

count = 0
number = 2

while count < 3:
    result= doubles(number)
    print(result)
    number = result
    count += 1