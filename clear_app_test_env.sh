#!/bin/bash
ps -ax | grep -i genymotion | grep -v grep | awk '{print $1}' | xargs kill -9
ps -ax | grep -i appium | grep -v grep | awk '{print $1}' | xargs kill -9
