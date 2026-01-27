contacts = {}

while True:
    print('\nContact Book App')
    print('1. Add Contact')
    print('2. View Contact')
    print('3. Search Contact')
    print('4. Update Contact')
    print('5. Delete Contact')
    print('6. View All Contacts')
    print('7. Exit')

    choice = input('Enter your choice: ')

    if choice == '1':
        name = input('Enter your name: ')
        if name in contacts:
            print(f'Contact name {name} already exists!')
        else:
            age = input('Enter age: ')
            email = input('Enter email: ')
            mobile = input('Enter mobile number: ')
            contacts[name] = {'age': int(age), 'email': email, 'mobile': mobile}
            print(f'Contact {name} has been created successfully.')

    elif choice == '2':
        name = input('Enter contact name to view: ')
        if name in contacts:
            contact = contacts[name]
            print(f"Name: {name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}")
        else:
            print(f"Contact {name} not found!")

    elif choice == '3':
        search_name = input('Enter name to search: ')
        if search_name in contacts:
            contact = contacts[search_name]
            print(f"Found -> Name: {search_name}, Age: {contact['age']}, Email: {contact['email']}, Mobile: {contact['mobile']}")
        else:
            print("No contact found with that name.")

    elif choice == '4':
        name = input('Enter contact name to update: ')
        if name in contacts:
            print("Leave blank if you don’t want to change a field.")
            age = input('Enter new age: ')
            email = input('Enter new email: ')
            mobile = input('Enter new mobile number: ')
            if age:
                contacts[name]['age'] = int(age)
            if email:
                contacts[name]['email'] = email
            if mobile:
                contacts[name]['mobile'] = mobile
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact {name} not found!")

    elif choice == '5':
        name = input('Enter contact name to delete: ')
        if name in contacts:
            del contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact {name} not found!")

    elif choice == '6':
        if contacts:
            print("\nAll Contacts:")
            for name, info in contacts.items():
                print(f"Name: {name}, Age: {info['age']}, Email: {info['email']}, Mobile: {info['mobile']}")
        else:
            print("No contacts available.")

    elif choice == '7':
        print("Exit. !")
        break

    else:
        print("Invalid choice. Please try again.")
