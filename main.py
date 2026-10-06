import json
import os

FILE_NAME = "contacts.json"


# Load contacts from JSON file
def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}


# Save contacts to JSON file
def save_contacts():
    with open(FILE_NAME, "w") as file:
        json.dump(contacts, file, indent=4)


contacts = load_contacts()


# Check whether phone number already exists
def phone_exists(phone, current_key=None):
    for key, data in contacts.items():
        if key != current_key and data["phone"] == phone:
            return True
    return False


# Add Contact
def add_contact():
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty!")
        return

    key = name.lower()

    if key in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone (10 digits): ").strip()

    if not phone.isdigit() or len(phone) != 10:
        print("Invalid phone number! Must be exactly 10 digits.")
        return

    if phone_exists(phone):
        print("This phone number already belongs to another contact!")
        return

    contacts[key] = {
        "name": name,
        "phone": phone
    }

    save_contacts()
    print("Contact added successfully!")


# View all contacts
def view_contacts():
    if not contacts:
        print("No contacts found.")
        return

    print("\n========== CONTACT LIST ==========")

    for data in contacts.values():
        print(f"Name  : {data['name']}")
        print(f"Phone : {data['phone']}")
        print("---------------------------------")


# Search Contact
def search_contact():
    search = input("Enter name to search: ").strip().lower()

    if not search:
        print("Search cannot be empty!")
        return

    found = False

    print("\n========== SEARCH RESULTS ==========")

    for data in contacts.values():
        if search in data["name"].lower():
            print(f"Name  : {data['name']}")
            print(f"Phone : {data['phone']}")
            print("---------------------------------")
            found = True

    if not found:
        print("Contact not found.")


# Update Contact
def update_contact():
    name = input("Enter contact name to update: ").strip().lower()

    if name not in contacts:
        print("Contact not found!")
        return

    print("\n1. Update Name")
    print("2. Update Phone")

    choice = input("Enter choice: ").strip()

    if choice == "1":
        new_name = input("Enter new name: ").strip()

        if not new_name:
            print("Name cannot be empty!")
            return

        new_key = new_name.lower()

        if new_key != name and new_key in contacts:
            print("A contact with this name already exists!")
            return

        contacts[new_key] = contacts.pop(name)
        contacts[new_key]["name"] = new_name

        save_contacts()
        print("Name updated successfully!")

    elif choice == "2":
        new_phone = input("Enter new phone (10 digits): ").strip()

        if not new_phone.isdigit() or len(new_phone) != 10:
            print("Invalid phone number!")
            return

        if phone_exists(new_phone, name):
            print("This phone number already belongs to another contact!")
            return

        contacts[name]["phone"] = new_phone

        save_contacts()
        print("Phone number updated successfully!")

    else:
        print("Invalid choice!")


# Delete Contact
def delete_contact():
    name = input("Enter contact name to delete: ").strip().lower()

    if name not in contacts:
        print("Contact not found!")
        return

    confirm = input(
        f"Are you sure you want to delete {contacts[name]['name']}? (y/n): "
    ).strip().lower()

    if confirm == "y":
        del contacts[name]
        save_contacts()
        print("Contact deleted successfully!")
    else:
        print("Delete cancelled.")


# Main Menu
def main():
    while True:
        print("\n========== CONTACT BOOK ==========")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        print("==================================")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_contact()

        elif choice == "2":
            view_contacts()

        elif choice == "3":
            search_contact()

        elif choice == "4":
            update_contact()

        elif choice == "5":
            delete_contact()

        elif choice == "6":
            print("Thank you for using Contact Book!")
            break

        else:
            print("Invalid choice! Please select 1-6.")


if __name__ == "__main__":
    main()