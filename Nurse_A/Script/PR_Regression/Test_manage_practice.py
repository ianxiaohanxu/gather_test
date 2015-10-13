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

class Manage_practice(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        self.demo = setup.demo_data
        
    def tearDown(self):
        # self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
        
    def verify_bg_unit(self, unit):
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.click(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.verify(data.PR_PATIENT_RECORD_PRE_MEAL_BG_UNIT)
        # Verify BG unit on BG goals area
        self.assertTrue(unit in self.pr.text(data.PR_PATIENT_RECORD_PRE_MEAL_BG_UNIT))
        self.assertTrue(unit in self.pr.text(data.PR_PATIENT_RECORD_POST_MEAL_BG_UNIT))
        # Verify BG unit on Summary graph Y label
        self.pr.click(data.PR_PATIENT_RECORD_SUMMARY_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_SUMMARY_BG_Y_LABEL)
        self.assertTrue(unit in self.pr.text(data.PR_PATIENT_RECORD_SUMMARY_BG_Y_LABEL))
        # Verify BG unit on BG table
        
        # Verify BG unit on Visits page
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_NEW_BUTTON)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_NEW_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_FASTING_BG_UNIT)
        self.assertTrue(unit in self.pr.text(data.PR_PATIENT_RECORD_VISIT_FASTING_BG_UNIT))
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_POST_BG_UNIT)
        self.assertTrue(unit in self.pr.text(data.PR_PATIENT_RECORD_VISIT_POST_BG_UNIT))
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_RANDOM_BG_UNIT)
        self.assertTrue(unit in self.pr.text(data.PR_PATIENT_RECORD_VISIT_RANDOM_BG_UNIT))
        # Verify BG unit on Manage Practice page
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_FIRST_PRACTICE)
        self.pr.verify(data.PR_MANAGE_PRACTICE_TITLE)
    
    def number_validation_check_on_manage_practice(self):
        self.pr.number_validation_check(
                data.US_COUNTRY_CODE, 10, data.PR_MANAGE_PRACTICE_COUNTRY_CODE, 
                data.PR_MANAGE_PRACTICE_NUMBER, data.PR_MANAGE_PRACTICE_NUMBER_ERROR, 
                data.PR_MANAGE_PRACTICE_SAVE_BUTTON
                )
        self.pr.number_validation_check(
                data.CH_COUNTRY_CODE, 11, data.PR_MANAGE_PRACTICE_COUNTRY_CODE, 
                data.PR_MANAGE_PRACTICE_NUMBER, data.PR_MANAGE_PRACTICE_NUMBER_ERROR, 
                data.PR_MANAGE_PRACTICE_SAVE_BUTTON
                )
        self.pr.number_validation_check(
                data.HK_COUNTRY_CODE, 8, data.PR_MANAGE_PRACTICE_COUNTRY_CODE, 
                data.PR_MANAGE_PRACTICE_NUMBER, data.PR_MANAGE_PRACTICE_NUMBER_ERROR, 
                data.PR_MANAGE_PRACTICE_SAVE_BUTTON
                )
        self.pr.number_validation_check(
                data.IN_COUNTRY_CODE, 10, data.PR_MANAGE_PRACTICE_COUNTRY_CODE, 
                data.PR_MANAGE_PRACTICE_NUMBER, data.PR_MANAGE_PRACTICE_NUMBER_ERROR, 
                data.PR_MANAGE_PRACTICE_SAVE_BUTTON
                )
        
        
    def test_urgent_update_bg_unit(self):
        '''
        106008
        This test is for '106008 Update BG Units'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_FIRST_PRACTICE)
        self.pr.verify(data.PR_MANAGE_PRACTICE_TITLE)
        # Change BG unit to mmol/L
        self.pr.select(data.MMO_L, data.PR_MANAGE_PRACTICE_BG_UNIT)
        self.pr.click(data.PR_MANAGE_PRACTICE_SAVE_BUTTON)
        self.pr.verify(data.PR_MANAGE_PRACTICE_SAVE_SUCCESS)
        # Verify BG unit updated
        self.pr.verify(data.PR_MANAGE_PRACTICE_CRITICAL_LOW_MMO)
        self.verify_bg_unit('mmol/L')
        self.assertTrue(data.MMO_L == self.pr.text(data.PR_MANAGE_PRACTICE_BG_UNIT))
        # Change BG unit to mg/dL
        self.pr.select(data.MG_DL, data.PR_MANAGE_PRACTICE_BG_UNIT)
        self.pr.click(data.PR_MANAGE_PRACTICE_SAVE_BUTTON)
        self.pr.verify(data.PR_MANAGE_PRACTICE_SAVE_SUCCESS)
        # Verify BG unit updated
        self.pr.verify(data.PR_MANAGE_PRACTICE_CRITICAL_UPPER_MG)
        self.verify_bg_unit('mg/dL')
        self.assertTrue(data.MG_DL == self.pr.text(data.PR_MANAGE_PRACTICE_BG_UNIT))
        
    def test_urgent_update_critical_bg_range(self):
        '''
        106009
        This test is for '106009 Update Critical range'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_FIRST_PRACTICE)
        self.pr.verify(data.PR_MANAGE_PRACTICE_TITLE)
        # Update critical BG range with unit mg/dL
        self.pr.select(data.MG_DL, data.PR_MANAGE_PRACTICE_BG_UNIT)
        self.pr.verify(data.PR_MANAGE_PRACTICE_CRITICAL_UPPER_MG)
        self.pr.select('90', data.PR_MANAGE_PRACTICE_CRITICAL_LOW_MG)
        self.pr.select('300', data.PR_MANAGE_PRACTICE_CRITICAL_UPPER_MG)
        self.pr.click(data.PR_MANAGE_PRACTICE_SAVE_BUTTON)
        self.pr.verify(data.PR_MANAGE_PRACTICE_SAVE_SUCCESS)
        self.assertTrue('90' in self.pr.text(data.PR_MANAGE_PRACTICE_CRITICAL_LOW_MG))
        self.assertTrue('300' in self.pr.text(data.PR_MANAGE_PRACTICE_CRITICAL_UPPER_MG))
        # Update critical BG range with unit mmol/L
        self.pr.select(data.MMO_L, data.PR_MANAGE_PRACTICE_BG_UNIT)
        self.pr.verify(data.PR_MANAGE_PRACTICE_CRITICAL_LOW_MMO)
        self.pr.select('3.0', data.PR_MANAGE_PRACTICE_CRITICAL_LOW_MMO)
        self.pr.select('20.0', data.PR_MANAGE_PRACTICE_CRITICAL_UPPER_MMO)
        self.pr.click(data.PR_MANAGE_PRACTICE_SAVE_BUTTON)
        self.pr.verify(data.PR_MANAGE_PRACTICE_SAVE_SUCCESS)
        self.assertTrue('3.0' in self.pr.text(data.PR_MANAGE_PRACTICE_CRITICAL_LOW_MMO))
        self.assertTrue('20.0' in self.pr.text(data.PR_MANAGE_PRACTICE_CRITICAL_UPPER_MMO))
        
    def test_urgent_update_practice_number(self):
        '''
        106011 106012
        This test is for '106011 Update practice phone'
        This test is for '106012 Practice phone number validation check'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_FIRST_PRACTICE)
        self.pr.verify(data.PR_MANAGE_PRACTICE_TITLE)
        self.number_validation_check_on_manage_practice()
        self.pr.click(data.PR_MANAGE_PRACTICE_SAVE_BUTTON)
        self.pr.verify(data.PR_MANAGE_PRACTICE_SAVE_SUCCESS)
        
    def test_normal_interrupt_edit_practice_settings(self):
        '''
        106010
        This test is for '106010 Interrupt edit practice settings'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_FIRST_PRACTICE)
        self.pr.verify(data.PR_MANAGE_PRACTICE_TITLE)
        # Get original data
        original_name = self.pr.text(data.PR_MANAGE_PRACTICE_PRACTICE_NAME)
        original_height_unit = self.pr.text(data.PR_MANAGE_PRACTICE_HEIGHT_UNIT)
        original_weight_unit = self.pr.text(data.PR_MANAGE_PRACTICE_WEIGHT_UNIT)
        original_bp_unit = self.pr.text(data.PR_MANAGE_PRACTICE_BP_UNIT)
        original_bg_unit = self.pr.text(data.PR_MANAGE_PRACTICE_BG_UNIT)
        original_bg_low =   self.pr.text(data.PR_MANAGE_PRACTICE_CRITICAL_LOW_MG)
        original_bg_upper = self.pr.text(data.PR_MANAGE_PRACTICE_CRITICAL_UPPER_MG)
        original_country_code = self.pr.text(data.PR_MANAGE_PRACTICE_COUNTRY_CODE)
        original_number = self.pr.text(data.PR_MANAGE_PRACTICE_NUMBER)
        original_group_unit = self.pr.text(data.PR_MANAGE_PRACTICE_UNIT_GROUP)
        # Input new data
        self.pr.clear(data.PR_MANAGE_PRACTICE_PRACTICE_NAME)
        self.pr.enter('abc', data.PR_MANAGE_PRACTICE_PRACTICE_NAME)
        self.pr.select('1', data.PR_MANAGE_PRACTICE_HEIGHT_UNIT)
        self.pr.select('1', data.PR_MANAGE_PRACTICE_WEIGHT_UNIT)
        self.pr.select('1', data.PR_MANAGE_PRACTICE_BP_UNIT)
        self.pr.select('1', data.PR_MANAGE_PRACTICE_BG_UNIT)
        self.pr.select('1', data.PR_MANAGE_PRACTICE_COUNTRY_CODE)
        self.pr.clear(data.PR_MANAGE_PRACTICE_NUMBER)
        self.pr.enter('1234567890', data.PR_MANAGE_PRACTICE_NUMBER)
        self.pr.select('1128', data.PR_MANAGE_PRACTICE_UNIT_GROUP)
        self.pr.driver.get(data.DIRECTORY_PATH)
        try:
            Alert(self.pr.driver).accept()
        except:
            pass
        self.pr.verify(data.PR_DIRECTORY_TITLE)
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_FIRST_PRACTICE)
        self.pr.verify(data.PR_MANAGE_PRACTICE_TITLE)
        self.assertEqual(original_name, self.pr.text(data.PR_MANAGE_PRACTICE_PRACTICE_NAME))
        self.assertEqual(original_height_unit, self.pr.text(data.PR_MANAGE_PRACTICE_HEIGHT_UNIT))
        self.assertEqual(original_weight_unit, self.pr.text(data.PR_MANAGE_PRACTICE_WEIGHT_UNIT))
        self.assertEqual(original_bp_unit, self.pr.text(data.PR_MANAGE_PRACTICE_BP_UNIT))
        self.assertEqual(original_bg_unit, self.pr.text(data.PR_MANAGE_PRACTICE_BG_UNIT))
        self.assertEqual(original_bg_low, self.pr.text(data.PR_MANAGE_PRACTICE_CRITICAL_LOW_MG))
        self.assertEqual(original_bg_upper, self.pr.text(data.PR_MANAGE_PRACTICE_CRITICAL_UPPER_MG))
        self.assertEqual(original_country_code, self.pr.text(data.PR_MANAGE_PRACTICE_COUNTRY_CODE))
        self.assertEqual(original_number, self.pr.text(data.PR_MANAGE_PRACTICE_NUMBER))
        self.assertEqual(original_group_unit, self.pr.text(data.PR_MANAGE_PRACTICE_UNIT_GROUP))
        
    def test_urgent_invite_another_practice_staff(self):
        '''
        106014
        This test is for '106014 Invite an another practice's staff to the practice'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_FIRST_PRACTICE)
        self.pr.verify(data.PR_MANAGE_PRACTICE_TITLE)
        self.pr.verify(data.PR_MANAGE_PRACTICE_STAFF_ENTRY)
        ORIGINAL_STAFF_COUNT =  len(self.pr.find(data.PR_MANAGE_PRACTICE_STAFF_ENTRY))
        self.pr.verify(data.PR_MANAGE_PRACTICE_ADD_STAFF_BUTTON)
        self.pr.click(data.PR_MANAGE_PRACTICE_ADD_STAFF_BUTTON)
        self.pr.verify(data.PR_MANAGE_PRACTICE_INVITE_STAFF_DIALOG)
        self.pr.enter('doctor_fake', data.PR_MANAGE_PRACTICE_INVITE_STAFF_NAME)
        self.pr.enter(setup.doctor_account_demo2, data.PR_MANAGE_PRACTICE_INVITE_STAFF_EMAIL)
        self.pr.select('0', data.PR_MANAGE_PRACTICE_INVITE_STAFF_ROLE)
        self.pr.select(data.ENGLISH, data.PR_MANAGE_PRACTICE_INVITE_STAFF_LANG)
        self.pr.select('true', data.PR_MANAGE_PRACTICE_INVITE_STAFF_RIGHT)
        self.pr.click(data.PR_MANAGE_PRACTICE_INVITE_STAFF_SUBMIT)
        self.pr.verify(data.PR_MANAGE_PRACTICE_STAFF_ENTRY)
        NOW_STAFF_COUNT =  len(self.pr.find(data.PR_MANAGE_PRACTICE_STAFF_ENTRY))
        self.assertEqual(ORIGINAL_STAFF_COUNT+1, NOW_STAFF_COUNT)
        self.pr.logout()
        self.pr.login(data.DOCTOR, setup.demo_data2[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        PRACTICE_LIST = self.pr.find(data.PR_NAV_OPTION_MENU_PRACTICE)
        self.assertEqual(len(PRACTICE_LIST), 2)
        
    def test_urgent_open_manage_practice(self):
        '''
        106013
        This test is for '106013 Open manage practice page'
        '''
        self.demo = setup.demo_data1
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        PRACTICE_LIST = self.pr.find(data.PR_NAV_OPTION_MENU_PRACTICE)
        self.assertEqual(len(PRACTICE_LIST), 2)
        PRACTICE_LIST[0].click()
        self.pr.verify(data.PR_MANAGE_PRACTICE_YELLOW_AREA)
        self.pr.click(data.PR_NAV_OPTION_MENU)
        PRACTICE_LIST = self.pr.find(data.PR_NAV_OPTION_MENU_PRACTICE)
        PRACTICE_LIST[1].click()
        self.pr.verify(data.PR_MANAGE_PRACTICE_YELLOW_AREA)
        
    def test_normal_change_practice_name(self):
        '''
        106004
        This test is for '106004 Change Practice Name'
        '''
        self.demo = setup.demo_data1
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_OPTION_MENU)
        self.pr.click(data.PR_NAV_OPTION_MENU_FIRST_PRACTICE)
        self.pr.verify(data.PR_MANAGE_PRACTICE_PRACTICE_NAME)
        self.pr.clear(data.PR_MANAGE_PRACTICE_PRACTICE_NAME)
        NEW_NAME = 'New_name%s' % str(int(time()))
        self.pr.enter(NEW_NAME, data.PR_MANAGE_PRACTICE_PRACTICE_NAME)
        self.pr.click(data.PR_MANAGE_PRACTICE_SAVE_BUTTON)
        self.pr.verify(data.PR_MANAGE_PRACTICE_SAVE_SUCCESS)
        self.pr.refresh()
        self.pr.verify(data.PR_MANAGE_PRACTICE_PRACTICE_NAME)
        self.assertTrue(NEW_NAME in self.pr.text(data.PR_MANAGE_PRACTICE_PRACTICE_NAME))
        self.assertTrue(NEW_NAME in self.pr.text(data.PR_MANAGE_PRACTICE_NAME_IN_YELLOW))
        self.pr.click(data.PR_NAV_OPTION_MENU)
        PRACTICE_LIST = self.pr.find(data.PR_NAV_OPTION_MENU_PRACTICE)
        for PRACTICE in PRACTICE_LIST:
            if 'New_name' in PRACTICE.text:
                continue
            else:
                PRACTICE.click()
                break
        self.pr.verify(data.PR_MANAGE_PRACTICE_PRACTICE_NAME)
        self.assertFalse(NEW_NAME in self.pr.text(data.PR_MANAGE_PRACTICE_PRACTICE_NAME))
        self.assertFalse(NEW_NAME in self.pr.text(data.PR_MANAGE_PRACTICE_NAME_IN_YELLOW))
        
if __name__ == '__main__':
    unittest.main()