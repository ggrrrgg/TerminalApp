from mcontact_functions import search_mcontact, add_mcontact, update_mcontact, remove_mcontact, browse_mcontact
import csv

print('Hi, welcome to your Musician Contacts')

contact_master = 'contacts.csv'

try:
    mcontact_file = open(contact_master, 'r')
    mcontact_file.close()

except FileNotFoundError as e:
    mcontact_file = open(contact_master, 'w')
    mcontact_file.write('Name, Phone, Email, Instrument, City\n')
    mcontact_file.close()
        

def create_menu():
    
    print('1. Press 1 to Search a Contact')
    print('2. Press 2 to Add a New Contact')
    print('3. Press 3 to Update a Contact')
    print('4. Press 4 to Remove a Contact')
    print('5. Press 5 to Browse Contacts')
    print('6. Press 6 to Exit')
    
    choice = input('Enter your Selection: ')
    return choice

user_choice = ''

while user_choice != '6':
    user_choice = create_menu()

    if (user_choice == '1'):
        search_mcontact(contact_master)
    elif (user_choice == '2'):
        add_mcontact(contact_master)
    elif (user_choice == '3'):
        update_mcontact(contact_master)
    elif (user_choice == '4'):
        remove_mcontact(contact_master)
    elif (user_choice == '5'):
        browse_mcontact(contact_master)
    elif (user_choice == '6'):
        continue
    else:
        print('Invalid Input')

    input('Press Enter to continue...')

print('Thankyou bye bye')

