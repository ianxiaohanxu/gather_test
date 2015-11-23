#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('.'))))
from Nurse_A.Settings import setup
from Nurse_A.Ext_unittest.XMLrunner import xmlTestRunner
from Nurse_A.Scenario.android_scenario import ANDROID

ANDROID(PORT='4723').set_server()

Loader = unittest.defaultTestLoader
Loader.testMethodPrefix = 'test_normal'
suites = Loader.discover('../Android/Patient_app', pattern='Test_*.py')
Runner = xmlTestRunner(output='../reports', verbosity=2)
result = Runner.run(suites)
setup.delete_test_demo(setup.demo_data[1])
setup.delete_test_demo(setup.demo_data1[1])
setup.delete_test_demo(setup.demo_data2[1])

