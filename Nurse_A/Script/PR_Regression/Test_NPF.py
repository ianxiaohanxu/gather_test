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
import unittest, datetime
from Nurse_A.Settings import keycode, constant, data, setup
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case

class Add_new_patient(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        self.demo = setup.demo_data
        
    def tearDown(self):
        self.pr.teardown()
        
    def calc_age(self, birthday):
        birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
        age = datetime.datetime.today() - birthday
        age = age.days / 365
        return str(age)
        
    def add_patient_with_full_info(self, account):
        # This test is for '101103 Invite a app patient with billing'
        self.pr.login(account, self.demo[0])
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.assertEqual(self.pr.text(data.PR_ADD_PATIENT_TITLE), data.ADD_PATIENT)
        INFO = self.pr.generate_info()
        PUSH = []
        self.pr.enter(INFO['surname'], data.PR_ADD_PATIENT_SURNAME)
        PUSH.append(INFO['surname'])
        self.pr.enter(INFO['givename'], data.PR_ADD_PATIENT_GIVENAME)
        PUSH.append(INFO['givename'])
        self.pr.click(data.PR_ADD_PATIENT_GENDER_MALE)
        PUSH.append('Male')
        dob = '2000-01-01'
        self.pr.driver.execute_script('document.getElementsByName("dob")[0].value="%s"' %dob)
        age = self.calc_age(dob)
        PUSH.append(dob)
        PUSH.append(age)
        self.pr.select('1', data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        PUSH.append('+1')
        self.pr.enter(INFO['us_cell'], data.PR_ADD_PATIENT_P_NUMBER)
        PUSH.append(INFO['us_cell'])
        self.pr.click(data.PR_ADD_PATIENT_APP_PATIENT)
        self.pr.enter(INFO['email'], data.PR_ADD_PATIENT_EMAIL)
        PUSH.append(INFO['email'])
        self.pr.select('en', data.PR_ADD_PATIENT_LANGUAGE)    
        self.pr.select('3', data.PR_ADD_PATIENT_BILL_TIME)
        PUSH.append('3')
        self.pr.clear(data.PR_ADD_PATIENT_BILL_RATE)
        self.pr.enter('5', data.PR_ADD_PATIENT_BILL_RATE)
        PUSH.append('5.00')
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.select('1', data.PR_ADD_PATIENT_PATIENT_TYPE)
        PUSH.append('Type 1')
        self.pr.driver.execute_script('document.getElementsByName("diagnosis_date")[0].value="2010-01-01"')
        PUSH.append('2010-01-01')
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
        self.pr.verify(data.PR_PRESCRIPTION_DIALOG)
        self.pr.add_med_goals(data.MED_GOALS)
        PUSH.append(data.MED_GOALS)
        self.pr.verify(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.enter('ccc\n', data.PR_ADD_PATIENT_OTHER_MED)
        self.pr.enter('ddd\n', data.PR_ADD_PATIENT_OTHER_MED)
        PUSH.append(['ccc', 'ddd'])
        self.pr.click(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_ID)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        PULL = self.pr.get_data()
        self.assertEqual(PUSH, PULL)
        # Delete the patient
        ID = self.pr.text(data.PR_PATIENT_RECORD_ID)
        self.pr.delete_patient(ID)
        self.pr.logout()
        
    def add_nobilling_patient(self, account):
        # This test is for '101001 Invite a patient without billing'
        self.pr.login(account, self.demo[0])
        self.pr.create_new_patient()
        # Delete the patient
        ID = self.pr.text(data.PR_PATIENT_RECORD_ID)
        self.pr.delete_patient(ID)
        self.pr.logout()
        
    '''
    Since HKID is removed, we don't need this test case.
    '''
    # def test_urgent_add_hk_patient_with_hkid(self):
    #     # This test is for '198015 Add a new HK patient with HKID'
    #     self.pr.login(data.HK_DOCTOR, self.demo[0])
    #     self.pr.click(data.PR_NAV_ADD_PATIENT)
    #     self.assertEqual(self.pr.text(data.PR_ADD_PATIENT_TITLE), data.ADD_PATIENT)
    #     INFO = self.pr.generate_info()
    #     self.pr.enter(INFO['surname'], data.PR_ADD_PATIENT_SURNAME)
    #     self.pr.enter(INFO['givename'], data.PR_ADD_PATIENT_GIVENAME)
    #     self.pr.click(data.PR_ADD_PATIENT_GENDER_MALE)
    #     self.pr.select('1', data.PR_ADD_PATIENT_P_COUNTRY_CODE)
    #     self.pr.enter(INFO['us_cell'], data.PR_ADD_PATIENT_P_NUMBER)
    #     self.pr.click(data.PR_ADD_PATIENT_APP_PATIENT)
    #     self.pr.enter(INFO['email'], data.PR_ADD_PATIENT_EMAIL)
    #     self.pr.select('en', data.PR_ADD_PATIENT_LANGUAGE)
    #     self.pr.click(data.PR_ADD_PATIENT_HAS_HKID_YES)
    #     self.pr.verify(data.PR_ADD_PATIENT_HKID)
    #     self.pr.enter(data.HKID, data.PR_ADD_PATIENT_HKID)
    #     self.pr.enter(data.HKID_CHECK, data.PR_ADD_PATIENT_HKID_CHECK)
    #     self.pr.click(data.PR_ADD_PATIENT_PREMIUM_TRIAL)
    #     self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
    #     self.pr.verify(data.PR_ADD_PATIENT_FINAL_BUTTON)
    #     self.pr.click(data.PR_ADD_PATIENT_FINAL_BUTTON)
    #     self.pr.verify(data.PR_PATIENT_RECORD_ID)
    #     ID = self.pr.text(data.PR_PATIENT_RECORD_ID)
    #     # Delete the patient
    #     self.pr.delete_patient(ID)
    
    def test_urgent_add_patient_with_full_info(self):
        '''
        101103 101112
        This test is for '101103 Invite a app patient with billing'
        This test is for '101112 Verify patient data after invitation'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.add_patient_with_full_info(data.DOCTOR)
        self.add_patient_with_full_info(data.NURSE)
        
    def test_urgent_add_nobilling_patient(self):
        '''
        101101
        This test is for '101101 Invite a app patient without billing'
        '''
        self.demo = self.pr.generate_test_demo(demo_conf='4098', billing=False)
        self.add_nobilling_patient(data.DOCTOR)
        self.add_nobilling_patient(data.NURSE)
        self.pr.delete_test_demo(self.demo[1])
        
    def test_urgent_add_patient_with_required_info(self):
        '''
        101105 109012
        This test is for '101105 Invite a app patient without fill optional fields'
                         '109012 Delete patient record'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        # Delete the patient
        self.pr.delete_patient(INFO[1])
    
    def test_urgent_add_ehr_patient_in_billing_practice(self):
        '''
        101104
        This test is for '101104 Invite a normal patient with billing'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        ID = self.pr.create_new_EHR_patient()
        # Delete the patient
        self.pr.delete_patient(ID)
        
    def test_urgent_add_ehr_patient_in_non_billing_practice(self):
        '''
        101102
        This test is for '101102 Invite a normal patient without billing'
        '''
        self.demo = self.pr.generate_test_demo(billing=False)
        self.pr.login(data.DOCTOR, self.demo[0])
        ID = self.pr.create_new_EHR_patient()
        # Delete the patient
        self.pr.delete_patient(ID)
        self.pr.delete_test_demo(self.demo[1])
        
    def test_normal_validation_for_normal_patient_field(self):
        '''
        101108
        This test is for '101108 Validation check for inviting a normal patient fields'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.pr.verify(data.PR_ADD_PATIENT_SURNAME)
        
        # Validation check for empty fields
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 4)
        self.assertEqual(data.EM_PR_NPF_EMPTY_SURNAME, errors[0].text)
        self.assertEqual(data.EM_PR_NPF_EMPTY_GIVEN_NAME, errors[1].text)
        self.assertEqual(data.EM_PR_NPF_EMPTY_PATIENT_CELL, errors[2].text)
        self.assertEqual(data.EM_PR_NPF_EMPTY_GENDER, errors[3].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_SURNAME).get_attribute('class'))
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_GIVENAME).get_attribute('class'))
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_GENDER_MALE).get_attribute('class'))
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_GENDER_FEMALE).get_attribute('class'))
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        
        # Validation check for space name
        self.pr.enter(' ', data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter(' ', data.PR_ADD_PATIENT_GIVENAME)
        self.pr.click(data.PR_ADD_PATIENT_GENDER_MALE)
        self.pr.enter('abcdefghij', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 2)
        self.assertEqual(data.EM_PR_NPF_EMPTY_SURNAME, errors[0].text)
        self.assertEqual(data.EM_PR_NPF_EMPTY_GIVEN_NAME, errors[1].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_SURNAME).get_attribute('class'))
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_GIVENAME).get_attribute('class'))
        self.assertTrue('invalid' not in self.pr.focus(data.PR_ADD_PATIENT_GENDER_MALE).get_attribute('class'))
        self.assertTrue('invalid' not in self.pr.focus(data.PR_ADD_PATIENT_GENDER_FEMALE).get_attribute('class'))
        self.assertTrue('invalid' not in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        
        # Validation check for letter number
        self.pr.enter('surname', data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter('givename', data.PR_ADD_PATIENT_GIVENAME)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_P_NUMBER, errors[0].text)
        self.assertTrue('invalid' not in self.pr.focus(data.PR_ADD_PATIENT_SURNAME).get_attribute('class'))
        self.assertTrue('invalid' not in self.pr.focus(data.PR_ADD_PATIENT_GIVENAME).get_attribute('class'))
        self.assertTrue('invalid' not in self.pr.focus(data.PR_ADD_PATIENT_GENDER_MALE).get_attribute('class'))
        self.assertTrue('invalid' not in self.pr.focus(data.PR_ADD_PATIENT_GENDER_FEMALE).get_attribute('class'))
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        
        # Valication check for number length
        # US number
        self.pr.select(data.US_COUNTRY_CODE, data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.clear(data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter('123456789', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_P_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        self.pr.clear(data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter('12345678900', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_P_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        
        # HK number
        self.pr.select(data.HK_COUNTRY_CODE, data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.clear(data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter('1234567', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_P_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        self.pr.clear(data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter('123456789', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_P_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        
        # CH number
        self.pr.select(data.CH_COUNTRY_CODE, data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.clear(data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter('1234567890', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_P_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        self.pr.clear(data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter('123456789000', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_P_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        
        # IN number
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.clear(data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter('123456789', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_P_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        self.pr.clear(data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.enter('12345678900', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_P_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_P_NUMBER).get_attribute('class'))
        
    def test_normal_validation_for_app_user_fields(self):
        '''
        101107 101109 101110 
        This test is for '101107 Interrupt invite a app patient'
        This test is for '101109 Validation check for all required fileds during invite a app patient'
        This test is for '101110 Validation check for all optional fields during invite a app patient'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.pr.verify(data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter('surname', data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter('givename', data.PR_ADD_PATIENT_GIVENAME)
        self.pr.click(data.PR_ADD_PATIENT_GENDER_MALE)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.enter('1234567890', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_APP_PATIENT)
        self.pr.verify(data.PR_ADD_PATIENT_EMAIL)
        
        # Empty check
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        #self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        #errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        #self.assertEqual(len(errors), 1)
        #self.assertEqual(data.EM_PR_NPF_EMPTY_EMAIL, errors[0].text)
        self.pr.verify(data.PR_ADD_PATIENT_BILL_RATE_ERROR)
        self.assertEqual(data.EM_PR_NPF_EMPTY_MONTHLY_RATE, self.pr.text(data.PR_ADD_PATIENT_BILL_RATE_ERROR))
        #self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_EMAIL).get_attribute('class'))
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_BILL_RATE).get_attribute('class'))
        
        # Email format check
        self.pr.click(data.PR_ADD_PATIENT_PREMIUM_TRIAL)
        self.pr.enter('abcdef@.com', data.PR_ADD_PATIENT_EMAIL)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_EMAIL, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_EMAIL).get_attribute('class'))
        
        self.pr.clear(data.PR_ADD_PATIENT_EMAIL)
        self.pr.enter('abcdef@sss.', data.PR_ADD_PATIENT_EMAIL)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_EMAIL, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_EMAIL).get_attribute('class'))
        
        self.pr.clear(data.PR_ADD_PATIENT_EMAIL)
        self.pr.enter('f@s.s', data.PR_ADD_PATIENT_EMAIL)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_EMAIL, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_EMAIL).get_attribute('class'))
        
        # Validation check for loved one cell
        self.pr.clear(data.PR_ADD_PATIENT_EMAIL)
        self.pr.enter('test@test.com', data.PR_ADD_PATIENT_EMAIL)
        
        # Validation check for letter number
        self.pr.enter('abcdefghij', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_LO_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        
        # Valication check for number length
        # US number
        self.pr.select(data.US_COUNTRY_CODE, data.PR_ADD_PATIENT_L_COUNTRY_CODE)
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.enter('123456789', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_LO_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.enter('12345678900', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_LO_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        
        # HK number
        self.pr.select(data.HK_COUNTRY_CODE, data.PR_ADD_PATIENT_L_COUNTRY_CODE)
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.enter('1234567', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_LO_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.enter('123456789', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_LO_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        
        # CH number
        self.pr.select(data.CH_COUNTRY_CODE, data.PR_ADD_PATIENT_L_COUNTRY_CODE)
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.enter('1234567899', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_LO_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.enter('123456789000', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_LO_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        
        # IN number
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ADD_PATIENT_L_COUNTRY_CODE)
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.enter('123456789', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_LO_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.enter('12345678900', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_INVALID_LO_NUMBER, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        
        # Duplicate loved one number with patient's
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ADD_PATIENT_L_COUNTRY_CODE)
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.enter('1234567890', data.PR_ADD_PATIENT_L_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_DUPLICATE_NUMBER_WITH_PATIENT, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_L_NUMBER).get_attribute('class'))
        self.pr.clear(data.PR_ADD_PATIENT_L_NUMBER)
        
        # Duplicate email check
        time_str = str(int(time()))
        email = 'test'+time_str+'@test.com'
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_TITLE)
        self.pr.create_new_patient(email)
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.pr.verify(data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter('surname', data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter('givename', data.PR_ADD_PATIENT_GIVENAME)
        self.pr.click(data.PR_ADD_PATIENT_GENDER_MALE)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.enter('1234567890', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_APP_PATIENT)
        self.pr.verify(data.PR_ADD_PATIENT_EMAIL)
        self.pr.enter(email, data.PR_ADD_PATIENT_EMAIL)
        self.pr.click(data.PR_ADD_PATIENT_PREMIUM_TRIAL)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_BASIC_ERROR)
        errors = self.pr.find(data.PR_ADD_PATIENT_BASIC_ERROR)
        self.assertEqual(len(errors), 1)
        self.assertEqual(data.EM_PR_NPF_DUPLICATE_EMAIL, errors[0].text)
        self.assertTrue('invalid' in self.pr.focus(data.PR_ADD_PATIENT_EMAIL).get_attribute('class'))
        
    def test_normal_interrupt_normal_patient_invitation(self):
        '''
        101106
        This test is for '101106 Interrupt invite a normal patient'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.pr.verify(data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter('surname', data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter('givename', data.PR_ADD_PATIENT_GIVENAME)
        self.pr.click(data.PR_ADD_PATIENT_GENDER_MALE)
        self.pr.select(data.IN_COUNTRY_CODE, data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.enter('1234567890', data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_TITLE)
        
    def test_normal_correct_country_code(self):
        '''
        101111
        This test is for '101111 Change practice name check default country code during add new patient'
        '''
        self.pr.login(data.DOCTOR, setup.demo_data1[0])
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.pr.verify(data.PR_ADD_PATIENT_SURNAME)
        practice = self.pr.focus(data.PR_ADD_PATIENT_PRACTICE)
        Select(practice).select_by_index(1)
        country_code_1 = self.pr.text(data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        Select(practice).select_by_index(2)
        country_code_2 = self.pr.text(data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.assertFalse(country_code_1 == country_code_2)
              
    def test_normal_invite_patient_with_bp_weight_goals(self):
        '''
        This test is for "Invite a patient with BP goals"
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_NAV_ADD_PATIENT)
        self.pr.verify(data.PR_ADD_PATIENT_SURNAME)
        INFO = self.pr.generate_info()
        self.pr.enter(INFO['surname'], data.PR_ADD_PATIENT_SURNAME)
        self.pr.enter(INFO['givename'], data.PR_ADD_PATIENT_GIVENAME)
        self.pr.click(data.PR_ADD_PATIENT_GENDER_MALE)
        self.pr.select('1', data.PR_ADD_PATIENT_P_COUNTRY_CODE)
        self.pr.enter(INFO['us_cell'], data.PR_ADD_PATIENT_P_NUMBER)
        self.pr.click(data.PR_ADD_PATIENT_APP_PATIENT)
        self.pr.verify(data.PR_ADD_PATIENT_EMAIL)
        email = INFO['email']
        self.pr.enter(email, data.PR_ADD_PATIENT_EMAIL)
        self.pr.select('en', data.PR_ADD_PATIENT_LANGUAGE)
        if self.pr.is_element_present(data.PR_ADD_PATIENT_PREMIUM_TRIAL):
            self.pr.click(data.PR_ADD_PATIENT_PREMIUM_TRIAL)
        self.pr.click(data.PR_ADD_PATIENT_INVITE_BUTTON)
        self.pr.verify(data.PR_ADD_PATIENT_PATIENT_TYPE)
        self.pr.select('1', data.PR_ADD_PATIENT_PATIENT_TYPE)
        self.pr.driver.execute_script('document.getElementsByName("diagnosis_date")[0].value="2010-01-01"')
        self.pr.enter('abc', data.PR_ADD_PATIENT_PATIENT_NOTES)
        self.pr.select('80', data.PR_ADD_PATIENT_PRE_LOWER_LIMIT)
        self.pr.select('140', data.PR_ADD_PATIENT_PRE_UPPER_LIMIT)
        self.pr.select('80', data.PR_ADD_PATIENT_POST_LOWER_LIMIT)
        self.pr.select('140', data.PR_ADD_PATIENT_POST_UPPER_LIMET)
        self.pr.select(data.VALUE_AND_PATIENT_BPWEIGHT_FREQUENCY_DAILY, data.PR_ADD_PATIENT_BP_FREQUENCY)
        self.pr.verify(data.PR_ADD_PATIENT_BP_DAILY_TABLE)
        self.pr.click(data.PR_ADD_PATIENT_BP_EVERY_PRE_BRK)
        self.pr.click(data.PR_ADD_PATIENT_BP_EVERY_NIGHT)
        self.pr.enter('70', data.PR_ADD_PATIENT_WEIGHT_TARGET)
        self.pr.select(data.VALUE_AND_PATIENT_BPWEIGHT_FREQUENCY_DAILY, data.PR_ADD_PATIENT_WEIGHT_FREQUENCY)
        self.pr.verify(data.PR_ADD_PATIENT_WEIGHT_DAILY_TABLE)
        self.pr.select(data.VALUE_AND_PATIENT_BPWEIGHT_FREQUENCY_2WEEK, data.PR_ADD_PATIENT_WEIGHT_FREQUENCY)
        self.pr.select(data.WEEKDAY[0], data.PR_ADD_PATIENT_WEIGHT_WEEKDAY)
        self.assertTrue('Monday' in self.pr.text(data.PR_ADD_PATIENT_WEIGHT_NEXT_MEASURE_DAY))
        self.pr.verify(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.click(data.PR_ADD_PATIENT_FINAL_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_ID, 20)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_COUNTER)
        self.assertEqual(data.VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_1 %'14', self.pr.text(data.PR_PATIENT_RECORD_BP_COUNTER))
        self.assertEqual('70', self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_TARGET))
        self.assertEqual(data.VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_2, self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_COUNTER))


        
if __name__ == '__main__':
    unittest.main()
