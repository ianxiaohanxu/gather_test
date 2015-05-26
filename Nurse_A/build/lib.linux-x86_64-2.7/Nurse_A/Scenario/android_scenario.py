#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Nurse_A.Platform.android import AND
from web_scenario import WEB
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from appium import webdriver

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
        
    def login(self, username = 'pt034@test.com', password = 'test'):
        # Log in with an exist patient account
        # If APP not logged in
        if self.is_element_present('intro_skip_button'):
            self.click('enter')
            self.verify('Sign in')
            self.enter(username, 'login_email_et')
            self.click('Next')
            self.verify('Confirm')
            self.enter(password, 'login_pwd_et')
            self.click('Sign In')
            self.verify('main_button0_text')
            
    def logout(self):
        # Log out from any view
        # If APP not logged in
        if self.is_element_present('intro_skip_button'):
            return
        # If APP logged in
        # And Gather icon invisible
        if not self.is_element_present('home'):
            self.do_until_true(self.press, 'Back', self.is_element_present, 'home')
        self.do_until_true(self.click, 'home', self.is_element_present, 'Settings')
        self.click('Settings')
        self.click('Log out')
        self.verify('enter')
        
    def get_new_patient_account(self, SERVER = 'Stag0', ACCOUNT = 'alex+01@gatherhealth.com', PASSWORD = '123456'):
        # Create a new patient and return the email
        pr = WEB(server = SERVER)
        pr.login(ACCOUNT, PASSWORD)
        PATIENT_EMAIL = pr.create_new_patient()
        pr.teardown()
        return PATIENT_EMAIL
