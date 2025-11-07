
print("Welcome to Contact Saver!")

while True:
    print("\n1. Add new contact")
    print("2. View all contacts")
    print("3. Exit")
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        with open("contacts.txt", "a") as file:
            file.write(f"{name} - {phone}\n")
        print("✅ Contact saved!")

    elif choice == "2":
        print("\n📋 Your Contacts:")
        try:
            with open("contacts.txt", "r") as file:
                content = file.read()
                if content.strip() == "":
                    print("(No contacts found)")
                else:
                    print(content)
        except FileNotFoundError:
            print("(No contacts saved yet!)")

    elif choice == "3":
        print("Goodbye! Your contacts are saved in contacts.txt ")
        break

    else:
        print("Invalid choice! Please enter 1-3.")
