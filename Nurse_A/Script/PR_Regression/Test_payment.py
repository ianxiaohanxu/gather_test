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
from Nurse_A.Settings import keycode, constant, data, setup
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case

class Payment(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        self.demo = setup.demo_data
        
    def tearDown(self):
        # self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
        
    def test_urgent_extend_subscriptioin_with_premium(self):
        '''
        111052
        This test is for '111052 Extend Premium'
        '''
        # # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_BILLING)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_OVERVIEW)
        self.pr.clear(data.PR_PATIENT_RECORD_BILLING_MONTH_RATE)
        self.pr.enter('0', data.PR_PATIENT_RECORD_BILLING_MONTH_RATE)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_SUBMIT)
        self.assertTrue(self.pr.is_element_present(data.PR_PATIENT_RECORD_BILLING_RATE_ERROR))
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_BILLING_MONTH_RATE).get_attribute('class') == 'invalid')
        self.pr.clear(data.PR_PATIENT_RECORD_BILLING_MONTH_RATE)
        self.pr.enter('abc', data.PR_PATIENT_RECORD_BILLING_MONTH_RATE)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_SUBMIT)
        self.assertTrue(self.pr.is_element_present(data.PR_PATIENT_RECORD_BILLING_RATE_ERROR))
        self.pr.clear(data.PR_PATIENT_RECORD_BILLING_MONTH_RATE)
        self.pr.enter('5', data.PR_PATIENT_RECORD_BILLING_MONTH_RATE)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_SUBMIT)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_P_CONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_P_CONFIRM_BACK)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BILLING_P_CONFIRM)
        self.assertTrue('5' in self.pr.text(data.PR_PATIENT_RECORD_BILLING_MONTH_RATE))
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_SUBMIT)
        end_date = self.pr.text(data.PR_PATIENT_RECORD_BILLING_P_CONFIRM_DATE)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_P_CONFIRM_SUBMIT)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BILLING_P_CONFIRM)
        self.assertTrue(end_date in self.pr.text(data.PR_PATIENT_RECORD_BILLING_END_DATE))
        self.assertTrue(len(self.pr.find(data.PR_PATIENT_RECORD_BILLING_HISTOR_ENTRY)) == 2)
        
    def test_urgent_extend_subscriptioin_with_free_trial(self):
        '''
        111053
        This test is for '111053 Extend Premium (Free Trial)'
        '''
        # # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_BILLING)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_OVERVIEW)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_FREE_TRIAL_RADIO)
        sleep(constant.INTERVAL_1)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_BILLING_MONTH_RATE).is_enabled())
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_SUBMIT)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_F_CONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_F_CONFIRM_BACK)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BILLING_F_CONFIRM)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_BILLING_MONTH_RATE).is_enabled())
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_SUBMIT)
        end_date = self.pr.text(data.PR_PATIENT_RECORD_BILLING_F_CONFIRM_DATE)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_F_CONFIRM_SUBMIT)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BILLING_F_CONFIRM)
        self.assertTrue(end_date in self.pr.text(data.PR_PATIENT_RECORD_BILLING_END_DATE))
        self.assertTrue(len(self.pr.find(data.PR_PATIENT_RECORD_BILLING_HISTOR_ENTRY)) == 2)
        
    def test_urgent_void_premium_entry(self):
        '''
        111056
        This test is for '111056 Void a premium entry'
        '''
        # # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_BILLING)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_OVERVIEW)
        self.pr.clear(data.PR_PATIENT_RECORD_BILLING_MONTH_RATE)
        self.pr.enter('5', data.PR_PATIENT_RECORD_BILLING_MONTH_RATE)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_SUBMIT)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_P_CONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_P_CONFIRM_SUBMIT)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BILLING_P_CONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_FIRST_VOID)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM_BACK)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM)
        self.assertFalse(self.pr.is_element_present(data.PR_PATIENT_RECORD_BILLING_FIRST_VOIDED))
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_FIRST_VOID)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM)
        end_date = self.pr.text(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM_DATE)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM_SUBMIT)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM)
        self.assertTrue(end_date in self.pr.text(data.PR_PATIENT_RECORD_BILLING_END_DATE))
        self.assertTrue(self.pr.is_element_present(data.PR_PATIENT_RECORD_BILLING_FIRST_VOIDED))
        
    def test_urgent_void_free_trial_entry(self):
        '''
        111057
        This test is for '111057 Void a free trial entry'
        '''
        # # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_BILLING)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_OVERVIEW)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_FIRST_VOID)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM_BACK)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM)
        self.assertFalse(self.pr.is_element_present(data.PR_PATIENT_RECORD_BILLING_FIRST_VOIDED))
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_FIRST_VOID)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM)
        self.assertTrue(self.pr.is_element_present(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM_BASIC))
        plan = self.pr.text(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM_BASIC)
        self.pr.click(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM_SUBMIT)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BILLING_V_CONFIRM)
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_BASIC_PLAN)
        self.assertTrue(plan in self.pr.text(data.PR_PATIENT_RECORD_BILLING_BASIC_PLAN))
        self.pr.verify(data.PR_PATIENT_RECORD_BILLING_FIRST_VOIDED)
        
if __name__ == '__main__':
    unittest.main()