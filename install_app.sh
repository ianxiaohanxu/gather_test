#!/bin/bash

# Get emulators' name
devices=($(adb devices | awk '/device$/{print $1}'))
(( ${#devices[@]}!=2 )) && exit 1
# Uninstall duplicate app
adb -s ${devices[0]} wait-for-device
adb -s ${devices[0]} uninstall com.gatherhealth.gatherdm
adb -s ${devices[0]} uninstall com.gatherhealth.gatherpro

adb -s ${devices[1]} wait-for-device
adb -s ${devices[1]} uninstall com.gatherhealth.gatherdm
adb -s ${devices[1]} uninstall com.gatherhealth.gatherpro

# Install test app
adb -s ${devices[0]} install ~/Desktop/app-release.apk 
#adb -s ${devices[0]} install <gatherpro_apk_path>

adb -s ${devices[1]} install ~/Desktop/app-release.apk
#adb -s ${devices[1]} install <gatherpro_apk_path>
