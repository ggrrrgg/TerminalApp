import csv
from rich import print
from rich.console import Console

console = Console()

def search_mcontact(contact_master):

    console.print('Search Contacts', style='bold cyan')

    search_name = input('Search by Name? (y/n): ')
    if search_name == 'y':
        name_lookup = input('Enter the Name of the Contact: ')
        with open(contact_master, 'r') as f:
            reader = csv.reader(f)
            found_match = False
            for row in reader:
                if (name_lookup == row[0]):
                    console.print(row, style='bold cyan')
                    found_match = True
            if not found_match:
                console.print('Sorry, no matches for that name', style='bold cyan')
                return
                
    else:
        search_instr = input('Search by Instrument/City? (y/n): ')
        if search_instr != 'y':
            console.print('Returning to Main Menu', style='bold cyan')
            
        else:
            instr_lookup = input('What kind of Instrumentalist do you need? ')
            city_lookup = input('In which City / Location? ')
            with open(contact_master, 'r') as f:
                reader = csv.reader(f)
                match_count = 0
                for row in reader:
                    if(instr_lookup == row[3] and city_lookup == row[4]):
                        console.print(row, style='bold cyan')
                        match_count += 1
                if match_count == 0:
                    console.print('Sorry, no matches for that instrument in that location', style='bold cyan')
                        
                    
def add_mcontact(contact_master):
    
    console.print('Add Contact', style='bold green')
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
        console.print('Contact Added', style='bold green')
        another = input('Would you like to Add another Contact? (y/n): ')
        if another != 'y':
            break     

def update_mcontact(contact_master):
    
    console.print('Update Contact', style='bold purple')
    browse_mcontact(contact_master)

    while True:
        mcontact_name = input('Enter the name of the Contact to Update: ')
        mcontact_lists = []
        
        with open(contact_master, 'r') as f:
            reader = csv.reader(f)
            found_match = False
            for row in reader:
                if (mcontact_name == row[0]):
                    mcontact_lists.append(row)
                    console.print(row, style='bold purple')
                    found_match = True
            if not found_match:
                console.print('Sorry, could not find a contact with that name', style='bold purple')
                return
        
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
        
        console.print('Updating...', style='bold purple')
        console.print(mcontact_lists, style='bold purple')
        console.print('Contact Updated', style='bold purple')
        
        another = input('Would you like to Update another Contact? (y/n): ')
        if another != 'y':
            break

def remove_mcontact(contact_master):
    
    console.print('Remove Contact', style= 'bold red')
    browse_mcontact(contact_master)
    
    while True: 
        
        mcontact_name = input('Enter the name of the contact you want to remove: ')
        mcontact_lists = []
        
        with open(contact_master, 'r')as f:
            reader = csv.reader(f)
            for row in reader:
                if(mcontact_name != row[0]):
                    mcontact_lists.append(row)
                    return
                
        with open(contact_master, 'w')as f:
            writer = csv.writer(f)
            writer.writerows(mcontact_lists)
        console.print(f'{mcontact_name} Removed', style='bold red')
        
        another = input('Would you like to Remove another Contact? (y/n): ')
        if another != 'y':
            break

def browse_mcontact(contact_master):
    
    console.print('Displaying Contacts...', style='bold dark_orange')
    
    with open(contact_master, 'r')as f:
        reader = csv.reader(f)
        for row in reader:
            console.print(row, style='bold dark_orange')

   
    