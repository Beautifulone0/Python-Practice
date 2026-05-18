# Create a contact manager with dictionary (Week 4).
contacts = {}
no_of_contacts = 10

while True:
    print("\n Welcome to the Contact Manager!")
    print("\n You can add, view, and delete contacts.")
    print("\n Lets get started!")
    print("\n 1. Add a Contact")
    print("\n 2. View Contacts")
    print("\n 3. Delete a Contact")
    print("\n 4. Return to Main Menu")
    print("\n 5. Exit")

    choice = int(input("\n Enter One of the options above: "))
    if choice == 1:
        if no_of_contacts == 0:
            print("\nYou can only add 10 contacts. Delete some first.")
        else:
            name = input("\n Enter Contact Name: ")
            phone = input("\n Enter Contact Phone Number: ")
            contacts[name] = phone
            no_of_contacts -= 1
            print(f"\n Contact {name} added Successfully! You can add {no_of_contacts} more contacts.")
        if no_of_contacts == 0:
           print("You have now reached the maximum number of contacts.")
        else:
           print(f"You can add {no_of_contacts} more contacts.")
    elif choice == 2:
        print("\n Your contacts:")
        for name in contacts:
            print(f"{name}: {contacts[name]}")
    elif choice == 3:
        name = input("\n Enter the name of the contact you want to delete: ")
        if name in contacts:
            del contacts[name]
            no_of_contacts += 1
            print(f"\n Contact {name} deleted successfully! You can add {no_of_contacts} more contacts.")
    elif choice == 4:
        print("\n Returning to Main Menu....")
    elif choice == 5:
        print("\n Exiting Contact Manager. Goodbye!")
        break
    else:
        print("\n Invalid option. Please try again.")
       
