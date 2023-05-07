#!/bin/bash
python3 -m venv mcontact-venv
source mcontact-venv/bin/activate
pip3 install pytest
pip3 install rich
pip3 install art
pytest -s
# Enter 6 when main menu appears to complete the test