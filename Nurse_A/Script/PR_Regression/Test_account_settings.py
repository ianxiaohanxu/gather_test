#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
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
        self.pr.driver.maximize_window()
        
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
        '''
        107009
        This test is for '107009 Reset password'
        '''
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
        '''
        107007
        This test is for '107007 Change cell phone'
        '''
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
        
    def test_normal_show_bg_data(self):
        '''
        107014
        This test is for '107014 Patient record data view show BG data'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_SHOW_BG)
        self.pr.click(data.PR_ACCOUNT_SHOW_BG)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ACCOUNT_COUNTRY_CODE)
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter('1234567890', data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        sleep(constant.INTERVAL_10)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.click(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.verify(data.PR_PATIENT_RECORD_BG_DIV)
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_SHOW_BG)
        self.assertTrue(self.pr.focus(data.PR_ACCOUNT_SHOW_BG).is_selected())
        
    def test_normal_show_summary(self):
        '''
        107013
        This test is for '107013 Patient record data view show summary'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_SHOW_SUMMARY)
        self.pr.click(data.PR_ACCOUNT_SHOW_SUMMARY)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ACCOUNT_COUNTRY_CODE)
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter('1234567890', data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        sleep(constant.INTERVAL_10)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.click(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.verify(data.PR_PATIENT_RECORD_SUMMARY_DIV)
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_SHOW_SUMMARY)
        self.assertTrue(self.pr.focus(data.PR_ACCOUNT_SHOW_SUMMARY).is_selected())
        
    def test_normal_show_visit(self):
        '''
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_SHOW_VISIT)
        self.pr.click(data.PR_ACCOUNT_SHOW_VISIT)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ACCOUNT_COUNTRY_CODE)
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter('1234567890', data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        sleep(constant.INTERVAL_10)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.click(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_CONTENT)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_HEIGHT)
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_SHOW_VISIT)
        self.assertTrue(self.pr.focus(data.PR_ACCOUNT_SHOW_VISIT).is_selected())
        
    def test_normal_update_name_and_birthday(self):
        '''
        107001 107003
        This test is for '107001 Update name'
        This test is for '107003 Update birthdate'
        '''
        surname = 'surname'
        given_name = 'given'
        birthday = '1980-01-07'
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_SURNAME)
        self.pr.clear(data.PR_ACCOUNT_SURNAME)
        self.pr.enter(surname, data.PR_ACCOUNT_SURNAME)
        self.pr.clear(data.PR_ACCOUNT_GIVEN_NAME)
        self.pr.enter(given_name, data.PR_ACCOUNT_GIVEN_NAME)
        self.pr.driver.execute_script('document.getElementsByName("dob")[0].value="%s"' %birthday)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ACCOUNT_COUNTRY_CODE)
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter('1234567890', data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        sleep(constant.INTERVAL_10)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.refresh()
        self.pr.verify(data.PR_ACCOUNT_SURNAME)
        self.assertEqual(surname, self.pr.text(data.PR_ACCOUNT_SURNAME))
        self.assertEqual(given_name, self.pr.text(data.PR_ACCOUNT_GIVEN_NAME))
        self.assertEqual(birthday, self.pr.text(data.PR_ACCOUNT_BIRTHDATE))
        
    def test_normal_update_language(self):
        '''
        107002
        This test is for '107002 Change Language'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_LANGUAGE)
        # Update language to Traditional Chinese
        self.pr.select(data.TRADITIONAL_CHINESE, data.PR_ACCOUNT_LANGUAGE)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ACCOUNT_COUNTRY_CODE)
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter('1234567890', data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        sleep(constant.INTERVAL_10)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.refresh()
        self.pr.verify(data.PR_ACCOUNT_LANGUAGE)
        self.assertEqual(data.ACCOUNT_HK.decode('utf-8'), self.pr.text(data.PR_ACCOUNT_TITLE))
        self.assertEqual(data.TRADITIONAL_CHINESE, self.pr.text(data.PR_ACCOUNT_LANGUAGE))
        # Update language to Indian
        self.pr.select(data.INDIAN, data.PR_ACCOUNT_LANGUAGE)
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        sleep(constant.INTERVAL_10)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.refresh()
        self.pr.verify(data.PR_ACCOUNT_LANGUAGE)
        self.assertEqual(data.ACCOUNT_IN.decode('utf-8'), self.pr.text(data.PR_ACCOUNT_TITLE))
        self.assertEqual(data.INDIAN, self.pr.text(data.PR_ACCOUNT_LANGUAGE))
        # Update language to English
        self.pr.select(data.ENGLISH, data.PR_ACCOUNT_LANGUAGE)
        self.pr.click(data.PR_ACCOUNT_SAVE_ALL_BUTTON)
        sleep(constant.INTERVAL_10)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.refresh()
        self.pr.verify(data.PR_ACCOUNT_LANGUAGE)
        self.assertEqual(data.ACCOUNT_US.decode('utf-8'), self.pr.text(data.PR_ACCOUNT_TITLE))
        self.assertEqual(data.ENGLISH, self.pr.text(data.PR_ACCOUNT_LANGUAGE))
        
if __name__ == '__main__':
    unittest.main()