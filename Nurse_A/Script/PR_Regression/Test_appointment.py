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
import datetime
from Nurse_A.Settings import keycode, constant, data, setup
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case

class Appointment(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        self.demo = setup.demo_data
        
    def tearDown(self):
        # self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
        
    def create_simple_appointment(self):
        today = datetime.datetime.now()
        today_after_180 = today + datetime.timedelta(days=180)
        today_after_180 = today_after_180.strftime('%Y-%m-%d')
        today_after_180_slash = today_after_180.replace('-', '/')
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        INFO = list(INFO)
        INFO.append(today_after_180_slash)
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.pr.click(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1])
        self.pr.verify(data.PR_APPOINTMENT_TITLE_ADD)
        self.pr.click(data.PR_APPOINTMENT_SIX_MONTH)
        self.pr.click(data.PR_APPOINTMENT_SAVE)
        self.pr.wait_until_not(data.PR_APPOINTMENT_TITLE)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.assertTrue(today_after_180_slash in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))
        return INFO
        
    def test_urgent_add_appointment_with_full_info(self):
        '''
        197001
        This test is for '197001 Add a new appointment from patient directory'
        '''
        today = datetime.datetime.now()
        today = today.strftime('%Y-%m-%d')
        today_slash = today.replace('-', '/')
        tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        tomorrow_slash = tomorrow.replace('-', '/')
        time_str = '12:00'
        notes = 'Hello world!'
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.pr.click(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1])
        self.pr.verify(data.PR_APPOINTMENT_TITLE_ADD)
        self.pr.click(data.PR_APPOINTMENT_TODAY)
        # self.pr.enter(tomorrow, data.PR_APPOINTMENT_DATE)
        self.pr.enter(time_str, data.PR_APPOINTMENT_TIME)
        self.pr.enter(notes, data.PR_APPOINTMENT_NOTE)
        self.pr.click(data.PR_APPOINTMENT_SAVE)
        self.pr.wait_until_not(data.PR_APPOINTMENT_TITLE)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.assertTrue(today_slash in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))
        
    def test_urgent_add_appointment_without_time(self):
        '''
        197002 197006
        This test is for '197002 Add a new appointment without time set'
        This test is for '197006 Add a new appointment with date shortcut'
        '''
        self.create_simple_appointment()
        
    def test_urgent_edit_appointment(self):
        '''
        197004
        This test is for '197004 Edit an appointment'
        '''
        today = datetime.datetime.now()
        date_after_90 = today + datetime.timedelta(days=90)
        date_after_90 = date_after_90.strftime('%Y-%m-%d')
        date_after_90_slash = date_after_90.replace('-', '/')
        time_str = '12:30'
        notes = 'Hello world!'
        INFO = self.create_simple_appointment()
        # Edit appointment
        self.pr.click(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1])
        self.pr.verify(data.PR_APPOINTMENT_TITLE_EDIT)
        self.pr.click(data.PR_APPOINTMENT_THREE_MONTH)
        self.pr.enter(time_str, data.PR_APPOINTMENT_TIME)
        self.pr.enter(notes, data.PR_APPOINTMENT_NOTE)
        self.pr.click(data.PR_APPOINTMENT_SAVE)
        self.pr.wait_until_not(data.PR_APPOINTMENT_TITLE)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.assertTrue(date_after_90_slash in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))
        self.assertTrue(time_str in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))
        
    def test_urgent_delete_appointment(self):
        '''
        197005
        This test is for '197005 Delete an appointment'
        '''
        INFO = self.create_simple_appointment()
        # Delete appointment
        self.pr.click(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1])
        self.pr.verify(data.PR_APPOINTMENT_TITLE_EDIT)
        self.pr.click(data.PR_APPOINTMENT_DELETE)
        self.pr.wait_until_not(data.PR_APPOINTMENT_TITLE)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.assertTrue(INFO[2] not in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))
        
    def test_urgent_complete_appointment(self):
        '''
        197008
        This test is for '197008 Mark an appointment as complete'
        '''
        INFO = self.create_simple_appointment()
        # Complete appointment
        self.pr.click(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1])
        self.pr.verify(data.PR_APPOINTMENT_TITLE_EDIT)
        self.pr.click(data.PR_APPOINTMENT_COMPLETE)
        self.pr.wait_until_not(data.PR_APPOINTMENT_TITLE)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.assertTrue(INFO[2] not in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))
        self.assertTrue(INFO[2] in self.pr.text(data.PR_DIRECTORY_PATIENT_LAST_APPT %INFO[1]))
        
    def test_normal_add_appointment_at_the_same_time(self):
        '''
        197007
        This test is for '197007 Add appointments at the same time'
        '''
        today = datetime.datetime.now()
        today = today.strftime('%Y-%m-%d')
        today_slash = today.replace('-', '/')
        time_str = '12:00'
        notes = 'Hello world!'
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.pr.click(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1])
        self.pr.verify(data.PR_APPOINTMENT_TITLE_ADD)
        self.pr.click(data.PR_APPOINTMENT_TODAY)
        self.pr.enter(time_str, data.PR_APPOINTMENT_TIME)
        self.pr.enter(notes, data.PR_APPOINTMENT_NOTE)
        self.pr.click(data.PR_APPOINTMENT_SAVE)
        self.pr.wait_until_not(data.PR_APPOINTMENT_TITLE)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.assertTrue(today_slash in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))
        self.assertTrue(time_str in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))
        INFO = self.pr.create_new_patient()
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.pr.click(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1])
        self.pr.verify(data.PR_APPOINTMENT_TITLE_ADD)
        self.pr.click(data.PR_APPOINTMENT_TODAY)
        self.pr.enter(time_str, data.PR_APPOINTMENT_TIME)
        self.pr.enter(notes, data.PR_APPOINTMENT_NOTE)
        self.pr.click(data.PR_APPOINTMENT_SAVE)
        self.pr.wait_until_not(data.PR_APPOINTMENT_TITLE)
        self.pr.verify(data.PR_DIRECTORY_PATIENT_ENTRY %INFO[1])
        self.assertTrue(today_slash in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))
        self.assertTrue(time_str in self.pr.text(data.PR_DIRECTORY_PATIENT_NEXT_APPT %INFO[1]))

if __name__ == '__main__':
    unittest.main()