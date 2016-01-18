#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Nurse_A.Platform.android import AND
from web_scenario import WEB
from time import sleep, time
import datetime
import simplejson as json
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from Nurse_A.Settings import data, setup, mobile_setup, constant

class ANDROID(AND):
    
    def __init__(self, PORT = '4723', PKG = 'com.gatherhealth.gatherdm', ACT = '.activity.LaunchActivity'):
        # Create a new session with passed in Port, package and activity
        address = 'http://localhost:'+PORT+'/wd/hub'
        caps = {
            'deviceName' : 'Sony',
            'platformName' : 'Android',
            'platformVersion' : '4.4',
            'appPackage' : PKG,
            'appActivity' : ACT,
        }
        self.driver = webdriver.Remote(address, caps)
        # Get resolution
        self.X = self.driver.get_window_size()['width']
        self.Y = self.driver.get_window_size()['height']
        # Package name
        self.package_name = PKG
        self.activity_name = ACT

    def login(self, username, password = '123456'):
        # Log in with an exist patient account
        # If APP not logged in
        self.hide_keyboard()
        self.verify(data.DM_AND_SIGN_IN_FIELD)
        self.enter(username, data.DM_AND_SIGN_IN_FIELD)
        self.hide_keyboard()
        self.click(data.DM_AND_SIGN_IN_BUTTON)
        self.verify(data.DM_AND_PASSWORD_TITLE)
        self.enter(password, data.DM_AND_PASSWORD_FIELD)
        self.hide_keyboard()
        self.click(data.DM_AND_PASSWORD_SIGN_IN_BTN)
        self.verify(data.DM_AND_BOTTOM_GOALS)
            
    def logout(self):
        self.restart()
        if self.is_element_present(data.DM_AND_MED_CHANGE_DECLINE_BUTTON):
            self.click(data.DM_AND_MED_CHANGE_DECLINE_BUTTON)
            self.verify(data.DM_AND_CHAT_SEND_BTN)
        # And Gather icon invisible
        if not self.is_element_present(data.DM_AND_OPTIONS_MENU_BTN):
            self.do_until_true(lambda: self.press('Back'), lambda: self.is_element_present(data.DM_AND_OPTIONS_MENU_BTN) or self.is_element_present(data.DM_AND_SIGN_IN_NO_SPAM_HINT))
        if self.is_element_present(data.DM_AND_SIGN_IN_NO_SPAM_HINT):
            return
        self.do_until_true(lambda: self.click(data.DM_AND_OPTIONS_MENU_BTN), lambda: self.is_element_present(data.DM_AND_OPTIONS_SETTINGS))
        self.click(data.DM_AND_OPTIONS_SETTINGS)
        self.do_until_true(lambda: self.swipe_up(), lambda: self.is_element_present(data.DM_AND_SETTINGS_LOG_OUT))
        self.click(data.DM_AND_SETTINGS_LOG_OUT)
        self.verify(data.DM_AND_SIGN_IN_NO_SPAM_HINT)

    def signup(self, email):
        # Finish a simple sign up for the given email
        self.verify(data.DM_AND_SIGN_IN_FIELD)
        self.enter(email, data.DM_AND_SIGN_IN_FIELD)
        self.hide_keyboard()
        self.click(data.DM_AND_SIGN_IN_BUTTON)
        self.verify(data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.enter('123456', data.DM_AND_SET_PASSWORD_PASSWORD_FIELD)
        self.enter('123456', data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.hide_keyboard()
        self.click(data.DM_AND_SET_PASSWORD_BUTTON)
        self.verify(data.DM_AND_BOTTOM_GOALS)
        
    def get_new_patient_account(self, practice_id=setup.demo_data[1], email=None, state=2,
            name=None, country_code='91', number='1234567890', billing=True,
            ACCOUNT=data.DOCTOR, PASSWORD=setup.demo_data[0], bg=None, med=None, after_sign_up=False
    ):
        # Create a new patient and return the email
        patient = mobile_setup.get_new_patient_account(practice_id=practice_id, email=email, state=state,
                name=name, country_code=country_code, number=number, billing=billing,
                ACCOUNT=ACCOUNT, PASSWORD=PASSWORD, bg=bg, med=med, after_sign_up=after_sign_up
                )
        return patient

    def set_bg_goal(self, goals, patient_id, ACCOUNT=data.DOCTOR, PASSWORD=setup.demo_data[0]):
        # Set bg goals for patient
        mobile_setup.set_bg_goal(goals=goals, patient_id=patient_id, ACCOUNT=ACCOUNT, PASSWORD=PASSWORD)

    def set_med_goal(self, goals, patient_id, ACCOUNT=data.DOCTOR, PASSWORD=setup.demo_data[0]):
        # Set med goals for patient
        mobile_setup.set_med_goal(goals=goals, patient_id=patient_id, ACCOUNT=ACCOUNT, PASSWORD=PASSWORD)

    def accept_med_change(self):
        # Accept the medication change
        self.restart()
        self.verify(data.DM_AND_BOTTOM_GOALS)
        self.click(data.DM_AND_BOTTOM_GOALS)
        self.wait_until_present(data.DM_AND_MED_CHANGE_CONFIRM_BUTTON)
        self.click(data.DM_AND_MED_CHANGE_CONFIRM_BUTTON)
        self.verify(data.DM_AND_GOAL_DATE)

    '''
    Rewrite this method to set_server automatically
    '''
    def set_server(self):
        server = self.get_server_ip()
        self.verify(data.DM_AND_SIGN_IN_NO_SPAM_HINT)
        self.hide_keyboard()
        self.press('Back')
        self.verify(data.DM_AND_SERVER_ADDRESS)
        self.clear(data.DM_AND_SERVER_ADDRESS)
        self.enter(server, data.DM_AND_SERVER_ADDRESS)
        self.click(data.DM_AND_SERVER_SUBMIT)
        self.verify(data.DM_AND_SIGN_IN_NO_SPAM_HINT)
        self.teardown()

    def restart(self):
        self.close_app()
        self.launch_app()

