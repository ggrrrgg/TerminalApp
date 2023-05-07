import pytest
import csv
from main import create_menu
from mcontact_functions import add_mcontact
from unittest.mock import patch
import re

# TEST create_menu function:
# Press 6 to exit when menu is displayed to complete the test.

def test_create_menu(capfd):
    with patch('builtins.input'):
        create_menu()
    
    expected_output = (
        '\n'
        'Press 1 to Search a Contact\n'
        'Press 2 to Add a New Contact\n'
        'Press 3 to Update a Contact\n'
        'Press 4 to Remove a Contact\n'
        'Press 5 to Browse Contacts\n'
        'Press 6 to Exit\n'
        '\n'
    )
    out, err = capfd.readouterr()
    
    assert re.sub(r'\x1b\[\d+(;\d+)*m', '', expected_output) in re.sub(r'\x1b\[\d+(;\d+)*m', '', out)

# TEST add_mcontacts function:

contacts_test = 'contacts_test.csv'

def test_add_mcontact(monkeypatch):
    original_length = 0
    
    with open(contacts_test) as f:
        reader = csv.reader(f)
        original_length = sum(1 for row in reader)
    monkeypatch.setattr('builtins.input', lambda _: 'entry 1')
    add_mcontact(contacts_test)
    
    with open(contacts_test) as f:
        reader = csv.reader(f)
        new_length = sum(1 for row in reader)
    
    print(original_length)
    print(new_length)
    
    assert new_length == original_length + 1




