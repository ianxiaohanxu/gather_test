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
from time import sleep, time, localtime
from Nurse_A.Platform.web import Web
from Nurse_A.Settings import data


class WEB(Web):
    
    def __init__(self, browser = "Firefox", server = data.Stag0):
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
        self.HOMEPAGE = server
        self.driver.get(self.HOMEPAGE)
        
    def generate_info(self):
        # Generate first name, last name, email, cell number
        TIME_STRING = str(int(time()))
        SURNAME = 'test' + TIME_STRING
        GIVENAME = 'test'
        EMAIL = SURNAME + '@test.com'
        CELL_NUM_US = '1234567890'
        CELL_NUM_IN = '1234567890'
        CELL_NUM_CH = '12345678900'
        CELL_NUM_HK = '12345678'
        return {'surname' : SURNAME, 'givename' : GIVENAME, 
                'email' : EMAIL, 'us_cell' : CELL_NUM_US, 
                'in_cell' : CELL_NUM_IN, 'ch_cell' : CELL_NUM_CH, 'hk_cell' : CELL_NUM_HK,}
               
    def login(self, ACCOUNT, PASSWORD):
        # Log in with the account and password
        if self.title == data.PR_LOGIN_TITLE:
            self.enter(ACCOUNT, data.PR_LOGIN_USERNAME)
            self.enter(PASSWORD, data.PR_LOGIN_PASSWORD)
            self.click(data.PR_LOGIN_SUBMIT)
            self.verify(data.PR_NAV_FEED)
        
    def logout(self):
        # Log out
        if not self.title == data.PR_LOGIN_TITLE:
            self.driver.get(self.HOMEPAGE)
            # If an alert pops up, accept it.
            try:
                Alert(self.driver).accept()
            except:
                pass
            self.click(data.PR_NAV_OPTION_MENU)
            self.click(data.PR_NAV_OPTION_MENU_LOGOUT)
            self.verify(data.PR_LOGIN_FORGOT_PASSWORD)

    def create_new_patient(self):
        # Create a new patient
        self.driver.get(self.HOMEPAGE)
        # If an alert pops up, accept it.
        try:
            Alert(self.driver).accept()
        except:
            pass
        self.click('.normal .add a')
        INFO = self.generate_info()
        self.enter(INFO['surname'], 'input[name="last_name"]')
        self.enter(INFO['givename'], 'input[name="first_name"]')
        self.select('United States (+1)', 'select[name="phone1_country"]')
        self.enter(INFO['us_cell'], 'input[name="phone1"]')
        self.enter(INFO['email'], 'input[name="email"]')
        self.select('English', 'select[name="language"]')
        self.click('input[name="sex"]')
        self.click('#premium_trial_subscription')
        self.click('input.full_width')
        self.verify('button.final')
        self.click('button.final')
        self.verify('.id')
        return EMAIL
        
    def delete_patient(self, id):
        # Delete a patient by id
        self.driver.get(data.DIRECTORY_PATH)
        self.click('//tr/td/a[@href="/provider/patient/%s"]/../../td[last()]/a' %id)
        self.verify(data.PR_DIRECTORY_REMOVE_CONFIRM)
        self.click(data.PR_DIRECTORY_REMOVE_CONFIRM)
        
    def get_surname(self):
        # Return patient surname from PR page
        name = self.text(data.PR_INFO_NAME)
        surname = name.split()[1]
        return surname
        
    def get_givename(self):
        # Return patient givename from PR page
        name = self.text(data.PR_INFO_NAME)
        givename = name.split()[0]
        return givename
        
    def get_gender(self):
        # Return patient gender from PR page
        data_str = self.text(data.PR_INFO_PATIENT_DATA)
        gender = data_str.split(',')[0]
        return gender
        
    def get_type(self):
        # Return patient diabetes type
        data_str = self.text(data.PR_INFO_PATIENT_DATA)
        dia_type = data_str.split(',')[-1].split('of')[0].strip()
        return dia_type
        
    def get_year(self):
        # Return the year when patient got diabetes
        data_str = self.text(data.PR_INFO_PATIENT_DATA)
        interval = int(data_str.split(',')[-1].split('of')[-1].split().[0])
        year = str(localtime().tm_year - interval)
        return year
        
    def get_comorbidities(self):
        # Return patient comorbidities
        elements = self.find(data.PR_INFO_COMORBIDITIES)
        return [i.text for i in elements]
        
    def get_other_med(self):
        # Return patient's other meds
        elements = self.find(data.PR_INFO_OTHER_MED)
        return [i.text for i in elements]
        
    def get_notes(self):
        # Return patient's notes
        notes = self.text(data.PR_INFO_NOTE)
        return notes
        
    def get_email(self):
        # Return patient's email address
        address = self.text(data.PR_INFO_EMAIL)
        return address
        
    def get_country_code(self):
        # Return patient's country code
        number = self.text(data.PR_INFO_NUMBER)
        return number.split()[0]
        
    def get_number(self):
        # Return patient's number
        number = self.text(data.PR_INFO_NUMBER)
        return number.split()[1]
        
        
        
        
