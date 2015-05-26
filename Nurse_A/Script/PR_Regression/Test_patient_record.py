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

class Patient_record(unittest.TestCase):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        
    def tearDown(self):
        self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
    
    def test_add_med_goals(self):
        # This test is for '111014 Add new medication - insulin'
        #                  '111015 Add new medication - insulin'
        now = datetime.datetime.now()
        date_str = now.strftime('%b %d, %Y')
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
        
    def test_add_bg_goals(self):
        # This test is for '111020 Add BG Goals'
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

if __name__ == '__main__':
    unittest.main()
        