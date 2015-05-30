#!/bin/bash

source ./venv/bin/activate
pip install -r requirements/test.txt
python ./Nurse_A/Script/PR_Regression/Test_chat.py
