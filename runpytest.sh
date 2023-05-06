#!/bin/bash
source mcontact-venv/bin/activate
pip3 install rich
pip3 install art
pytest -s
# Enter 6 to promt the program to exit