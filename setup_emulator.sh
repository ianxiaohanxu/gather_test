#!/bin/bash

# Kill the existing genymotion process
ps -ax | grep -i genymotion | grep -v grep | awk '{print $1}' | xargs kill -9

# Start emulators
emulator1="4.4.4"
emulator2="5.0.0"
if [[ $(uname -s)=='Darwin' ]]; then
    /Applications/Genymotion.app/Contents/MacOS/player --vm-name $emulator1&
    /Applications/Genymotion.app/Contents/MacOS/player --vm-name $emulator2&
#elif [[ $(uname -s)=='Linux' ]]; then
    #<Genymotion installer path>/player --vm-name $emulator1&
    #<Genymotion installer path>/player --vm-name $emulator2&
fi

# Verify emulators available
sleep 10
(( $(adb devices | grep -c device$)==2 )) || exit 1

