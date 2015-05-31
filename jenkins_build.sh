#!/bin/bash

# If no virtualenv in ~/Temp/, create virtualenv there
if 
! test -e ~/Temp/venv
then
~/.virtualenv ~/Temp/venv
fi

# Activate virtualenv
if
. ~/Temp/venv/bin/activate
then
echo 'Activate virtualenv'
fi

# Intall dependence modules
~/.pip install -r requirements/test.txt

# Install loacal package
# cp -R ./Nurse_A/Nurse_A ~/Temp/ 
# cp -Rf ./Nurse_A/setup.py ~/Temp/
# pushd ~/Temp/
# python setup.py sdist
# python setup.py install
pushd Nurse_A
python setup.py sdist
python setup.py install

popd
