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
        
    def add_patient_with_full_info(self, account):
        # This test is for '101005 Invite a patient and full fill info'
        #                  '101002 Invite a patient with billing' 
        self.pr.login(account, data.PASSWORD)
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.assertEqual(self.pr.text(data.PR_ADD_PATIENT_TITLE), data.ADD_PATIENT)
        INFO = self.pr.generate_info()
        PUSH = []
        self.pr.enter(INFO['surname'], data.PR_ADD_PATIENT_SURNAME)
        PUSH.append(INFO['surname'])
        self.pr.enter(INFO['givename'], data.PR_ADD_PATIENT_GIVENAME)
        PUSH.append(INFO['givename'])
        self.pr.select('1', data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        PUSH.append('+1')
        self.pr.enter(INFO['us_cell'], data.PR_ADD_PATIENT_P_NUMBER)
        PUSH.append(INFO['us_cell'])
        self.pr.enter(INFO['email'], data.PR_ADD_PATIENT_EMAIL)
        PUSH.append(INFO['email'])
        self.pr.select('en', data.PR_ADD_PATIENT_LANGUAGE)
        self.pr.click(data.PR_ADD_PATIENT_GENDER_MALE)
        PUSH.append('Male')
        self.pr.select('3', data.PR_ADD_PATIENT_BILL_TIME)
        PUSH.append('3')
        self.pr.clear(data.PR_ADD_PATIENT_BILL_RATE)
        self.pr.enter('5', data.PR_ADD_PATIENT_BILL_RATE)
        PUSH.append('5.00')
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.select('1', data.PR_ADD_PATIENT_PATIENT_TYPE)
        PUSH.append('Type 1')
        self.pr.select('2010', data.PR_ADD_PATIENT_PATIENT_YEAR)
        PUSH.append('2010')
        self.pr.enter('aaa\n', data.PR_ADD_PATIENT_PATIENT_COMORBIDITIES)
        self.pr.enter('bbb\n', data.PR_ADD_PATIENT_PATIENT_COMORBIDITIES)
        PUSH.append(['aaa', 'bbb'])
        self.pr.enter('abc', data.PR_ADD_PATIENT_PATIENT_NOTES)
        PUSH.append('abc')
        self.pr.select('80', data.PR_ADD_PATIENT_PRE_LOWER_LIMIT)
        self.pr.select('140', data.PR_ADD_PATIENT_PRE_UPPER_LIMIT)
        self.pr.select('80', data.PR_ADD_PATIENT_POST_LOWER_LIMIT)
        self.pr.select('140', data.PR_ADD_PATIENT_POST_UPPER_LIMET)
        PUSH.extend(['80', '140', '80', '140'])
        map(self.pr.click, data.PR_ADD_PATIENT_EVERY)
        BG_GOALS = []
        for i in range(49):
            BG_GOALS.append(1)
        PUSH.append(BG_GOALS)
        self.pr.click(data.PR_ADD_PATIENT_MED_GOALS_BUTTON)
        self.pr.verify(data.PR_MED_GOALS_TITLE)
        self.pr.add_med_goals(data.MED_GOALS)
        PUSH.append(data.MED_GOALS)
        self.pr.verify(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.enter('ccc\n', data.PR_ADD_PATIENT_OTHER_MED)
        self.pr.enter('ddd\n', data.PR_ADD_PATIENT_OTHER_MED)
        PUSH.append(['ccc', 'ddd'])
        self.pr.enter('180', data.PR_ADD_PATIENT_HEIGHT)
        self.pr.enter('75', data.PR_ADD_PATIENT_WEIGHT)
        self.pr.enter('100', data.PR_ADD_PATIENT_WAIST)
        self.pr.enter('120', data.PR_ADD_PATIENT_BP_SYS)
        self.pr.enter('80', data.PR_ADD_PATIENT_BP_DIA)
        self.pr.enter('5', data.PR_ADD_PATIENT_A1C)
        self.pr.click(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_ID)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        PULL = self.pr.get_data()
        print 'PUSH:\n'
        print PUSH
        print 'PULL:\n'
        print PULL
        self.assertEqual(PUSH, PULL)
        # Delete the patient
        ID = self.pr.text(data.PR_PATIENT_RECORD_ID)
        self.pr.delete_patient(ID)
        self.pr.logout()
        
    def add_nobilling_patient(self, account):
        # This test is for '101001 Invite a patient without billing'
        self.pr.login(account, data.PASSWORD)
        self.pr.create_new_patient()
        # Delete the patient
        ID = self.pr.text(data.PR_PATIENT_RECORD_ID)
        self.pr.delete_patient(ID)
        self.pr.logout()
          
    def test_add_hk_patient_with_hkid(self):
        # This test is for '198015 Add a new HK patient with HKID'
        self.pr.login(data.HK_DOCTOR, data.PASSWORD)
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.assertEqual(self.pr.text(data.PR_ADD_PATIENT_TITLE), data.ADD_PATIENT)
        INFO = self.pr.generate_info()
        self.pr.enter(INFO['surname'], data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter(INFO['givename'], data.PR_ADD_PATIENT_GIVENAME)
        self.pr.select('1', data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.enter(INFO['us_cell'], data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter(INFO['email'], data.PR_ADD_PATIENT_EMAIL)
        self.pr.select('en', data.PR_ADD_PATIENT_LANGUAGE)
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
        self.add_patient_with_full_info(data.INDIA_DOCTOR)
        self.add_patient_with_full_info(data.INDIA_NURSE)
        
    def test_add_nobilling_patient(self):
        # This test is for '101001 Invite a patient without billing'
        self.add_nobilling_patient(data.DOCTOR_FREE)
        self.add_nobilling_patient(data.NURSE_FREE)
        
        
        
if __name__ == '__main__':
    unittest.main()