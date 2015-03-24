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

class Add_new_patient(unittest.TestCase):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        
    def tearDown(self):
        self.pr.teardown()
        
    def test_add_hk_patient_with_hkid(self):
        # This test is for '198015 Add a new HK patient with HKID'
        self.pr.login(data.HK_DOCTOR, data.PASSWORD)
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.assertEqual(self.pr.text(data.PR_ADD_PATIENT_TITLE), data.ADD_PATIENT)
        INFO = self.pr.generate_info()
        self.pr.enter(INFO['surname'], data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter(INFO['givename'], data.PR_ADD_PATIENT_GIVENAME)
        self.pr.select('United States (+1)', data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.enter(INFO['us_cell'], data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter(INFO['email'], data.PR_ADD_PATIENT_EMAIL)
        self.pr.select('English', data.PR_ADD_PATIENT_LANGUAGE)
        self.pr.click(data.PR_ADD_PATIENT_GENDER_MALE)
        self.pr.click(data.PR_ADD_PATIENT_HAS_HKID_YES)
        self.pr.verify(data.PR_ADD_PATIENT_HKID)
        self.pr.enter(data.HKID, data.PR_ADD_PATIENT_HKID)
        self.pr.enter(data.HKID_CHECK, data.PR_ADD_PATIENT_HKID_CHECK)
        self.pr.click(data.PR_ADD_PATIENT_PREMIUM_TRIAL)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.click(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_ID)
        ID = self.pr.text(data.PR_PATIENT_RECORD_ID)
        # Delete the patient
        self.pr.delete_patient(ID)
        
    def test_add_patient_with_full_info(self):
        # This test is for '101005 Invite a patient and full fill info'
        #                  '101002 Invite a patient with billing' 
        
if __name__ == '__main__':
    unittest.main()