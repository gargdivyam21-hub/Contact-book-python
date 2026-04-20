contacts = {}
def add_contact():
    name = input("Enter name: ").strip()
    key = name.lower()

    if key in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone (10 digits): ").strip()

    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number! Must be 10 digits.")
        return

    contacts[key] = {"name": name, "phone": phone}
    print("Contact added successfully!!")


def view_contacts():
    if not contacts:
        print("No contacts found")
        return

    print("\n--- Contact List ---")
    for data in contacts.values():
        print(f"{data['name']} : {data['phone']}")


def search_contact():
    name = input("Enter name to search: ").strip().lower()

    if name in contacts:
        data = contacts[name]
        print(f"Found: {data['name']} : {data['phone']}")
    else:
        print("Contact not found")


def delete_contact():
    name = input("Enter name to delete: ").strip().lower()

    if name in contacts:
        del contacts[name]
        print("Deleted successfully")
    else:
        print("Contact not found")


while True:
    print("\n")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")