import pytest
from main import create_menu
from unittest.mock import patch
import re

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



