# to do list
def assignment_tracker():
    """A simple student assignment tracker"""
    assignments = []

    while True:
        print("\n=== ASSIGNMENT TRACKER ===")
        print("1. View assignments")
        print("2. Add assignment")
        print("3. Remove assignment")
        print("4. Mark assignment as submitted")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if not assignments:
                print("No assignments yet!")
            else:
                print("\nYour Assignments:")
                for i, a in enumerate(assignments, 1):
                    status = "✅" if a["submitted"] else "❌"
                    print(f"{i}. [{status}] {a['title']} - Due: {a['due_date']}")

        elif choice == "2":
            title = input("Enter assignment title: ")
            due_date = input("Enter due date: ")
            assignments.append({"title": title, "due_date": due_date, "submitted": False})
            print(f"Added assignment: {title} (Due: {due_date})")

        elif choice == "3":
            if not assignments:
                print("No assignments to remove!")
                continue
            try:
                index = int(input("Enter assignment number to remove: ")) - 1
                if 0 <= index < len(assignments):
                    removed = assignments.pop(index)
                    print(f"Removed: {removed['title']}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "4":
            if not assignments:
                print("No assignments to mark!")
                continue
            try:
                index = int(input("Enter assignment number to mark as submitted: ")) - 1
                if 0 <= index < len(assignments):
                    assignments[index]["submitted"] = True
                    print(f"Marked as submitted: {assignments[index]['title']}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

        elif choice == "5":
            print("Good luck with your studies! 👋")
            break
        else:
            print("Invalid choice! Please enter 1-5.")

assignment_tracker()
