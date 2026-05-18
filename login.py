# Create a login simulation system (Week 2).
# Username and password for the simulation
correct_user = "faith"
correct_password = "python"
# Number of attempts allowed
trys = 3
# Loop to allow user to attempt login
while trys > 0:
    user_name = input("Enter username: ").lower()
    user_password = input("Enter password: ").lower()
    if user_name == correct_user and user_password == correct_password:
        print("Login Successful")
        break
    else:
        trys -= 1
        if trys > 0:
            print(f"Invalid Details, {trys} trys left")
        else:
            print("Account Suspended")