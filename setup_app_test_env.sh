#!/bin/bash

ps -ax | grep -i genymotion | grep -v grep | awk '{print $1}' | xargs kill -9
ps -ax | grep -i appium | grep -v grep | awk '{print $1}' | xargs kill -9

function setup_emulator(){
    # Start emulators
    for i in $@; do
        if [[ $(uname -s)=='Darwin' ]]; then
            /Applications/Genymotion.app/Contents/MacOS/player --vm-name $i&
        #elif [[ $(uname -s)=='Linux' ]]; then
            #<Genymotion installer path>/player --vm-name $i&
        fi
    done
    # Verify emulators available
    sleep 60
    (( $(adb devices | grep -c device$)==2 )) || exit 1
}

function install_apps(){
    # Get emulators' name
    devices=($(adb devices | awk '/device$/{print $1}'))
    len=${#devices[*]}

    # Uninstall duplicate app
    for ((i = 0; i < $len; i++)); do
        adb -s ${devices[$i]} wait-for-device
        adb -s ${devices[$i]} uninstall com.gatherhealth.gatherdm
        adb -s ${devices[$i]} uninstall com.gatherhealth.gatherpro
        #while [ $# -gt 0  ]; do
        #    adb -s ${devices[$i]} install $1
        #    shift
        #done
        for j in $@; do
            adb -s ${devices[$i]} install $j
        done
    done
}

function start_appium(){
    devices=($(adb devices | awk '/device$/{print $1}'))
    port=4723
    for i in ${devices[@]}; do
        appium -p $((port++)) -bp $((port++)) -U $i &
        ((port+=2))
    done
}

setup_emulator 4.4.4 5.0.0 || exit 1
install_apps ~/Desktop/app-debug.apk ~/Desktop/doctor.apk || exit 1
start_appium

