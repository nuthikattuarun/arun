

def show_menu():
    print("\nContact Book Menu")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")


def add_contact(contacts):
    name = input("Enter contact name: ").strip()
    if name in contacts:
        print("Contact already exists.")
    else:
        number = input("Enter phone number: ").strip()
        contacts[name] = number
        print("Contact added.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts to show.")
    else:
        print("\nYour Contacts:")
        for name in sorted(contacts):
            print(f"{name.title()}: {contacts[name]}")


def edit_contact(contacts):
    name = input("Enter contact name to edit: ").strip()
    if name in contacts:
        print(f"Current number: {contacts[name]}")
        new_number = input("Enter new number: ").strip()
        contacts[name] = new_number
        print("Contact updated.")
    else:
        print("Contact not found.")


def delete_contact(contacts):
    name = input("Enter contact name to delete: ").strip()
    if name in contacts:
        confirm = input(f"Are you sure you want to delete {name}? (y/n): ").lower()
        if confirm == 'y':
            del contacts[name]
            print("Contact deleted.")
        else:
            print("Deletion cancelled.")
    else:
        print("Contact not found.")



def main():
    contacts = {}
    while True:
        show_menu()
        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Goodbye.")
            break
        else:
            print("Invalid choice. Please choose between 1–6.")



main()
