#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Nurse_A.Platform.android import AND
from web_scenario import WEB
from time import sleep, time
import datetime
import simplejson as json
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver
from Nurse_A.Settings import data, setup, mobile_setup

class ANDROID(AND):
    
    def __init__(self, PORT = '4723', PKG = 'com.gatherhealth.gatherdm', ACT = '.activity.MainActivity'):
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
        if self.is_element_present(data.DM_AND_WELCOME_ENTER):
            self.click(data.DM_AND_WELCOME_ENTER)
        self.verify(data.DM_AND_SIGN_IN_FIELD)
        self.enter(username, data.DM_AND_SIGN_IN_FIELD)
        self.click(data.DM_AND_SIGN_IN_BUTTON)
        self.verify(data.DM_AND_PASSWORD_TITLE)
        self.enter(password, data.DM_AND_PASSWORD_FIELD)
        self.click(data.DM_AND_PASSWORD_SIGN_IN_BTN)
        self.verify(data.DM_AND_GOAL_DATE)
            
    def logout(self):
        self.close_app()
        self.launch_app()
        if self.is_element_present(data.DM_AND_MED_CHANGE_DECLINE_BUTTON):
            self.click(data.DM_AND_MED_CHANGE_DECLINE_BUTTON)
        # And Gather icon invisible
        if not self.is_element_present(data.DM_AND_OPTIONS_MENU_BTN):
            self.do_until_true(lambda: self.press('Back'), lambda: self.is_element_present(data.DM_AND_OPTIONS_MENU_BTN) or self.is_element_present(data.DM_AND_WELCOME_ENTER))
        if self.is_element_present(data.DM_AND_WELCOME_ENTER):
            return
        self.do_until_true(lambda: self.click(data.DM_AND_OPTIONS_MENU_BTN), lambda: self.is_element_present(data.DM_AND_OPTIONS_SETTINGS))
        self.click(data.DM_AND_OPTIONS_SETTINGS)
        self.do_until_true(lambda: self.swipe_up(), lambda: self.is_element_present(data.DM_AND_SETTINGS_LOG_OUT))
        self.click(data.DM_AND_SETTINGS_LOG_OUT)
        self.verify(data.DM_AND_WELCOME_ENTER)

    def signup(self, email):
        # Finish a simple sign up for the given email
        if self.is_element_present(data.DM_AND_WELCOME_ENTER):
            self.click(data.DM_AND_WELCOME_ENTER)
        self.verify(data.DM_AND_SIGN_IN_FIELD)
        self.enter(email, data.DM_AND_SIGN_IN_FIELD)
        self.click(data.DM_AND_SIGN_IN_BUTTON)
        self.verify(data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.enter('123456', data.DM_AND_SET_PASSWORD_PASSWORD_FIELD)
        self.enter('123456', data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.click(data.DM_AND_SET_PASSWORD_BUTTON)
        self.verify(data.DM_AND_PERSONAL_INFO_CELL_NUMBER)
        self.click(data.DM_AND_PERSONAL_INFO_BUTTON)
        self.verify(data.DM_AND_LOVED_ONE_SKIP_BUTTON)
        self.click(data.DM_AND_LOVED_ONE_SKIP_BUTTON)
        self.verify(data.DM_AND_SET_MEALTIME_BRK)
        self.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)
        self.verify(data.DM_AND_USER_AGREE_CHECK_BOX)
        self.click(data.DM_AND_USER_AGREE_CHECK_BOX)
        self.click(data.DM_AND_USER_AGREE_SIGN_IN_BUTTON)
        try:
            self.verify(data.DM_AND_TUTORIAL_TITLE_1)
            self.press('Back')
            return
        except NoSuchElementException:
            self.verify(data.DM_AND_MED_CHANGE_DECLINE_BUTTON)
            return
        
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
        self.press('Home')
        self.start_app()
        self.wait_until_present(data.DM_AND_MED_CHANGE_CONFIRM_BUTTON)
        self.click(data.DM_AND_MED_CHANGE_CONFIRM_BUTTON)
        try:
            self.verify(data.DM_AND_GOAL_DATE)
        except NoSuchElementException:
            self.verify(data.DM_AND_TUTORIAL_TITLE_1)
            self.press('Back')
            self.verify(data.DM_AND_GOAL_DATE)
        self.press('Back', 2)
        self.start_app()
        self.verify(data.DM_AND_GOAL_DATE)


