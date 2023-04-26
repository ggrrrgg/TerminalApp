def create_menu():
    print('1. Press 1 to Search by Name')
    print('2. Press 2 to Search by Instrument/Location')
    print('3. Press 3 to Add a New Contact')
    print('4. Press 4 to Edit a Contact')
    print('5. Press 5 to Remove a Contact')
    print('6. Press 6 to Exit')
    choice = input('Enter your Selection: ')
    return choice

user_choice = ''

while user_choice != '6':
    user_choice = create_menu()

    if (user_choice == '1'):
        pass
    elif (user_choice == '2'):
        pass
    elif (user_choice == '3'):
        pass
    elif (user_choice == '4'):
        pass
    elif (user_choice == '5'):
        pass
    elif (user_choice == '6'):
        continue
    else:
        print('Invalid Input')

    input('Press Enter to continue...')

print('Thankyou bye bye')

