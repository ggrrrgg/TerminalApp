from rich import print
from rich.console import Console
__version__ = '13.3.5'
__author__ = 'Will McGugan'
from art import *
__version__ = '5.9'
__author__ = 'Sepand Haghighi'
from mcontact_functions import search_mcontact, add_mcontact, update_mcontact, remove_mcontact, browse_mcontact
#rich variable
console = Console()
#Welcome message
console.print(':guitar:'' Hi, welcome to your Musician Contacts '
              ':guitar:', style='bold underline red on light_goldenrod1')
#Add a blank line
print()
#define csv
contact_master = 'contacts.csv'
#tryexcept to create a new csv if none exists
try:
    mcontact_file = open(contact_master, 'r')
    mcontact_file.close()
except FileNotFoundError as e:
    mcontact_file = open(contact_master, 'w')
    mcontact_file.write('NAME, PHONE, EMAIL, INSTRUMENT, CITY\n')
    mcontact_file.close()
#create main menu        
def create_menu():
    print()
    console.print('Press 1 to [bold cyan]Search[/] a Contact')
    console.print('Press 2 to [bold green]Add[/] a New Contact')
    console.print('Press 3 to [bold purple]Update[/] a Contact')
    console.print('Press 4 to [bold red]Remove[/] a Contact')
    console.print('Press 5 to [bold dark_orange]Browse[/] Contacts')
    console.print('Press 6 to [bold yellow]Exit[/]')
    print()
    choice = input('Enter your Selection: ')
    return choice
#define user choice variable
user_choice = ''
#whileloop to run main menu
while user_choice != '6':
    user_choice = create_menu()
    #match case for selections
    match user_choice:
        case '1':
            search_mcontact(contact_master)
        case '2':
            add_mcontact(contact_master)
        case '3':
            update_mcontact(contact_master)
        case '4':
            remove_mcontact(contact_master)
        case '5':
            browse_mcontact(contact_master)
        case '6':
            continue
        case x:
            console.print('Invalid Input', style= 'bold red')

    input('Press Enter to continue...')
print()
#Exit message using art module
console.print(':waving_hand:'' Thankyou for using... '
              ':waving_hand:', style='bold underline light_goldenrod1 on red')
print()
tprint('GOODBYE', 'rnd-medium')
