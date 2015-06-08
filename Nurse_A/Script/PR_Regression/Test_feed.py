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

class Feed(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        
    def tearDown(self):
        self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
        
    def test_urgent_dismiss_event_by_chat(self):
        '''
        108002
        This test is for '108002 Complete the event by chat'
        '''
        MES = 'hello, world!'
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_FEED_FIRST_WARNING)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT)
        self.pr.click(data.PR_PATIENT_RECORD_CHAT)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT_TEXTAREA)
        self.pr.enter(MES, data.PR_PATIENT_RECORD_CHAT_TEXTAREA)
        self.pr.click(data.PR_PATIENT_RECORD_CHAT_SEND_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT_LATEST_MES)
        self.assertEqual(self.pr.text(data.PR_PATIENT_RECORD_CHAT_LATEST_MES), MES)
        # Check the feed event
        self.pr.click(data.PR_NAV_FEED)
        self.assertEqual(self.pr.title, data.PR_FEED_TITLE)
        self.assertFalse(self.pr.is_element_present(data.PR_FEED_FIRST_WARNING))
        
    def test_urgent_dismiss_event_by_med_goal(self):
        '''
        108003
        This test is for '108003 Complete the event by update MED goals'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_FEED_FIRST_WARNING)
        self.pr.verify(data.PR_PATIENT_RECORD_MED_GOALS)
        self.pr.click(data.PR_PATIENT_RECORD_MED_GOALS)
        self.pr.verify(data.PR_MED_GOALS_TITLE)
        self.pr.click(data.PR_MED_GAOLS_FORM_DELETE)
        self.pr.click(data.PR_MED_GOALS_SUBMIT_BUTTON)
        self.pr.verify(data.PR_MED_GOALS_CONFIRM_DIALOG)
        self.pr.click(data.PR_MED_GOALS_CONFIRM_SUBMIT_BUTTON)
        self.pr.wait_until_not(data.PR_MED_GOALS_CONFIRM_DIALOG)
        # Check the feed event
        self.pr.click(data.PR_NAV_FEED)
        self.assertEqual(self.pr.title, data.PR_FEED_TITLE)
        self.assertFalse(self.pr.is_element_present(data.PR_FEED_FIRST_WARNING))
        
    def test_urgent_dismiss_event_by_bg_goal(self):
        '''
        108004
        This test is for '108004 Complete the event by update BG goals'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_FEED_FIRST_WARNING)
        self.pr.verify(data.PR_PATIENT_RECORD_SMBG)
        self.pr.click(data.PR_PATIENT_RECORD_SMBG)
        self.pr.verify(data.PR_PATIENT_RECORD_SMBG_TITLE)
        map(self.pr.click, data.PR_ADD_PATIENT_EVERY)
        self.pr.click(data.PR_BG_GOALS_SAVE_BUTTON)
        self.pr.wait_until_not(data.PR_PATIENT_RECORD_SMBG_TITLE)
        # Check the feed event
        self.pr.click(data.PR_NAV_FEED)
        self.assertEqual(self.pr.title, data.PR_FEED_TITLE)
        self.assertFalse(self.pr.is_element_present(data.PR_FEED_FIRST_WARNING))
        
    def test_urgent_delete_feed_event(self):
        '''
        108005
        This test is for '108005 Delete event in feed'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_FEED_CLOSE)
        self.pr.refresh()
        self.assertFalse(self.pr.is_element_present(data.PR_FEED_FIRST_WARNING))
        
    def test_urgent_forward_feed_event(self):
        '''
        108006
        This test is for '108006 Forward event in feed'
        '''
        notes = 'It is up to you.'
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_FEED_FORWARD)
        self.pr.verify(data.PR_FEED_FORWARD_TO)
        self.pr.click(data.PR_FEED_FORWARD_TO)
        self.pr.click(data.PR_FEED_FORWARD_FIRST_OPTION)
        self.pr.enter(notes, data.PR_FEED_FORWARD_NOTE)
        self.pr.click(data.PR_FEED_FORWARD_BUTTON)
        self.pr.wait_until_not(data.PR_FEED_FIRST_WARNING)
        self.pr.logout()
        self.pr.login(data.NURSE, self.demo[0])
        self.assertTrue(self.pr.is_element_present(data.PR_FEED_WARNING_FORWARD_BY))
        
    def test_urgent_delete_feed_message(self):
        '''
        106013
        This test is for '106013 Delete messages event in Feed'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.NURSE, self.demo[0])
        self.pr.clear_message_event()
        self.pr.logout()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.assertTrue(self.pr.is_element_present(data.PR_FEED_FIRST_MESSAGE))
        
    def test_urgent_dismiss_feed_message_by_chat(self):
        '''
        106014
        This test is for '106014 Complete messages event by chat'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.NURSE, self.demo[0])
        MES = 'hello, world!'
        NAME = 'Ashvin'
        self.pr.click(data.PR_FEED_FIRST_MESSAGE)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT)
        self.pr.click(data.PR_PATIENT_RECORD_CHAT)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT_TEXTAREA)
        self.pr.enter(MES, data.PR_PATIENT_RECORD_CHAT_TEXTAREA)
        self.pr.click(data.PR_PATIENT_RECORD_CHAT_SEND_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_CHAT_LATEST_MES)
        sleep(constant.INTERVAL_5)
        self.assertEqual(self.pr.text(data.PR_PATIENT_RECORD_CHAT_LATEST_MES), MES)
        self.pr.click(data.PR_NAV_FEED)
        self.assertEqual(self.pr.title, data.PR_FEED_TITLE)
        if self.pr.is_element_present(data.PR_FEED_FIRST_MESSAGE):
            self.assertFalse(NAME in self.pr.focus(data.PR_FEED_FIRST_MESSAGE).find_element_by_css_selector(data.PR_FEED_PATIENT_NAME).text)
        self.pr.logout()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.assertTrue(NAME in self.pr.focus(data.PR_FEED_FIRST_MESSAGE).find_element_by_css_selector(data.PR_FEED_PATIENT_NAME).text)
        

if __name__ == '__main__':
    unittest.main()