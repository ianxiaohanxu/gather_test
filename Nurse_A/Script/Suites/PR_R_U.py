#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, xmlrunner

Loader = unittest.defaultTestLoader
Loader.testMethodPrefix = 'test_urgent'
suites = Loader.discover('../PR_Regression', pattern='Test_*.py')
Runner = xmlrunner.XMLTestRunner(output='../reports')
result = Runner.run(suites)
