#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, xmlrunner
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('.'))))
from Nurse_A.Settings import setup

Loader = unittest.defaultTestLoader
Loader.testMethodPrefix = 'test'
suites = Loader.discover('../PR_Regression', pattern='Test_*.py')
Runner = xmlrunner.XMLTestRunner(output='../reports', verbosity=2)
result = Runner.run(suites)
setup.delete_test_demo(setup.demo_data[1])
