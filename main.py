
import json
import os

FILE_NAME = "contacts.json"


def load_contacts():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            print("Could not read the contacts file.")
            return []
    return []


def save_contacts(contacts):
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    print("\n--- Add Contact ---")

    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    if not name or not phone:
        print("Name and phone number are required.")
        return

    for contact in contacts:
        if contact["phone"] == phone:
            print("This phone number already exists.")
            return

    contact = {
        "name": name,
        "phone": phone,
        "email": email
    }

    contacts.append(contact)
    save_contacts(contacts)

    print("Contact added successfully!")


def view_contacts(contacts):
    print("\n--- All Contacts ---")

    if not contacts:
        print("No contacts found.")
        return

    for number, contact in enumerate(contacts, start=1):
        print(f"\nContact {number}")
        print(f"Name : {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")


def search_contact(contacts):
    print("\n--- Search Contact ---")

    search_name = input("Enter name to search: ").strip().lower()

    found = False

    for contact in contacts:
        if search_name in contact["name"].lower():
            print(f"\nName : {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            found = True

    if not found:
        print("Contact not found.")


def update_contact(contacts):
    print("\n--- Update Contact ---")

    phone = input("Enter the current phone number: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            new_name = input(
                f"Enter new name [{contact['name']}]: "
            ).strip()

            new_phone = input(
                f"Enter new phone [{contact['phone']}]: "
            ).strip()

            new_email = input(
                f"Enter new email [{contact['email']}]: "
            ).strip()

            if new_phone and any(
                other["phone"] == new_phone and other is not contact
                for other in contacts
            ):
                print("That phone number belongs to another contact.")
                return

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            save_contacts(contacts)
            print("Contact updated successfully!")
            return

    print("Contact not found.")


def delete_contact(contacts):
    print("\n--- Delete Contact ---")

    phone = input("Enter the phone number of the contact to delete: ").strip()

    for contact in contacts:
        if contact["phone"] == phone:
            confirm = input(
                f"Delete {contact['name']}? (yes/no): "
            ).strip().lower()

            if confirm == "yes":
                contacts.remove(contact)
                save_contacts(contacts)
                print("Contact deleted successfully!")
            else:
                print("Deletion cancelled.")
            return

    print("Contact not found.")


def main():
    contacts = load_contacts()

    while True:
        print("\n====== CONTACT BOOK ======")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Thank you for using Contact Book!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")


if __name__ == "__main__":
    main()
