#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
from time import sleep, time
import unittest, datetime
from Nurse_A.Settings import keycode, constant, data, setup
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case

class Patient_directory(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        self.demo = setup.demo_data
        
    def tearDown(self):
        self.pr.teardown()
        
    def number_validation_check_on_group_sms(self):
        self.pr.number_validation_check(
                data.US_COUNTRY_CODE, 10, data.PR_DIRECTORY_GROUP_SMS_COUTRY_CODE, 
                data.PR_DIRECTORY_GROUP_SMS_CELL_NUMBER, data.PR_DIRECTORY_GROUP_SMS_CELL_VALIDATION, 
                data.PR_DIRECTORY_GROUP_SMS_SEND
                )
        self.pr.number_validation_check(
                data.CH_COUNTRY_CODE, 11, data.PR_DIRECTORY_GROUP_SMS_COUTRY_CODE, 
                data.PR_DIRECTORY_GROUP_SMS_CELL_NUMBER, data.PR_DIRECTORY_GROUP_SMS_CELL_VALIDATION, 
                data.PR_DIRECTORY_GROUP_SMS_SEND
                )
        self.pr.number_validation_check(
                data.HK_COUNTRY_CODE, 8, data.PR_DIRECTORY_GROUP_SMS_COUTRY_CODE, 
                data.PR_DIRECTORY_GROUP_SMS_CELL_NUMBER, data.PR_DIRECTORY_GROUP_SMS_CELL_VALIDATION, 
                data.PR_DIRECTORY_GROUP_SMS_SEND
                )
        self.pr.number_validation_check(
                data.IN_COUNTRY_CODE, 10, data.PR_DIRECTORY_GROUP_SMS_COUTRY_CODE, 
                data.PR_DIRECTORY_GROUP_SMS_CELL_NUMBER, data.PR_DIRECTORY_GROUP_SMS_CELL_VALIDATION, 
                data.PR_DIRECTORY_GROUP_SMS_SEND
                )
        
    def test_urgent_compose_sms_to_all(self):
        '''
        109304
        This test is for '109304 Compose SMS to all patient'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.click(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        sms_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_SMS_NUMBER))
        app_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_APP_NUMBER))
        total_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_TOTAL_NUMBER))
        self.assertEqual(total_counter, sms_counter+app_counter)
        self.pr.enter('Hello!', data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        if self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX).is_selected():
            self.pr.click(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX)
        self.assertTrue(self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_SEND).is_enabled())
        self.pr.click(data.PR_DIRECTORY_GROUP_SMS_SEND)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_RESULT_DIALOG)
        # self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_RESULT_TITLE_SUCCESS)
        # self.assertEqual(data.MES_GROUP_SMS_SUCCESS, self.pr.text(data.PR_DIRECTORY_GROUP_SMS_RESULT_SUCCESS))
        
    def test_normal_compose_sms_to_installed_app_patient(self):
        '''
        109305
        This test is for '109305 Compose SMS to install app patient'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.select(data.FILTER_ACTIVE, data.PR_DIRECTORY_FILTER)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.click(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        sms_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_SMS_NUMBER))
        app_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_APP_NUMBER))
        total_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_TOTAL_NUMBER))
        self.assertEqual(total_counter, sms_counter+app_counter)
        self.assertEqual(sms_counter, 0)
        self.pr.enter('Hello!', data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        if self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX).is_selected():
            self.pr.click(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX)
        self.assertTrue(self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_SEND).is_enabled())
        self.pr.click(data.PR_DIRECTORY_GROUP_SMS_SEND)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_RESULT_DIALOG)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_RESULT_TITLE_SUCCESS)
        self.assertEqual(data.MES_GROUP_SMS_SUCCESS, self.pr.text(data.PR_DIRECTORY_GROUP_SMS_RESULT_SUCCESS))
        
    def test_normal_compose_sms_to_uninstalled_app_patient(self):
        '''
        109306
        This test is for '109306 Compose SMS to uninstall app patient'
        '''
        self.pr.login(data.NURSE, self.demo[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.select(data.FILTER_NOT_INSTALL, data.PR_DIRECTORY_FILTER)
        self.pr.verify(data.PR_DIRECTORY_SEARCH_RESULT_INFO)
        if (data.MES_PATIENT_SEARCH_NO_RESULT == self.pr.text(data.PR_DIRECTORY_SEARCH_RESULT_INFO)):
            self.pr.create_new_patient()
            self.pr.driver.get(data.DIRECTORY_PATH)
            self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
            self.pr.select(data.FILTER_NOT_INSTALL, data.PR_DIRECTORY_FILTER)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.click(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        sms_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_SMS_NUMBER))
        app_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_APP_NUMBER))
        total_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_TOTAL_NUMBER))
        self.assertEqual(total_counter, sms_counter+app_counter)
        self.assertEqual(app_counter, 0)
        self.pr.enter('Hello!', data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        if self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX).is_selected():
            self.pr.click(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX)
        self.assertTrue(self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_SEND).is_enabled())
        self.pr.click(data.PR_DIRECTORY_GROUP_SMS_SEND)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_RESULT_DIALOG)
        # self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_RESULT_TITLE_SUCCESS)
        # self.assertEqual(data.MES_GROUP_SMS_SUCCESS, self.pr.text(data.PR_DIRECTORY_GROUP_SMS_RESULT_SUCCESS))
        
    def test_normal_compose_sms_to_ehr_patient(self):
        '''
        109307
        This test is for '109307 Compose SMS to EHR patient'
        '''
        self.pr.login(data.NURSE, self.demo[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.select(data.FILTER_EHR_ONLY, data.PR_DIRECTORY_FILTER)
        self.pr.verify(data.PR_DIRECTORY_SEARCH_RESULT_INFO)
        if (data.MES_PATIENT_SEARCH_NO_RESULT == self.pr.text(data.PR_DIRECTORY_SEARCH_RESULT_INFO)):
            self.pr.create_new_EHR_patient()
            self.pr.driver.get(data.DIRECTORY_PATH)
            self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
            self.pr.select(data.FILTER_EHR_ONLY, data.PR_DIRECTORY_FILTER)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.click(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        sms_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_SMS_NUMBER))
        app_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_APP_NUMBER))
        total_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_TOTAL_NUMBER))
        self.assertEqual(total_counter, sms_counter+app_counter)
        self.assertEqual(app_counter, 0)
        self.pr.enter('Hello!', data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        if self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX).is_selected():
            self.pr.click(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX)
        self.assertTrue(self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_SEND).is_enabled())
        self.pr.click(data.PR_DIRECTORY_GROUP_SMS_SEND)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_RESULT_DIALOG)
        # self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_RESULT_TITLE_SUCCESS)
        # self.assertEqual(data.MES_GROUP_SMS_SUCCESS, self.pr.text(data.PR_DIRECTORY_GROUP_SMS_RESULT_SUCCESS))
        
    def test_normal_compose_sms_count_check(self):
        '''
        109308
        This test is for '109308 Charactoers count check'
        '''
        self.pr.login(data.NURSE, self.demo[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.click(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        sms_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_SMS_NUMBER))
        app_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_APP_NUMBER))
        total_counter = int(self.pr.text(data.PR_DIRECTORY_GROUP_SMS_TOTAL_NUMBER))
        self.assertEqual(total_counter, sms_counter+app_counter)
        if self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX).is_selected():
            self.pr.click(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX)
            
        # Verify counter works well when input less than 160 characters
        self.pr.enter('Hello!', data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        self.assertTrue('154' in self.pr.text(data.PR_DIRECTORY_GROUP_SMS_COUNTER))
        self.assertTrue('green' in self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_COUNTER).get_attribute('style'))
        self.assertTrue(self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_SEND).is_enabled())
        
        # Verify counter works well when input just 160 characters
        self.pr.clear(data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        for i in range(160):
            self.pr.enter('A', data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        self.assertTrue('0' in self.pr.text(data.PR_DIRECTORY_GROUP_SMS_COUNTER))
        self.assertTrue('green' in self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_COUNTER).get_attribute('style'))
        self.assertTrue(self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_SEND).is_enabled())
        
        # Verify counter works well when input more than 160 characters
        self.pr.enter('B', data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        self.assertTrue('-1' in self.pr.text(data.PR_DIRECTORY_GROUP_SMS_COUNTER))
        self.assertTrue('red' in self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_COUNTER).get_attribute('style'))
        self.assertFalse(self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_SEND).is_enabled())
        
    def test_normal_interrupt_send_sms(self):
        '''
        109310
        This test is for '109310 Interrupt send SMS'
        '''
        self.pr.login(data.NURSE, self.demo[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.click(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        self.pr.enter('Hello!', data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        self.pr.click(data.PR_DIRECTORY_GROUP_SMS_CANCEL)
        self.pr.wait_until_not_present(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.click(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        self.assertEqual('Hello!', self.pr.text(data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD))
        self.pr.click(data.PR_DIRECTORY_GROUP_SMS_CLOSE)
        self.pr.wait_until_not_present(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        
    def test_normal_validation_check_for_copy_number(self):
        '''
        109312
        This test is for '109312 Send a copy to validation check'
        '''
        self.pr.login(data.NURSE, self.demo[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.click(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_GROUP_SMS_DIALOG)
        self.pr.enter('Hello!', data.PR_DIRECTORY_GROUP_SMS_TEXT_FIELD)
        if not self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX).is_selected():
            self.pr.click(data.PR_DIRECTORY_GROUP_SMS_CHECK_BOX)
        self.number_validation_check_on_group_sms()
        self.pr.clear(data.PR_DIRECTORY_GROUP_SMS_CELL_NUMBER)
        # self.assertFalse(self.pr.focus(data.PR_DIRECTORY_GROUP_SMS_SEND).is_enabled())
        
    def test_normal_filter_list_check_for_non_study_practice(self):
        '''
        109301
        This test is for '109301 Quick search list check'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_SMS_BUTTON)
        self.pr.click(data.PR_DIRECTORY_FILTER)
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_ALL_PATIENT))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_TYPE_ONE))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_TYPE_TWO))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_GEST))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_PRE_DIA))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_OTHER))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_ACTIVE))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_INACTIVE))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_NOT_INSTALLED))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_EHR))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_A1C))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_BG_CONTROL))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_MEDADH))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_NEXT_APPO))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_WILL_EXPIRE))
        self.assertTrue(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_EXPIRED))
        self.assertFalse(self.pr.is_element_present(data.PR_DIRECTORY_FILTER_OPTION_STUDY_PATIENT))
        
    def test_normal_sort_by_practice_name(self):
        '''
        109018
        This test is for '109018 Sort by "practice name"'
        '''
        self.pr.login(data.DOCTOR, setup.demo_data1[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        practice_name = [item.text for item in self.pr.find(data.PR_DIRECTORY_PRACTICE_NAME)]
        self.assertEqual(len(set(practice_name)), 2)
        self.pr.click(data.PR_DIRECTORY_PRACTICE_NAME_SORT)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        practice_name = [item.text for item in self.pr.find(data.PR_DIRECTORY_PRACTICE_NAME)]
        self.assertEqual(practice_name[0], practice_name[1])
        self.assertEqual(practice_name[2], practice_name[3])
        
    def test_normal_search_by_practice_name(self):
        '''
        109017
        This test is for '109017 Search patients by practice name'
        '''
        self.pr.login(data.DOCTOR, setup.demo_data1[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        practice_name = [item.text for item in self.pr.find(data.PR_DIRECTORY_PRACTICE_NAME)]
        practice_name = list(set(practice_name))
        self.pr.enter('practice="%s"' %practice_name[0], data.PR_DIRECTORY_SEARCH_FIELD)
        self.pr.click(data.PR_DIRECTORY_SEARCH_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        practice_name = [item.text for item in self.pr.find(data.PR_DIRECTORY_PRACTICE_NAME)]
        self.assertEqual(len(practice_name), 2)
        
    def test_normal_search_by_name(self):
        '''
        109009
        This test is for '109009 Search patients by patient name'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        self.pr.enter('Daya', data.PR_DIRECTORY_SEARCH_FIELD)
        self.pr.click(data.PR_DIRECTORY_SEARCH_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        self.assertEqual(len(self.pr.find(data.PR_DIRECTORY_LAST_NAME)), 1)
        self.pr.clear(data.PR_DIRECTORY_SEARCH_FIELD)
        self.pr.enter('Utta', data.PR_DIRECTORY_SEARCH_FIELD)
        self.pr.click(data.PR_DIRECTORY_SEARCH_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        self.assertEqual(len(self.pr.find(data.PR_DIRECTORY_LAST_NAME)), 1)
        self.pr.clear(data.PR_DIRECTORY_SEARCH_FIELD)
        self.pr.enter('!@#$', data.PR_DIRECTORY_SEARCH_FIELD)
        self.pr.click(data.PR_DIRECTORY_SEARCH_BUTTON)
        self.pr.verify(data.PR_DIRECTORY_NO_PATIENT)
    
if __name__ == '__main__':
    unittest.main()