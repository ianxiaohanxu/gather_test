#!/bin/bash

ps -ax | grep "python \./manage\.py.*runserver.*Alex_test" | awk '{print $1;}' | xargs kill -9
