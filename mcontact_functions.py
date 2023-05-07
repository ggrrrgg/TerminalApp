import csv
import time
from rich import print
from rich.console import Console
from rich.progress import Progress
__version__ = '13.3.5'
__author__ = 'Will McGugan'

console = Console()
#Some repeat functions:
def invalid_input_yorn():
    console.print('Invalid input. Please only enter y or n: '
                              , style= 'bold red')
def invalid_input_empty():
    console.print('Sorry, field cannot be empty', style='bold red')
def return_menu_message():
    console.print('Returning to Main Menu', style='bold red')              
#Search function:
def search_mcontact(contact_master):
    console.print('Search Contacts', style='bold cyan')
    #Loop function for multiple input option
    while True:
        search_name = input('Search by Name? (y/n): ')
        if search_name.lower() == 'y':
            name_lookup = input('Enter the Name of the Contact: ').strip()
            with open(contact_master, 'r') as f:
                reader = csv.reader(f)
                found_match = False
                #Progress bar from rich module (see dev notes in readme)
                with Progress() as progress:
                                task1 = progress.add_task("[cyan]Searching..."
                                                          , total=10)
                                while not progress.finished:
                                    progress.update(task1, advance=0.8)
                                    time.sleep(0.1)
                for row in reader:
                    if (name_lookup == row[0]):
                        console.print(*row, style='bold cyan')
                        found_match = True
                if not found_match:
                    console.print('Sorry, no matches for that name'
                                  , style='bold cyan')
                    continue
        #Search by instr/location
        elif search_name.lower() == 'n':
            search_instr = input('Search by Instrument/City? (y/n): ')
            if search_instr.lower() == 'n':
                return_menu_message()
                break
            elif search_instr.lower() == 'y':
                instr_lookup = input('What kind of Instrumentalist do you need? ').strip()
                city_lookup = input('In which City / Location? ').strip()
                with open(contact_master, 'r') as f:
                    reader = csv.reader(f)
                    match_count = 0
                    #As above
                    with Progress() as progress:
                                task1 = progress.add_task("[cyan]Searching..."
                                                          , total=10)
                                while not progress.finished:
                                    progress.update(task1, advance=0.6)
                                    time.sleep(0.1)
                    for row in reader:
                        if(instr_lookup == row[3] and city_lookup == row[4]):
                            console.print(*row, style='bold cyan')
                            match_count += 1
                    if match_count == 0:
                        console.print('Sorry, no matches for that instrument in that location'
                                      , style='bold cyan')
            else:
                invalid_input_yorn()
                continue
        else:
            invalid_input_yorn()
            continue
        #Loop function?
        another = input('Would you like to Search again? y/n: ').strip()
        if another.lower() != 'y':
            return                        
#Add Contact                        
def add_mcontact(contact_master):
    console.print('Add Contact', style='bold green')
    #Using integers to prevent infinite loop if user just hits enter
    tries = 0
    while True:
        mcontact_name = input('Enter name: ').strip()
        if tries >= 2:
            return_menu_message()
            break
        if mcontact_name == '':
            tries += 1
            invalid_input_empty()
            continue
        mcontact_phone = input('Enter ph number: ').strip()
        if mcontact_phone == '':
            invalid_input_empty()
            continue
        mcontact_email = input('Enter email: ').strip()
        if mcontact_email == '':
            invalid_input_empty()
            continue
        mcontact_instr = input('Instrument / job: ').strip()
        mcontact_city = input('Enter city: ').strip()
        if mcontact_instr == '' and mcontact_city == '':
            console.print('Sorry, Contact must have an Instrument or a Location'
                          , style= 'bold red')
            continue
        #Write user input to csv
        with open(contact_master, 'a') as mcontact_file:
            writer = csv.writer(mcontact_file)
            writer.writerow([mcontact_name, mcontact_phone, mcontact_email,
                              mcontact_instr, mcontact_city])
        console.print('Contact Added', style='bold green')
        #Loop function?
        another = input('Would you like to Add another Contact? (y/n): ')
        if another.lower() != 'y':
            break     
#Update Contact
def update_mcontact(contact_master):
    console.print('Update Contact', style='bold purple')
    #Provide user option to see all their contacts to check details before updating
    display = input('Do you want to Display all Contacts? (y/n): ')
    if display.lower() == 'y':
        browse_mcontact(contact_master)
    #whileloop for updating multiple contacts:
    while True:
        mcontact_name = input('Enter the name of the Contact to Update: ').strip()
        mcontact_lists = []
        with open(contact_master, 'r') as f:
            reader = csv.reader(f)
            found_match = False
            for row in reader:
                if (mcontact_name == row[0]):
                    mcontact_lists.append(row)
                    console.print(*row, style='bold cyan')
                    found_match = True
            if not found_match:
                console.print('Sorry, could not find a contact with that name'
                              , style='bold red')
                return
        #Get user input for detail to update
        mcontact_update = input('Which Detail do you want to Update? ').strip()
        #Prevent blank input
        if mcontact_update == '':
            invalid_input_empty()
            continue
        mcontact_new_detail = input('Enter the New Detail: ').strip()
        if mcontact_new_detail == '':
            invalid_input_empty()
            continue
        #Swap detail for new detail on list
        for row in mcontact_lists:
            if mcontact_update in row:
                row[row.index(mcontact_update)] = mcontact_new_detail
        #Add all other contact to the list
        with open(contact_master, 'r') as f:
            reader = csv.reader(f)
            rows = [row for row in reader if row[0] != mcontact_name] + mcontact_lists
        #Write list to csv
        with open(contact_master, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        #Progress bar see dev notes in readme
        with Progress() as progress:
            task1 = progress.add_task("[purple]Updating...", total=10)
            while not progress.finished:
                progress.update(task1, advance=0.5)
                time.sleep(0.1) 
        #Output message
        for contact in mcontact_lists:
            console.print(*contact, style='bold cyan')
        console.print('Contact Updated', style='bold purple')
        #Loop function?
        another = input('Would you like to Update another Contact? (y/n): ')
        if another.lower() != 'y':
            break
#Remove Contact
def remove_mcontact(contact_master):
    console.print('Remove Contact', style= 'bold red')
    #Give option to display all contacts to check before removing
    display = input('Do you want to Display all Contacts? (y/n): ')
    if display.lower() == 'y':
        browse_mcontact(contact_master)
    #whileloop to give option to remove multiple entries without returning to menu
    while True: 
        mcontact_name = input('Enter the name of the contact you want to remove: ').strip()
        mcontact_lists = []
        #search csv using boolean variable, add all other rows to list
        with open(contact_master, 'r')as f:
            reader = csv.reader(f)
            found_match = False
            for row in reader:
                if (mcontact_name == row[0]):
                    found_match = True
                else:    
                    mcontact_lists.append(row)
            # Write new list to csv, output to user                    
            if found_match:                
                    with open(contact_master, 'w')as f:
                        writer = csv.writer(f)
                        writer.writerows(mcontact_lists)
                    console.print(f'{mcontact_name} Removed', style='bold red')
            else:
                console.print('Sorry, no Contact by that Name found'
                              , style='bold red')
                continue
        #Loop function?
        another = input('Would you like to Remove another Contact? (y/n): ')
        if another.lower() != 'y':
            break
#Browse CSV
def browse_mcontact(contact_master):
    console.print('Displaying Contacts...', style='bold dark_orange')
    #Open CSV and print using * to remove brackets and ,
    with open(contact_master, 'r')as f:
        reader = csv.reader(f)
        for row in reader:
            console.print(*row, style='bold cyan')
   
   
    