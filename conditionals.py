# Python Conditional Statements - Advanced Assignments
# 1. Smart Security System: Create variables for has_keycard, knows_password, and is_admin. Allow access only if (has_keycard AND knows_password) OR is_admin is True.
has_keycard  = True
knows_password = False
is_admin = True

if (has_keycard and knows_password) or is_admin == True :
    print("Access Granted")
else:
    print("Access Denied")
print("\n")

# 2. Online Shopping Checker: A user can checkout only if they have items in cart AND payment is successful. If not, print appropriate messages explaining why checkout failed.
items_incart = True
payment_successful = True

if (items_incart and payment_successful) == True :
    print("Checkout Successful yayyyy!")
elif items_incart == True and payment_successful != True :
    print("Payment Unsuccessful so Checkout failed")
else:
    print("You have to have items in your cart to make payment and checkout")

print("\n")
# 3. Traffic Light Simulator: Create a variable light_color (red, yellow, green). Use if/elif/else to print what action a driver should take.
light_color = " "

if light_color == "red" :
    print("stop")
elif light_color == "yellow":
    print("get ready")
elif light_color == "green":
    print("go")
else:
    print("Thats not a traffic light color Be watchful and keep moving")
print("\n")

# 4. Exam Eligibility: A student can take an exam only if attendance is above 75% AND fees are paid. Otherwise, explain the reason.
attendance = 80
fees_paid = True
if attendance > 75 and fees_paid == True :
    print("You are eligible to take the exam")
else:
    print("You are not eligible to take the exam")

print("\n")

# 5. Weather Decision Maker: Use is_sunny, is_windy, and is_raining to decide if someone should go outside, stay home, or carry an umbrella. Combine multiple logical conditions.
is_sunny = True
is_windy = False
is_raining = False

if is_sunny and not is_windy and not is_raining:
    print("Go outside and enjoy the weather!")
elif is_raining:
    print("Carry an umbrella.")
else:
    print("Stay home.")