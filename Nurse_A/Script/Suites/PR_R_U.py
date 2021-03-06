#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('.'))))
from Nurse_A.Settings import setup
from Nurse_A.Ext_unittest.XMLrunner import xmlTestRunner

Loader = unittest.defaultTestLoader
Loader.testMethodPrefix = 'test'
suites = Loader.discover('../PR_Regression', pattern='Test_*.py')
Runner = xmlTestRunner(output='../reports', verbosity=2)
result = Runner.run(suites)
setup.delete_test_demo(setup.demo_data[1])
setup.delete_test_demo(setup.demo_data1[1])
setup.delete_test_demo(setup.demo_data2[1])
