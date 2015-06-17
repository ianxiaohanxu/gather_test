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
# export PATH=$PATH:/usr/local/bin
Xvfb :98 -ac -screen 0 1920x1080x16 &
export DISPLAY=:98

# Run test scripts
pushd Nurse_A/Script/Suites
python PR_R_U.py
# python Nurse_A/Script/PR_Regression/Test_account_settings.py
popd

# Kill virtual screen
ps -ax | grep "Xvfb.:98" | awk '{print $1;}' | xargs kill -9
