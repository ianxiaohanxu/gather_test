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

class Sign_up(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        self.demo = setup.demo_data
        
    def tearDown(self):
        self.pr.teardown()
        
    def enroll_new_staff(self, role='0', admin='true'):
        security_key = self.pr.generate_security_key(data.DOCTOR, self.demo[0])
        random_str = str(int(time()))
        random_name = 'doctor%s' %random_str
        random_email = 'doctor%s@test.com' %random_str
        self.pr.enroll_new_staff(random_name, random_email, self.demo[1], security_key, role=role, is_practice_admin=admin)
        staff_email_list = self.pr.get_staff_invitation_email(security_key)
        new_staff_email = staff_email_list[random_email].replace('HOSTNAME', 'localhost:8000')
        return random_name, random_email, new_staff_email
        
    def number_validation_check_on_practice_contact_page(self):
        self.pr.number_validation_check(
                data.CH_COUNTRY_CODE, 11, data.PR_SIGN_UP_COUNTRY_CODE, 
                data.PR_SIGN_UP_PRACTICE_NUMBER, data.PR_SIGN_UP_PRACTICE_NUMBER_VALIDATION, 
                data.PR_SIGN_UP_NEXT_BUTTON
                )
        self.pr.number_validation_check(
                data.US_COUNTRY_CODE, 10, data.PR_SIGN_UP_COUNTRY_CODE, 
                data.PR_SIGN_UP_PRACTICE_NUMBER, data.PR_SIGN_UP_PRACTICE_NUMBER_VALIDATION, 
                data.PR_SIGN_UP_NEXT_BUTTON
                )
        self.pr.number_validation_check(
                data.HK_COUNTRY_CODE, 8, data.PR_SIGN_UP_COUNTRY_CODE, 
                data.PR_SIGN_UP_PRACTICE_NUMBER, data.PR_SIGN_UP_PRACTICE_NUMBER_VALIDATION, 
                data.PR_SIGN_UP_NEXT_BUTTON
                )
        self.pr.number_validation_check(
                data.IN_COUNTRY_CODE, 10, data.PR_SIGN_UP_COUNTRY_CODE, 
                data.PR_SIGN_UP_PRACTICE_NUMBER, data.PR_SIGN_UP_PRACTICE_NUMBER_VALIDATION, 
                data.PR_SIGN_UP_NEXT_BUTTON
                )
                
    def number_validation_check_on_add_phone_page(self):
        self.pr.number_validation_check(
                data.CH_COUNTRY_CODE, 11, data.PR_SIGN_UP_COUNTRY_CODE, 
                data.PR_SIGN_UP_CELL_NUMBER, data.PR_SIGN_UP_CELL_NUMBER_VALIDATION, 
                data.PR_SIGN_UP_NEXT_BUTTON, data.PR_SIGN_UP_VERIFY_SEND_BUTTON
                )
        self.pr.number_validation_check(
                data.US_COUNTRY_CODE, 10, data.PR_SIGN_UP_COUNTRY_CODE, 
                data.PR_SIGN_UP_CELL_NUMBER, data.PR_SIGN_UP_CELL_NUMBER_VALIDATION, 
                data.PR_SIGN_UP_NEXT_BUTTON, data.PR_SIGN_UP_VERIFY_SEND_BUTTON
                )
        self.pr.number_validation_check(
                data.HK_COUNTRY_CODE, 8, data.PR_SIGN_UP_COUNTRY_CODE, 
                data.PR_SIGN_UP_CELL_NUMBER, data.PR_SIGN_UP_CELL_NUMBER_VALIDATION, 
                data.PR_SIGN_UP_NEXT_BUTTON, data.PR_SIGN_UP_VERIFY_SEND_BUTTON
                )
        self.pr.number_validation_check(
                data.IN_COUNTRY_CODE, 10, data.PR_SIGN_UP_COUNTRY_CODE, 
                data.PR_SIGN_UP_CELL_NUMBER, data.PR_SIGN_UP_CELL_NUMBER_VALIDATION, 
                data.PR_SIGN_UP_NEXT_BUTTON, data.PR_SIGN_UP_VERIFY_SEND_BUTTON
                )

        
    def test_urgent_invite_a_new_staff(self):
        '''
        104017 104019 104011 104005
        This test is for '104017 Invite a new staff'
        This test is for '104019 Change practice phone number during practice administrator sign up'
        This test is for '104011 Check the "NEXT" button in add address page'
        This test is for '104005 The confirm password doesn't match the password'
        '''
        new_staff = self.enroll_new_staff()
        self.pr.driver.get(new_staff[2])
        self.pr.verify(data.PR_SIGN_UP_STEP_LINE)
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP), data.SIGN_UP_CONFIRM_INFO)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        
        ## Confirm info page
        # Validation check for 'Last name' field
        self.pr.clear(data.PR_SIGN_UP_LAST_NAME)
        self.assertTrue(self.pr.is_element_present(data.PR_SIGN_UP_LAST_NAME_VALIDATION))
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_LAST_NAME_VALIDATION), data.EM_SIGN_UP_REQUIRED)
        self.assertEqual(self.pr.focus(data.PR_SIGN_UP_LAST_NAME).get_attribute('data-validate-status'), 'invalid')
        self.pr.enter(new_staff[0], data.PR_SIGN_UP_LAST_NAME)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        
        # Validation check for 'First name' field
        self.pr.enter('doctor', data.PR_SIGN_UP_FIRST_NAME)
        self.pr.clear(data.PR_SIGN_UP_FIRST_NAME)
        self.assertTrue(self.pr.is_element_present(data.PR_SIGN_UP_FIRST_NAME_VALIDATION))
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_FIRST_NAME_VALIDATION), data.EM_SIGN_UP_REQUIRED)
        self.assertEqual(self.pr.focus(data.PR_SIGN_UP_FIRST_NAME).get_attribute('data-validate-status'), 'invalid')
        self.pr.enter('doctor', data.PR_SIGN_UP_FIRST_NAME)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        
        # Validation check for 'Doctor registration number' field
        self.pr.enter(new_staff[0], data.PR_SIGN_UP_DOCTOR_ID)
        self.pr.clear(data.PR_SIGN_UP_DOCTOR_ID)
        self.assertTrue(self.pr.is_element_present(data.PR_SIGN_UP_DOCTOR_ID_VALIDATION))
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_DOCTOR_ID_VALIDATION), data.EM_SIGN_UP_REQUIRED)
        self.assertEqual(self.pr.focus(data.PR_SIGN_UP_DOCTOR_ID).get_attribute('data-validate-status'), 'invalid')
        self.pr.enter(new_staff[0], data.PR_SIGN_UP_DOCTOR_ID)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        
        self.pr.select(data.ENGLISH, data.PR_SIGN_UP_DEFAULT_LANG)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        
        # Validation check for 'Password' field
        self.pr.enter('12345', data.PR_SIGN_UP_PASSWORD)
        self.pr.click(data.PR_SIGN_UP_PASSWORD_CONFIRM)
        self.assertTrue(self.pr.is_element_present(data.PR_SIGN_UP_PASSWORD_VALIDATION))
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_PASSWORD_VALIDATION), data.EM_SIGN_UP_PASSWORD_LENGH)
        self.assertEqual(self.pr.focus(data.PR_SIGN_UP_PASSWORD).get_attribute('data-validate-status'), 'invalid')
        self.pr.enter('6', data.PR_SIGN_UP_PASSWORD)
        self.pr.click(data.PR_SIGN_UP_PASSWORD_CONFIRM)
        self.assertFalse(self.pr.is_element_present(data.PR_SIGN_UP_PASSWORD_VALIDATION))
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        
        # Validation check for 'Confirm password' field
        self.pr.enter('12345', data.PR_SIGN_UP_PASSWORD_CONFIRM)
        self.pr.click(data.PR_SIGN_UP_PASSWORD)
        self.assertTrue(self.pr.is_element_present(data.PR_SIGN_UP_PASSWORD_CONFIRM_VALIDATION))
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_PASSWORD_CONFIRM_VALIDATION), data.EM_SIGN_UP_PASSWORD_MATCH)
        self.assertEqual(self.pr.focus(data.PR_SIGN_UP_PASSWORD_CONFIRM).get_attribute('data-validate-status'), 'invalid')
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.enter('6', data.PR_SIGN_UP_PASSWORD_CONFIRM)
        self.assertFalse(self.pr.is_element_present(data.PR_SIGN_UP_PASSWORD_CONFIRM_VALIDATION))
        
        ## Sign agreement page
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_SIGN_AGREEMENT)
        self.pr.click(data.PR_SIGN_UP_ACCEPT_CHECKBOX)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.enter('111', data.PR_SIGN_UP_SIGNATURE)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.assertTrue(self.pr.is_element_present(data.PR_SIGN_UP_SIGNATURE_ERROR))
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_SIGNATURE_ERROR), data.EM_SIGN_UP_SIGNATURE_SERVER_ERROR)
        self.pr.clear(data.PR_SIGN_UP_SIGNATURE)
        self.pr.enter('abc', data.PR_SIGN_UP_SIGNATURE)
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        
        ## Practice contact page
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_PRACTICE_CONTACT)
        self.pr.clear(data.PR_SIGN_UP_PRACTICE_NUMBER)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        
        # Validation check for practice number
        self.number_validation_check_on_practice_contact_page()
        
        ## Upload photo page
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_UPLOAD_PHOTO)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        
        ## Add phone page
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_ADD_PHONE)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.enter('1234567890', data.PR_SIGN_UP_CELL_NUMBER)
        
        # Validation check for cell number on 'Add phone' page
        self.number_validation_check_on_add_phone_page()
        
        ## Invite staff page
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_INVITE_STAFF)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_NEXT_BUTTON), 'FINISH')
        self.pr.enter('abc', data.PR_SIGN_UP_STAFF_NAME)
        self.pr.enter('abc', data.PR_SIGN_UP_STAFF_EMAIL)
        self.pr.click(data.PR_SIGN_UP_STAFF_INVITE_BUTTON)
        self.pr.verify(data.PR_SIGN_UP_STAFF_INVITE_ERROR)
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_STAFF_INVITE_ERROR), data.EM_SIGN_UP_INVITE_SHORT_ERROR)
        self.pr.select('0', data.PR_SIGN_UP_STAFF_ROLE)
        self.pr.click(data.PR_SIGN_UP_STAFF_INVITE_BUTTON)
        self.pr.verify(data.PR_SIGN_UP_STAFF_INVITE_ERROR)
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_STAFF_INVITE_ERROR), data.EM_SIGN_UP_INVALID_EMAIL)
        self.pr.clear(data.PR_SIGN_UP_STAFF_NAME)
        self.pr.click(data.PR_SIGN_UP_STAFF_INVITE_BUTTON)
        self.pr.verify(data.PR_SIGN_UP_STAFF_INVITE_ERROR)
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_STAFF_INVITE_ERROR), data.EM_SIGN_UP_INVITE_LONG_ERROR)
        self.pr.enter('abc', data.PR_SIGN_UP_STAFF_NAME)
        self.pr.clear(data.PR_SIGN_UP_STAFF_EMAIL)
        self.pr.click(data.PR_SIGN_UP_STAFF_INVITE_BUTTON)
        self.pr.verify(data.PR_SIGN_UP_STAFF_INVITE_ERROR)
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_STAFF_INVITE_ERROR), data.EM_SIGN_UP_INVITE_LONG_ERROR)
        self.pr.enter('abc%s@test.com' %str(int(time())), data.PR_SIGN_UP_STAFF_EMAIL)
        self.pr.click(data.PR_SIGN_UP_STAFF_INVITE_BUTTON)
        self.pr.wait_until_not_present(data.PR_SIGN_UP_STAFF_INVITE_ERROR)
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.verify(data.PR_TUTORIAL_WELCOME)
        
    def test_normal_not_invite_a_new_staff(self):
        '''
        104018
        This test is for '104018 Don't invite new staff'
        '''
        new_staff = self.enroll_new_staff()
        self.pr.driver.get(new_staff[2])
        self.pr.verify(data.PR_SIGN_UP_STEP_LINE)
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP), data.SIGN_UP_CONFIRM_INFO)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.enter('doctor', data.PR_SIGN_UP_FIRST_NAME)
        self.pr.enter(new_staff[0], data.PR_SIGN_UP_DOCTOR_ID)
        self.pr.select(data.ENGLISH, data.PR_SIGN_UP_DEFAULT_LANG)
        self.pr.enter('123456', data.PR_SIGN_UP_PASSWORD)
        self.pr.enter('123456', data.PR_SIGN_UP_PASSWORD_CONFIRM)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_SIGN_AGREEMENT)
        self.pr.click(data.PR_SIGN_UP_ACCEPT_CHECKBOX)
        self.pr.enter('abc', data.PR_SIGN_UP_SIGNATURE)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_PRACTICE_CONTACT)
        self.pr.clear(data.PR_SIGN_UP_PRACTICE_NUMBER)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_SIGN_UP_COUNTRY_CODE)
        self.pr.enter('1234565432', data.PR_SIGN_UP_PRACTICE_NUMBER)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_UPLOAD_PHOTO)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_ADD_PHONE)
        self.pr.clear(data.PR_SIGN_UP_CELL_NUMBER)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_SIGN_UP_COUNTRY_CODE)
        self.pr.enter('1234554321', data.PR_SIGN_UP_CELL_NUMBER)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_INVITE_STAFF)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_NEXT_BUTTON), 'FINISH')
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.verify(data.PR_TUTORIAL_WELCOME)
        
    def test_normal_invite_non_admin_staff(self):
        '''
        104004
        This test is for '104004 Confirm basic info in confirm info page'
        '''
        new_staff = self.enroll_new_staff(role='3', admin='false')
        self.pr.driver.get(new_staff[2])
        self.pr.verify(data.PR_SIGN_UP_STEP_LINE)
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP), data.SIGN_UP_CONFIRM_INFO)
        self.assertFalse(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.assertFalse(self.pr.is_element_present(data.PR_SIGN_UP_DOCTOR_ID))
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_LAST_NAME), new_staff[0].replace('d', 'D'))
        self.pr.enter('doctor', data.PR_SIGN_UP_FIRST_NAME)
        self.pr.select(data.ENGLISH, data.PR_SIGN_UP_DEFAULT_LANG)
        self.pr.enter('123456', data.PR_SIGN_UP_PASSWORD)
        self.pr.enter('123456', data.PR_SIGN_UP_PASSWORD_CONFIRM)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_SIGN_AGREEMENT)
        self.pr.click(data.PR_SIGN_UP_ACCEPT_CHECKBOX)
        self.pr.enter('abc', data.PR_SIGN_UP_SIGNATURE)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_UPLOAD_PHOTO)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.wait_until(lambda: self.pr.text(data.PR_SIGN_UP_ACTIVE_STEP)==data.SIGN_UP_ADD_PHONE)
        self.pr.clear(data.PR_SIGN_UP_CELL_NUMBER)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_SIGN_UP_COUNTRY_CODE)
        self.pr.enter('1234554321', data.PR_SIGN_UP_CELL_NUMBER)
        self.assertTrue(self.pr.focus(data.PR_SIGN_UP_NEXT_BUTTON).is_enabled())
        self.assertEqual(self.pr.text(data.PR_SIGN_UP_NEXT_BUTTON), 'NEXT')
        self.pr.click(data.PR_SIGN_UP_NEXT_BUTTON)
        self.pr.verify(data.PR_TUTORIAL_WELCOME)
        
if __name__ == '__main__':
    unittest.main()
