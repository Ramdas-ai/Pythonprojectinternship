# CODSOFT - TASK 5: CONTACT BOOK

contacts = []

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    email = input("Email: ")
    address = input("Address: ")

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"\nContact {i}:")
            for key, value in contact.items():
                print(f"{key.capitalize()}: {value}")

def search_contact():
    term = input("Search name or phone: ")
    found = False

    for contact in contacts:
        if term.lower() in contact["name"].lower() or term == contact["phone"]:
            print("\nFound Contact:")
            for key, value in contact.items():
                print(f"{key.capitalize()}: {value}")
            found = True

    if not found:
        print("No match found.")

def update_contact():
    search_contact()
    name = input("\nEnter the name of contact to update: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contact["phone"] = input("New Phone: ")
            contact["email"] = input("New Email: ")
            contact["address"] = input("New Address: ")
            print("Contact updated!")
            return

    print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")

    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            print("Contact deleted.")
            return

    print("Contact not found.")

while True:
    print("\n--- CONTACT BOOK MENU ---")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose: ")

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
        break
    else:
        print("Invalid choice!")
