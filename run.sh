#!/bin/bash

# Activate virtualenv
if
source ./venv/bin/activate
then
echo 'Activate virtualenv'
else
exit 1
fi

# Intall dependence modules
pip install --upgrade -r requirements/test.txt

# Install loacal package
pushd Nurse_A
python setup.py sdist
python setup.py install

popd

# Run test scripts
pushd Nurse_A/Script/Suites
rm -rf ../reports/*
python PR_R_A.py

