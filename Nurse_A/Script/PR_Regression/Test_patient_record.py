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
import unittest, datetime
from Nurse_A.Settings import keycode, constant, data
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case

class Patient_record(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        
    def tearDown(self):
        self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
    
    def test_urgent_add_med_goals(self):
        '''
        111014
        This test is for '111014 Add new medication - with a exist medication name'
        '''
        now = datetime.datetime.now()
        date_str = now.strftime('%b %d, %Y')
        if date_str[4] == '0':
            date_str = date_str.replace('0', '', 1)
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_MED_GOALS)
        self.pr.click(data.PR_PATIENT_RECORD_MED_GOALS)
        self.pr.verify(data.PR_MED_GOALS_TITLE)
        self.pr.add_med_goals(data.MED_GOALS)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_INFO)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_MED_GOALS_UNCONFIRM)
        goals = self.pr.get_med_goals()
        self.assertEqual(goals, data.MED_GOALS)
        self.pr.click(data.PR_PATIENT_RECORD_SUMMARY_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_SUMMARY_MED_LAST_HISTORY)
        self.assertEqual(date_str, self.pr.text(data.PR_PATIENT_RECORD_SUMMARY_MED_LAST_HISTORY))

    def test_urgent_add_bg_goals(self):
        '''
        111020
        This test is for '111020 Add BG Goals'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_SMBG)
        self.pr.click(data.PR_PATIENT_RECORD_SMBG)
        self.pr.verify(data.PR_PATIENT_RECORD_SMBG_TITLE)
        map(self.pr.click, data.PR_ADD_PATIENT_EVERY)
        self.pr.click(data.PR_BG_GOALS_SAVE_BUTTON)
        self.pr.wait_until_not(data.PR_PATIENT_RECORD_SMBG_TITLE)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_INFO)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.assertTrue('49' in self.pr.text(data.PR_PATIENT_RECORD_SMBG_COUNTER))


    def test_urgent_delete_med_goals(self):
        '''
        111017
        This test is for '111017 delete medication'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_MED_GOALS)
        self.pr.click(data.PR_PATIENT_RECORD_MED_GOALS)
        self.pr.verify(data.PR_MED_GOALS_TITLE)
        self.pr.add_med_goals(data.MED_GOALS)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_INFO)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_MED_GOALS_UNCONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_MED_GOALS)
        self.pr.verify(data.PR_MED_GOALS_TITLE)
        self.pr.click(data.PR_MED_GAOLS_FORM_DELETE)
        self.pr.clear(data.PR_MED_GOALS_FORM_LUN_DOSAGE)
        self.pr.clear(data.PR_MED_GOALS_FORM_LUN_AMOUNT)
        self.pr.click(data.PR_MED_GOALS_SUBMIT_BUTTON)
        self.pr.verify(data.PR_MED_GOALS_CONFIRM_TITLE)
        self.pr.click(data.PR_MED_GOALS_CONFIRM_SUBMIT_BUTTON)
        self.pr.wait_until_not(data.PR_MED_GOALS_CONFIRM_TITLE)
        goals = self.pr.get_med_goals()
        original_goals = data.MED_GOALS[1]
        original_goals[4][0] = 0
        original_goals[4][1] = 0
        self.assertEqual(goals[0], original_goals)

if __name__ == '__main__':
    unittest.main()
        
