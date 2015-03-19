#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.alert import Alert
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
from time import sleep, time
from Nurse_A.Platform.web import Web

SERVER = {
    "Stag0" : "http://stag0.gatherhealth.com/provider/",
    "Stag1" : "https://stag1.gatherhealth.com/provider",
    "Stag2" : "https://stag2.gatherhealth.com/provider",
    "Production" : "https://www.gatherhealth.com/provider",
}

LOGIN_TITLE = u'Gather \u22c5 Login'

class WEB(Web):
    
    def __init__(self, browser = "Firefox", server = "Stag0"):
        # Create a session with different Browser
        if browser == 'Firefox':
            self.driver = webdriver.Firefox(timeout = 3000)
        elif browser == 'Chrome':
            self.driver = webdriver.Chrome(timeout = 3000)
        elif browser == 'Safari':
            self.driver = webdriver.Safari(timeout = 3000)
        elif browser == 'IE':
            self.driver = webdriver.Ie(timeout = 3000)
        # Open the webpage
        self.HOMEPAGE = SERVER[server]
        self.driver.get(self.HOMEPAGE)
        
    def login(self, ACCOUNT, PASSWORD):
        # Log in with the account and password
        if self.title == LOGIN_TITLE:
            self.enter(ACCOUNT, 'id_username')
            self.enter(PASSWORD, 'id_password')
            self.click('input[name="submit"]')
            self.verify('.feed')
        
    def logout(self):
        # Log out
        if not self.title == LOGIN_TITLE:
            self.driver.get(self.HOMEPAGE)
            # If an alert pops up, accept it.
            try:
                Alert(self.driver).accept()
            except:
                pass
            self.click('.dropdown-toggle .avatar')
            self.click('[href="/provider/logout?next=/provider/"]')
            self.verify('.forgotpw')

    def create_new_patient(self):
        # Create a new patient
        self.driver.get(self.HOMEPAGE)
        # If an alert pops up, accept it.
        try:
            Alert(self.driver).accept()
        except:
            pass
        self.click('.normal .add a')
        TIME_STRING = str(int(time()))
        SURNAME = 'test' + TIME_STRING
        GIVENAME = 'test'
        EMAIL = SURNAME + '@test.com'
        CELL_NUM = '1234567890'
        self.enter(SURNAME, 'input[name="last_name"]')
        self.enter(GIVENAME, 'input[name="first_name"]')
        self.select('United States (+1)', 'select[name="phone1_country"]')
        self.enter(CELL_NUM, 'input[name="phone1"]')
        self.enter(EMAIL, 'input[name="email"]')
        self.select('English', 'select[name="language"]')
        self.click('input[name="sex"]')
        self.click('#premium_trial_subscription')
        self.click('input.full_width')
        self.verify('button.final')
        self.click('button.final')
        self.verify('.id')
        return EMAIL
        
