#!/usr/bin/env python
# -*- coding: utf-8 -*-
import base64
import requests, urllib2, urllib
import simplejson as json
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
    
    def __init__(self, browser = "Firefox", server = data.SERVER):
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
            if self.is_element_present(data.PR_TUTORIAL_WELCOME):
                self.click(data.PR_TUTORIAL_WELCOME_CLOSE)
                self.verify(data.PR_TUTORIAL_TOOLTIP_HELP)
                self.click(data.PR_TUTORIAL_TOOLTIP_HELP_CLOSE)
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
            self.verify(data.PR_NAV_OPTION_MENU)
            self.click(data.PR_NAV_OPTION_MENU)
            self.click(data.PR_NAV_OPTION_MENU_LOGOUT)
            try:
                Alert(self.driver).accept()
            except:
                pass
            self.verify(data.PR_LOGIN_FORGOT_PASSWORD, 20)

    def request_interface(self, url, method, parameter=None, security=data.SECURITY_KEY):
        method = method.upper()
        if method not in ['GET', 'POST', 'DELETE']:
            raise Exception('Method %s not yet supported.' % method)
        full_url = '%s%s' %(data.HOST, url)
        auth = 'Basic %s' %security
        req = urllib2.Request(full_url)
        req.add_header('Authorization', auth)
        if parameter != None:
            req.add_data(urllib.urlencode(parameter))
        if method == 'DELETE':
            req.get_method = lambda: 'DELETE'
        response = urllib2.urlopen(req)
        return response
        
                                 
    def generate_test_demo(self, billing=True, 
        country=data.INDIA, bg_unit=data.MG_DL, 
        height_unit=data.CM, validity=12, 
        language=data.ENGLISH, demo_conf=data.DEMO_TEST
    ):
        demo_data = {
            'doctor_name':      'doctor_test',
            'nurse_name':       'nurse_test',
            'bg_units':         bg_unit,
            'height_units':     height_unit,
            'language_code':    language,
            'country':          country,
            'period':           validity,
            'data':             demo_conf,
            'billing_enabled':  billing,
            'notes':            'abc'
        }
        
        demo_conf = self.request_interface('/api/v1/demo.json', 'POST', parameter=demo_data)
        assert (demo_conf.code == 200)
        demo_conf = eval(demo_conf.read())
        # Grab the password
        assert 'key' in demo_conf
        assert 'id' in demo_conf
        return demo_conf['key'], demo_conf['id']
        
    def create_new_practice(self, billing=True, 
        country=data.INDIA, language=data.ENGLISH, 
        role='0',
    ):
        INFO = self.generate_info()
        practice_data = {
            'admin_name':       'Alex',
            'admin_email':      INFO['email'],
            'practice_name':    INFO['surname'],
            'language':         language,
            'country':          country,
            'billing_enabled':  billing,
            'role':             role,
        }
        
        practice_conf = self.request_interface('/api/v1/practices.json', 'POST', parameter=practice_data)
        assert (practice_conf.code == 200)
        practice_conf = eval(practice_conf.read())
        import pdb;pdb.set_trace()
        
    def delete_test_demo(self, demo_id):
        demo_id = str(demo_id)
        url = '/api/v1/demo/%s.json' %demo_id
        response = self.request_interface(url, 'DELETE')
        assert (response.code == 204)
                                 
    def create_new_patient(self, email=None):
        # Create a new patient
        self.driver.get(self.HOMEPAGE)
        # If an alert pops up, accept it.
        try:
            Alert(self.driver).accept()
        except:
            pass
        self.click(data.PR_NAV_ADD_PATIENT)
        self.verify(data.PR_ADD_PATIENT_SURNAME)
        INFO = self.generate_info()
        self.enter(INFO['surname'], data.PR_ADD_PATIENT_SURNAME)
        self.enter(INFO['givename'], data.PR_ADD_PATIENT_GIVENAME)
        self.click(data.PR_ADD_PATIENT_GENDER_MALE)
        self.select('1', data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.enter(INFO['us_cell'], data.PR_ADD_PATIENT_P_NUMBER)
        self.click(data.PR_ADD_PATIENT_APP_PATIENT)
        self.verify(data.PR_ADD_PATIENT_EMAIL)
        if email is None:
            self.enter(INFO['email'], data.PR_ADD_PATIENT_EMAIL)
        else:
            self.enter(email, data.PR_ADD_PATIENT_EMAIL)
        self.select('en', data.PR_ADD_PATIENT_LANGUAGE)
        if self.is_element_present(data.PR_ADD_PATIENT_PREMIUM_TRIAL):
            self.click(data.PR_ADD_PATIENT_PREMIUM_TRIAL)
        self.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.verify(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.click(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.verify(data.PR_PATIENT_RECORD_ID, 20)
        ID = self.text(data.PR_PATIENT_RECORD_ID)
        return INFO['email'], ID
        
    def create_new_EHR_patient(self):
        # Create a new EHR patient
        self.driver.get(self.HOMEPAGE)
        # If an alert pops up, accept it.
        try:
            Alert(self.driver).accept()
        except:
            pass
        self.click(data.PR_NAV_ADD_PATIENT)
        self.verify(data.PR_ADD_PATIENT_SURNAME)
        INFO = self.generate_info()
        self.enter(INFO['surname'], data.PR_ADD_PATIENT_SURNAME)
        self.enter(INFO['givename'], data.PR_ADD_PATIENT_GIVENAME)
        self.click(data.PR_ADD_PATIENT_GENDER_MALE)
        self.select('1', data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.enter(INFO['us_cell'], data.PR_ADD_PATIENT_P_NUMBER)
        self.click(data.PR_ADD_PATIENT_NORMAL_PATIENT)
        self.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.verify(data.PR_PATIENT_RECORD_ID, 20)
        ID = self.text(data.PR_PATIENT_RECORD_ID)
        return ID
        
    def delete_patient(self, id):
        # Delete a patient by id
        self.driver.get(data.DIRECTORY_PATH)
        # If an alert pops up, accept it.
        try:
            Alert(self.driver).accept()
        except:
            pass
        self.verify(data.PR_DIRECTORY_PATIENT_ENTRY %id)
        self.click(data.PR_DIRECTORY_PATIENT_DELETE %id)
        self.verify(data.PR_DIRECTORY_REMOVE_CONFIRM)
        self.click(data.PR_DIRECTORY_REMOVE_CONFIRM)
        self.wait_until_not(data.PR_DIRECTORY_PATIENT_ENTRY %id)
                    
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
        interval = int(data_str.split(',')[-1].split('of')[-1].split()[0])
        year = str(localtime().tm_year - interval)
        return year
    
    def get_birthday(self):
        # Return patient's birthday
        self.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DOB)
        dob = self.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DOB)
        return dob
        
    def get_age(self):
        # Return patient's age
        data_str = self.text(data.PR_INFO_PATIENT_DATA)
        age =  data_str.split(',')[1].split()[1]
        return age
        
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
        
    def get_billing(self):
        # Return billing time and rate
        self.click(data.PR_PATIENT_RECORD_BILLING)
        self.verify(data.PR_PATIENT_RECORD_BILLING_OVERVIEW)
        month = self.text(data.PR_PATIENT_RECORD_BILLING_FIRST_M)
        rate = self.text(data.PR_PATIENT_RECORD_BILLING_FIRST_R)[1:]
        return [month, rate]
        
    def get_bg_range(self):
        # Return BG range
        pre = self.text(data.PR_PATIENT_RECORD_PRE_MEAL_RANGE).split(' - ')
        post = self.text(data.PR_PATIENT_RECORD_POST_MEAL_RANGE).split(' - ')
        return pre + post
        
    def get_bg_goals(self):
        # Return BG goals
        goals = []
        self.click(data.PR_PATIENT_RECORD_SMBG)
        self.verify(data.PR_PATIENT_RECORD_SMBG_TITLE)
        for day in data.WEEKDAY:
            for mealtime in data.MEAL:
                for pre_post in data.PRE_POST:
                    where = day + '_' + pre_post + '_' + mealtime
                    if self.is_selected(where):
                        goals.append(1)
                    else:
                        goals.append(0)
            where = day + '_' + data.NIGHT
            if self.is_selected(where):
                goals.append(1)
            else:
                goals.append(0)
        self.click(data.PR_BG_GOALS_CLOSE_BUTTON)
        return goals
        
    def get_med_goals(self):
        # Return MED goals
        goals = []
        self.click(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.verify(data.PR_PRESCRIPTION_VISIBLE_ENTRY)
        entries = self.find(data.PR_PRESCRIPTION_ENTRY)
        entries.pop(0)
        for entry in entries:
            goal = []
            name = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_NAME).get_attribute('value')
            goal.append(name)
            med_type = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_TYPE).get_attribute('value')
            goal.append(med_type)
            if entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_STRENGTH).is_displayed():
                strength = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_STRENGTH).get_attribute('value')
            else:
                strength = ''
            goal.append(strength)
            unit = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_UNIT).get_attribute('value')
            goal.append(unit)
            instruction = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_INSTRUCTION).get_attribute('value')
            goal.append(instruction)
            pre_post = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_PRE_POST).get_attribute('value')
            goal.append(pre_post)
            frequency = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_FREQUENCY).get_attribute('value')
            goal.append(frequency)
            bre = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_BRE).get_attribute('value')
            goal.append(bre)
            lun = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_LUN).get_attribute('value')
            goal.append(lun)
            din = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_DIN).get_attribute('value')
            goal.append(din)
            nig = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_NIG).get_attribute('value')
            goal.append(nig)
            tim = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_TIME).get_attribute('value')
            goal.append(tim)
            if tim != '':
                specific_time = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_TIME).get_attribute('value')
            else:
                specific_time = ''
            goal.append(specific_time)
            goals.append(goal)
        self.click(data.PR_PRESCRIPTION_CLOSE)
        return goals    
            
    def get_data(self):
        data = []
        data.append(self.get_surname())
        data.append(self.get_givename())
        data.append(self.get_gender())
        data.append(self.get_birthday())
        data.append(self.get_age())
        data.append(self.get_country_code())
        data.append(self.get_number())
        data.append(self.get_email())        
        data.extend(self.get_billing())
        data.append(self.get_type())
        data.append(self.get_year())
        #data.append(self.get_comorbidities())
        data.append(self.get_notes())
        data.extend(self.get_bg_range())
        data.append(self.get_bg_goals())
        data.append(self.get_med_goals())
        data.append(self.get_other_med())
        return data        
        
        
    def fill_dosage(self, value, where, element = None):
        # Fill 'value' into 'where', if the 'value' is not equal to 0.
        if element is None:
            if value != 0:
                self.enter(value, where)
        else:
            if value != 0:
                element.find_element_by_css_selector(where).send_keys(value)
            
    def add_med_goals(self, goals):
        # Add med goals with list 'goals'
        self.verify(data.PR_PRESCRIPTION_VISIBLE_ENTRY)
        for goal in goals:
            index = goals.index(goal)
            entry = self.find(data.PR_PRESCRIPTION_ENTRY)[index+1]
            entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_NAME).send_keys(goal[0])
            dropdown = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_TYPE)
            Select(dropdown).select_by_value(goal[1])
            if goal[2] != '':
                entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_STRENGTH).send_keys(goal[2])
            dropdown = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_UNIT)
            Select(dropdown).select_by_value(goal[3])
            entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_INSTRUCTION).send_keys(goal[4])
            dropdown = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_PRE_POST)
            Select(dropdown).select_by_value(goal[5])
            dropdown = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_FREQUENCY)
            Select(dropdown).select_by_value(goal[6])
            if goal[7] != '':
                entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_BRE).send_keys(goal[7])
            if goal[8] != '':
                entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_LUN).send_keys(goal[8])
            if goal[9] != '':
                entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_DIN).send_keys(goal[9])
            if goal[10] != '':
                entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_NIG).send_keys(goal[10])
            if goal[11] != '':
                entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_TIME).send_keys(goal[11])
                dropdown = entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_TIME)
                Select(dropdown).select_by_value(goal[12])
            if index < (len(goals)-1):
                self.click(data.PR_PRESCRIPTION_ADD_NEW)
        self.click(data.PR_PRESCRIPTION_SAVE)
        self.verify(data.PR_PRESCRIPTION_CONFIRM_DIALOG)
        self.click(data.PR_PRESCRIPTION_CONFIRM_SAVE)
        self.wait_until_not(data.PR_PRESCRIPTION_CONFIRM_DIALOG)
                
    def clear_message_event(self):
        # Clear all message events by 'x'    
        self.driver.get(data.FEED_PATH)
        # If an alert pops up, accept it.
        try:
            Alert(self.driver).accept()
        except:
            pass
        self.verify(data.PR_FEED_CONTENT)
        if self.is_element_present(data.PR_FEED_FIRST_MESSAGE):
            Messages = self.find(data.PR_FEED_FIRST_MESSAGE)
            for item in Messages:
                item.find_element_by_css_selector(data.PR_FEED_CLOSE).click()
                
    def same_list(self, list_a, list_b):
        # Compare two lists, judge if they have the same elements.
        if (type(list_a) != list or type(list_b) != list):
            raise Exception('same_list only accept "list" as parameters')
        for item in list_a:
            if item not in list_b:
                return False
        for item in list_b:
            if item not in list_a:
                return False
        return True
