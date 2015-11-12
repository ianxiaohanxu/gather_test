#!/bin/bash

ps -ax | grep -i appium | grep -v start_appium | awk '{print $1}' | xargs kill -9

devices=($(adb devices | awk '/device$/{print $1}'))

appium -p 4723 -bp 4724 -U ${devices[0]} &
appium -p 4725 -bp 4726 -U ${devices[1]} &

