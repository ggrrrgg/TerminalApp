import csv

def search_mcontact(file_name):
    pass

def add_mcontact(file_name):
    print('Adding New Contact...')
    mcontact_name = input('Enter name: ')
    mcontact_phone = input('Enter ph number: ')
    mcontact_email = input('Enter email: ')
    mcontact_instr = input('Instrument / job: ')
    mcontact_city = input('Enter city: ')
    with open(file_name, 'a')as mcontact_file:
        writer = csv.writer(mcontact_file)
        writer.writerow([mcontact_name, mcontact_phone, mcontact_email, mcontact_instr, mcontact_city])
    
def edit_mcontact(file_name):
    pass

def remove_mcontact(file_name): 
    print('Removing Contact...')
    browse_mcontact(file_name)
    mcontact_name = input('Enter the name of the contact you want to remove: ')
    


def browse_mcontact(file_name):
    print('Browsing Contacts...')
    with open(file_name, 'r')as reader:
        csv.reader = reader
        for row in csv.reader:
            print(row)
    