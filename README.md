#   T1 A3 TERMINAL APP
---
# MUSICIAN CONTACT BOOK
---
## Github Repo:

https://github.com/ggrrrgg/TerminalApp

## Trello Project Board:

https://trello.com/b/99cdDa23/terminal-app

## Presentation Video:

https://vimeo.com/824479988?share=copy

---
## INSTALLATION:

- To run mcontacts, you will need Python 3 (at least v3.7) installed on your system. 

- Open an instance of Terminal and navigate to the 'src' folder within the application directory.

- Type ./run.sh and hit enter.

- Additional required Python modules will be automatically installed and the application will run. For further reference of modules, see requirements.txt.

___

## GUIDE FOR USING THE APP:

### Overview
The mcontacts app is designed to function as a standard contact app would but with an additional search capability. The search function is configured to allow standard search by name but also gives you the ability to search by 'instrument or job (eg producer or sound engineer)' and location. If you are a producer or musical director and need a specific player for a show or session in a place thats unfamiliar you will be able to bring up a list of all the relevant people you know efficiently.

### Features
At initialization the app brings up a main menu feature which is self explanatory. 6 options allow you to create, edit, remove, update, and search your contact book. On selection, each function will guide through the process and then return you to the main menu. When finished, option 6 exits the application.

<i>note - In order for the search function to work as intended it is highly recommended to use consistent spelling for each instrument / location when adding or updating an entry. For example use 'Engineer' every time you are adding a new engineer contact, not 'Soundie' or 'Soundguy' etc (ver 2.0 will include a class system to address this issue, but in this instance of the application, the dev team were insufficiently briefed by management to implement this feature prior to release).</i>

---
## SYSTEM HARDWARE REQUIREMENTS:

Win, Mac, or Linux 64 bit OS with (or equivalent):

<i> 'rich' module cannot run on versions earlier than Python 3.7 which will run on Windows 7 but no earlier. Highly recommended to run latest OS version available </i>

CPU: 11th Gen Intel(R) Core(TM) i7-11800H @ 2.30GHz 

RAM: 64.0 GB RAM

Storage: 40MB

Application may run with lower spec but is untested.

---
## Development Notes:
Included is a pytest file. Run this by entering ./runpytest.sh in the terminal. This will test 2 functions of the program <i>(note press 6 when the main menu appears during the test to complete it).</i>

I applied DRY principles as best I could, a lot of lines of code for each function are almost identical and with tweaking the wording of output to the user they could have been turned into functions that would be globally applicable, BUT I decided not to do this as it has a less meaningful experience for the user.

eg.
I have used the progress bar feature from the rich module in a couple of functions, the ony difference is in the search function it displays 'Searching...', in the update function it displays 'Updating...'. Here I could have changed the word to 'Processing...'.

I had some problems with applying code style, specifically to line length, in several places I have nested if else statements that push the line length out but when I tried to format them using \ etc, the code breaks or displays bad looking out put to the user so I have left them.







