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
from Nurse_A.Ext_unittest.Testcase import Case

class Account_settings(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        
    def tearDown(self):
        self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
        
    def generate_number(self, length):
        # Generate valid & invalid numbers with length
        number = ''
        while(length > 0):
            number += '1'
            length -= 1
        short_number = number[:-1]
        long_number = number + '1'
        letter_number = number[:-1] + 'a'
        return number, short_number, long_number, letter_number
        
    def _number_validation(self, number, length):
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter(number, data.PR_ACCOUNT_CELL_NUMBER)
        self.assertEqual(self.pr.focus(data.PR_ACCOUNT_CELL_NUMBER).get_attribute('data-validate-status'), 'invalid')
        self.pr.verify(data.PR_ACCOUNT_CELL_ERROR)
        if length == 10:
            self.assertEqual(self.pr.text(data.PR_ACCOUNT_CELL_ERROR), data.EM_PR_ACCOUNT_CELL_NUM_IN_US)
        elif length == 8:
            self.assertEqual(self.pr.text(data.PR_ACCOUNT_CELL_ERROR), data.EM_PR_ACCOUNT_CELL_NUM_HK)
        else:
            self.assertEqual(self.pr.text(data.PR_ACCOUNT_CELL_ERROR), data.EM_PR_ACCOUNT_CELL_NUM_CH)
        self.assertFalse(self.pr.focus(data.PR_ACCOUNT_SEND_SMS_BUTTON).is_enabled())
        self.assertFalse(self.pr.focus(data.PR_ACCOUNT_SAVE_ALL_BUTTON).is_enabled())
        
    def number_validation_check(self, country_code, length):
        # Do validation check for different cell number (e.g. for US, country code is 1, length is 10)
        number, short_number, long_number, letter_number = self.generate_number(length)
        self.pr.select(country_code, data.PR_ACCOUNT_COUNTRY_CODE)
        self._number_validation(short_number, length)
        self._number_validation(long_number, length)
        self._number_validation(letter_number, length)
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter(number, data.PR_ACCOUNT_CELL_NUMBER)
        self.assertEqual(self.pr.focus(data.PR_ACCOUNT_CELL_NUMBER).get_attribute('data-validate-status'), 'valid')
        self.assertFalse(self.pr.is_element_present(data.PR_ACCOUNT_CELL_ERROR))
        self.assertTrue(self.pr.focus(data.PR_ACCOUNT_SEND_SMS_BUTTON).is_enabled())
        self.assertTrue(self.pr.focus(data.PR_ACCOUNT_SAVE_ALL_BUTTON).is_enabled())
        
    def test_urgent_reset_password(self):
        # This test is for '107009 Reset password'
        PASSWORD = '234567'
        LESS_PASSWORD = '12345'
        WRONG_PASSWORD = '345678'
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        # Validation check for short password
        self.pr.click(data.PR_ACCOUNT_NEW_PASSWORD)
        self.pr.enter(LESS_PASSWORD, data.PR_ACCOUNT_NEW_PASSWORD)
        self.pr.click(data.PR_ACCOUNT_CONFIRM_PASSWORD)
        self.pr.verify(data.PR_ACCOUNT_PASSWORD_ERROR)
        self.assertEqual(self.pr.focus(data.PR_ACCOUNT_NEW_PASSWORD).get_attribute('class'), 'invalid')
        self.assertEqual(self.pr.text(data.PR_ACCOUNT_PASSWORD_ERROR), data.EM_PR_ACCOUNT_PASSWORD_LENGH)
        self.assertEqual(self.pr.text(data.PR_ACCOUNT_PASSWORD_STRENGTH), data.EM_PR_ACCOUNT_PASSWROD_STRENGTH_TOO_WEAK)
        self.assertFalse(self.pr.focus(data.PR_ACCOUNT_SAVE_ALL_BUTTON).is_enabled())
        # Validation check for password lengh match
        self.pr.clear(data.PR_ACCOUNT_NEW_PASSWORD)
        self.pr.enter(PASSWORD, data.PR_ACCOUNT_NEW_PASSWORD)
        self.pr.enter(WRONG_PASSWORD, data.PR_ACCOUNT_CONFIRM_PASSWORD)
        self.pr.click(data.PR_ACCOUNT_PASSWORD_STRENGTH)
        self.pr.verify(data.PR_ACCOUNT_PASSWORD_ERROR)
        self.assertEqual(self.pr.focus(data.PR_ACCOUNT_CONFIRM_PASSWORD).get_attribute('class'), 'invalid')
        self.assertEqual(self.pr.text(data.PR_ACCOUNT_PASSWORD_ERROR), data.EM_PR_ACCOUNT_PASSWORD_MATCH)
        self.assertEqual(self.pr.text(data.PR_ACCOUNT_PASSWORD_STRENGTH), data.EM_PR_ACCOUNT_PASSWROD_STRENGTH_WEAK)
        self.assertFalse(self.pr.focus(data.PR_ACCOUNT_SAVE_ALL_BUTTON).is_enabled())
        # Reset password
        self.pr.clear(data.PR_ACCOUNT_CONFIRM_PASSWORD)
        self.pr.enter(PASSWORD, data.PR_ACCOUNT_CONFIRM_PASSWORD)
        self.assertTrue(self.pr.focus(data.PR_ACCOUNT_SAVE_ALL_BUTTON).is_enabled())
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.logout()
        
    def test_urgent_update_cell_number(self):
        # This test is for '107007 Change cell phone'
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.select('91', data.PR_ACCOUNT_COUNTRY_CODE)
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter('1234567890', data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        # Validation check for US number
        self.number_validation_check('1', 10)
        # Validation check for India number
        self.number_validation_check('91', 10)
        # Validation check for HK number
        self.number_validation_check('852', 8)
        # Validation check for China number
        self.number_validation_check('86', 11)
        
        # Save for number change
        self.pr.select('91', data.PR_ACCOUNT_COUNTRY_CODE)
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter('1234567890', data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        
        
if __name__ == '__main__':
    unittest.main()