import csv

def search_mcontact(contact_master):

    
    search_name = input('Search by Name? (y/n): ')
    if search_name == 'y':
        name_lookup = input('Enter the Name of the Contact: ')
        with open(contact_master, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if (name_lookup == row[0]):
                    print(row)
                    return
                
    else:
        search_instr = input('Search by Instrument/City? (y/n): ')
        if search_instr != 'y':
            print('Returning to Main Menu')
            
        else:
            instr_lookup = input('What kind of Instrumentalist do you need? ')
            city_lookup = input('In which City / Location? ')
            with open(contact_master, 'r') as f:
                reader = csv.reader(f)
                match_count = 0
                for row in reader:
                    if(instr_lookup == row[3] and city_lookup == row[4]):
                        print(row)
                        match_count += 1
                if match_count == 0:
                    print('Sorry, no matches for that instrument in that location')
                        
                    
def add_mcontact(contact_master):
    
    while True:
        print('Adding New Contact...')
        mcontact_name = input('Enter name: ')
        mcontact_phone = input('Enter ph number: ')
        mcontact_email = input('Enter email: ')
        mcontact_instr = input('Instrument / job: ')
        mcontact_city = input('Enter city: ')
        with open(contact_master, 'a') as mcontact_file:
            writer = csv.writer(mcontact_file)
            writer.writerow([mcontact_name, mcontact_phone, mcontact_email, mcontact_instr, mcontact_city])
        print('Contact Added')
        another = input('Would you like to Add another Contact? (y/n): ')
        if another != 'y':
            break     

def update_mcontact(contact_master):
    
    browse_mcontact(contact_master)

    while True:
        mcontact_name = input('Enter the name of the Contact to Update: ')
        mcontact_lists = []
        
        with open(contact_master, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if (mcontact_name == row[0]):
                    mcontact_lists.append(row)
                    print(row)
        
        mcontact_update = input('Which Detail do you want to Update? ')
        mcontact_new_detail = input('Enter the New Detail: ')
        
        for row in mcontact_lists:
            if mcontact_update in row:
                row[row.index(mcontact_update)] = mcontact_new_detail
        
        with open(contact_master, 'r') as f:
            reader = csv.reader(f)
            rows = [row for row in reader if row[0] != mcontact_name] + mcontact_lists
        
        with open(contact_master, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        
        print('Updating...')
        print(mcontact_lists)
        print('Contact Updated')
        
        another = input('Would you like to Update another Contact? (y/n): ')
        if another != 'y':
            break

def remove_mcontact(contact_master):
    
    browse_mcontact(contact_master)
    
    while True: 
        print('Remove Contact...')
        mcontact_name = input('Enter the name of the contact you want to remove: ')
        mcontact_lists = []
        
        with open(contact_master, 'r')as f:
            reader = csv.reader(f)
            for row in reader:
                if not row:
                    continue
                if(mcontact_name != row[0]):
                    mcontact_lists.append(row)
        # print(mcontact_lists)

        with open(contact_master, 'w')as f:
            writer = csv.writer(f)
            writer.writerows(mcontact_lists)
        print(f'{mcontact_name} Removed')
        
        another = input('Would you like to Remove another Contact? (y/n): ')
        if another != 'y':
            break

def browse_mcontact(contact_master):
    
    print('Displaying Contacts...')
    
    with open(contact_master, 'r')as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

   
    