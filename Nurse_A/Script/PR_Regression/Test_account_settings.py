#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
from time import sleep, time
import unittest
from Nurse_A.Settings import keycode, constant, data
from Nurse_A.Scenario.web_scenario import WEB

class Account_settings(unittest.TestCase):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        
    def tearDown(self):
        self.pr.teardown()
        
    def test_reset_password(self):
        # This test is for '107009 Reset password'
        PASSWORD = '234567'
        LESS_PASSWORD = '12345'
        WRONG_PASSWORD = '345678'
        self.pr.login(data.INDIA_DOCTOR, data.PASSWORD)
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        # Validation check for short password
        self.pr.enter(LESS_PASSWORD, data.PR_ACCOUNT_NEW_PASSWORD)
        self.pr.click(data.PR_ACCOUNT_CONFIRM_PASSWORD)
        self.assertEqual(self.pr.focus(data.PR_ACCOUNT_NEW_PASSWORD).get_attribute('class'), 'invalid')
        self.pr.verify(data.PR_ACCOUNT_PASSWORD_ERROR)
        self.assertEqual(self.pr.text(data.PR_ACCOUNT_PASSWORD_ERROR), data.EM_PR_ACCOUNT_PASSWORD_LENGH)
        self.assertEqual(self.pr.text(data.PR_ACCOUNT_PASSWORD_STRENGTH), data.EM_PR_ACCOUNT_PASSWROD_STRENGTH_TOO_WEAK)
        # Validation check for password lengh match
        self.pr.clear(data.PR_ACCOUNT_NEW_PASSWORD)
        self.pr.enter(PASSWORD, data.PR_ACCOUNT_NEW_PASSWORD)
        self.pr.enter(WRONG_PASSWORD, data.PR_ACCOUNT_CONFIRM_PASSWORD)
        self.pr.click(data.PR_ACCOUNT_PASSWORD_STRENGTH)
        self.assertEqual(self.pr.focus(data.PR_ACCOUNT_CONFIRM_PASSWORD).get_attribute('class'), 'invalid')
        self.assertEqual(self.pr.text(data.PR_ACCOUNT_PASSWORD_ERROR), data.EM_PR_ACCOUNT_PASSWORD_MATCH)
        self.assertEqual(self.pr.text(data.PR_ACCOUNT_PASSWORD_STRENGTH), data.EM_PR_ACCOUNT_PASSWROD_STRENGTH_WEAK)
        # Reset password
        self.pr.clear(data.PR_ACCOUNT_CONFIRM_PASSWORD)
        self.pr.enter(PASSWORD, data.PR_ACCOUNT_CONFIRM_PASSWORD)
        self.assertTrue(self.pr.focus(data.PR_ACCOUNT_SAVE_ALL_BUTTON).is_enabled())
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        
        self.pr.logout()
        self.pr.login(data.INDIA_DOCTOR, PASSWORD)
        # Resume password
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.enter(data.PASSWORD, data.PR_ACCOUNT_NEW_PASSWORD)
        self.pr.enter(data.PASSWORD, data.PR_ACCOUNT_CONFIRM_PASSWORD)
        self.assertTrue(self.pr.focus(data.PR_ACCOUNT_SAVE_ALL_BUTTON).is_enabled())
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        
if __name__ == '__main__':
    unittest.main()