#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, xmlrunner

Loader = unittest.defaultTestLoader
Loader.testMethodPrefix = 'test_urgent'
suites = Loader.discover('../PR_Regression', pattern='Test_account*.py')
# suites = Loader.loadTestsFromModule('../PR_Regression/Test_account_settings')
Runner = xmlrunner.XMLTestRunner(output='../reports', verbosity=2)
# Runner = unittest.TextTestRunner(verbosity=2)
result = Runner.run(suites)
