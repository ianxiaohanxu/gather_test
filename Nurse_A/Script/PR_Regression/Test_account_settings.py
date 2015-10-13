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
from Nurse_A.Settings import keycode, constant, data, setup
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case

class Account_settings(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        self.demo = setup.demo_data
        
    def tearDown(self):
        # self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
        
    def number_validation_check_on_account_settings(self):
        self.pr.number_validation_check(
                data.CH_COUNTRY_CODE, 11, data.PR_ACCOUNT_COUNTRY_CODE, 
                data.PR_ACCOUNT_CELL_NUMBER, data.PR_ACCOUNT_CELL_ERROR, 
                data.PR_ACCOUNT_SAVE_ALL_BUTTON, data.PR_ACCOUNT_SEND_SMS_BUTTON
                )
        self.pr.number_validation_check(
                data.US_COUNTRY_CODE, 10, data.PR_ACCOUNT_COUNTRY_CODE, 
                data.PR_ACCOUNT_CELL_NUMBER, data.PR_ACCOUNT_CELL_ERROR, 
                data.PR_ACCOUNT_SAVE_ALL_BUTTON, data.PR_ACCOUNT_SEND_SMS_BUTTON
                )
        self.pr.number_validation_check(
                data.HK_COUNTRY_CODE, 8, data.PR_ACCOUNT_COUNTRY_CODE, 
                data.PR_ACCOUNT_CELL_NUMBER, data.PR_ACCOUNT_CELL_ERROR, 
                data.PR_ACCOUNT_SAVE_ALL_BUTTON, data.PR_ACCOUNT_SEND_SMS_BUTTON
                )
        self.pr.number_validation_check(
                data.IN_COUNTRY_CODE, 10, data.PR_ACCOUNT_COUNTRY_CODE, 
                data.PR_ACCOUNT_CELL_NUMBER, data.PR_ACCOUNT_CELL_ERROR, 
                data.PR_ACCOUNT_SAVE_ALL_BUTTON, data.PR_ACCOUNT_SEND_SMS_BUTTON
                )
        
    def test_urgent_reset_password(self):
        '''
        107009
        This test is for '107009 Reset password'
        '''
        PASSWORD = '234567'
        LESS_PASSWORD = '12345'
        WRONG_PASSWORD = '345678'
        # self.demo = self.pr.generate_test_demo()
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
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_TITLE)
        self.pr.select('91', data.PR_ACCOUNT_COUNTRY_CODE)
        self.pr.clear(data.PR_ACCOUNT_CELL_NUMBER)
        self.pr.enter('1234567890', data.PR_ACCOUNT_CELL_NUMBER)
        self.number_validation_check_on_account_settings()
        
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
        # self.demo = self.pr.generate_test_demo()
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
        # self.demo = self.pr.generate_test_demo()
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
        107016
        This test is for '107016 Patient record data view show Visits by default'
        '''
        # self.demo = self.pr.generate_test_demo()
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
        107001 107003 107004
        This test is for '107001 Update name'
        This test is for '107003 Update birthdate'
        This test is for '107004 Enter birthdate'
        '''
        surname = 'surname'
        given_name = 'given'
        birthday = '1980-01-07'
        # self.demo = self.pr.generate_test_demo()
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
        
    def test_normal_interrupt_edit_account_settings(self):
        '''
        107015
        This test is for '107015 Interrupt editing account settings'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_SURNAME)
        self.pr.clear(data.PR_ACCOUNT_SURNAME)
        self.pr.enter('123', data.PR_ACCOUNT_SURNAME)
        self.pr.driver.get(data.DIRECTORY_PATH)
        Alert(self.pr.driver).accept()
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_ACCOUNT)
        self.pr.verify(data.PR_ACCOUNT_SURNAME)
        self.assertFalse('123' in self.pr.text(data.PR_ACCOUNT_SURNAME))
        self.pr.clear(data.PR_ACCOUNT_SURNAME)
        self.pr.enter('123', data.PR_ACCOUNT_SURNAME)
        self.pr.driver.get(data.DIRECTORY_PATH)
        Alert(self.pr.driver).dismiss()
        self.pr.verify(data.PR_ACCOUNT_SURNAME)
        self.pr.refresh()
        Alert(self.pr.driver).accept()
        
if __name__ == '__main__':
    unittest.main()