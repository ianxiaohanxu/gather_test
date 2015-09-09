#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest, xmlrunner

Loader = unittest.defaultTestLoader
Loader.testMethodPrefix = 'test'
suites = Loader.discover('../PR_Regression', pattern='Test_*.py')
Runner = xmlrunner.XMLTestRunner(output='../reports', verbosity=2)
result = Runner.run(suites)
