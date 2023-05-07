#!/bin/bash
pip3 -V 
python3 -m venv mcontact-venv
source mcontact-venv/bin/activate
pip3 install rich
pip3 install art
clear
python3 main.py