#!/bin/bash

# Activate virtualenv
if
. /var/lib/jenkins/.virtualenvs/gh-test/bin/activate 
then
echo 'Activate virtualenv'
fi

# Intall dependence modules
pip install --upgrade -r requirements/test.txt

# Install loacal package
pushd Nurse_A
python setup.py sdist
python setup.py install

popd

# Run test on virtual screen
export DISPLAY=:99

# Run test scripts
pushd Nurse_A/Script/Suites
python PR_R_U.py

popd
