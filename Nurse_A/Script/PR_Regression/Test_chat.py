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
from Nurse_A.Ext_unittest.Testcase import Case

class Chat(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        
    def tearDown(self):
        self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
        
    def test_urgent_send_quick_message(self):
        '''
        111032
        This test is for '111032 send quick message'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_CHAT)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT_QUICK_BUTTON)
        self.pr.click(data.PR_PATIENT_RECORD_CHAT_QUICK_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_QUICK_MES_BIG_SUCCESS)
        self.pr.click(data.PR_PATIENT_RECORD_QUICK_MES_BIG_SUCCESS)
        self.pr.click(data.PR_PATIENT_RECORD_QUICK_MES_SEND)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT_SECOND_MES)
        self.assertEqual(self.pr.text(data.PR_PATIENT_RECORD_CHAT_SECOND_MES), data.MES_CONTENT_BIGGEST_SUCCESS)
        
    def test_urgent_send_message_to_patient(self):
        '''
        111029
        This test is for '111029 send message to patient'
        '''
        MES = 'hello, world!'
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_CHAT)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT_TEXTAREA)
        self.pr.enter(MES, data.PR_PATIENT_RECORD_CHAT_TEXTAREA)
        self.pr.click(data.PR_PATIENT_RECORD_CHAT_SEND_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT_SECOND_MES)
        self.assertEqual(self.pr.text(data.PR_PATIENT_RECORD_CHAT_SECOND_MES), MES)
        
                
if __name__ == '__main__':
    unittest.main()