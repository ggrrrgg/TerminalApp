from mcontact_functions import search_mcontact, add_mcontact, update_mcontact, remove_mcontact, browse_mcontact
from rich import print
from rich.console import Console

console = Console()

console.print(':guitar:'' Hi, welcome to your Musician Contacts '':guitar:', style='bold underline red on light_goldenrod1')

contact_master = 'contacts.csv'

try:
    mcontact_file = open(contact_master, 'r')
    mcontact_file.close()

except FileNotFoundError as e:
    mcontact_file = open(contact_master, 'w')
    mcontact_file.write('Name, Phone, Email, Instrument, City\n')
    mcontact_file.close()
        

def create_menu():
    
    console.print('Press 1 to [bold cyan]Search[/] a Contact')
    console.print('Press 2 to [bold green]Add[/] a New Contact')
    console.print('Press 3 to [bold purple]Update[/] a Contact')
    console.print('Press 4 to [bold red]Remove[/] a Contact')
    console.print('Press 5 to [bold dark_orange]Browse[/] Contacts')
    console.print('Press 6 to [bold yellow]Exit[/]')
    
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

console.print(':waving_hand:'' Thankyou bye bye '':waving_hand:', style='bold underline light_goldenrod1')

