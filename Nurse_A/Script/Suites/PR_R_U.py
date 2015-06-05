#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unittest

Loader = unittest.defaultTestLoader
Loader.testMethodPrefix = 'test_urgent'
suites = Loader.discover('../PR_Regression', pattern='Test_*.py')
Runner = unittest.TextTestRunner(verbosity=2)
result = Runner.run(suites)
