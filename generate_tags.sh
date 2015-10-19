#!/bin/bash
ctags -R --languages=Python -f tags_temp venv/lib/python2.7/site-packages 
mv -f tags_temp tags
