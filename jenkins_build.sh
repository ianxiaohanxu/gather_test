#!/bin/bash

source ./venv/bin/activate
pip install -r requirements/test.txt
cd Nurse_A
python setup.py sdist
python setup.py install
