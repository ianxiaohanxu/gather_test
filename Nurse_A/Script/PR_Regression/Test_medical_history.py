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
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
from time import sleep, time
import unittest, datetime
from Nurse_A.Settings import keycode, constant, data, setup
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case

class Medical_history(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        self.demo = setup.demo_data
        
    def tearDown(self):
        # self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
        
    def calc_age(self, birthday):
        birthday = datetime.datetime.strptime(birthday, '%Y-%m-%d')
        age = datetime.datetime.today() - birthday
        age = age.days / 365
        return str(age)
    
    def fill_all_data(self, gender, dob, dia_type, other_str, year):
        self.pr.select(gender, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.pr.driver.execute_script("document.getElementsByClassName('medical_history')[0].getElementsByClassName('row')[2].getElementsByClassName('group')[2].getElementsByTagName('input')[0].value='%s'" %dob)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CC)
        if self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE) == '':
            self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE_YEAR).is_enabled())
        self.pr.select(dia_type, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE_YEAR).is_enabled())
        self.pr.driver.execute_script('document.getElementsByName("diagnosis_date")[0].value="%s"' %dob)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_YEAR)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_YEAR)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_YEAR)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_YEAR)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_YEAR)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC_YEAR)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM_YEAR)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH_YEAR)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_OTHER)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_NEUR)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_NEPH)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_RETI)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOT)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO_YEAR)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE_YEAR)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC_YEAR).is_enabled())
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC_YEAR).is_enabled())
        self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC_YEAR)
        if (gender == '1' or gender == '2'):
            self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM_YEAR).is_enabled())
            self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM)
            self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM_YEAR).is_enabled())
            self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM_YEAR)
            self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP_YEAR).is_enabled())
            self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP)
            self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP_YEAR).is_enabled())
            self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP_YEAR)
        if (gender == '0' or gender == '2'):
            self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA_YEAR).is_enabled())
            self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA)
            self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA_YEAR).is_enabled())
            self.pr.select(year, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA_YEAR)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SMOKE)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ALCO)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_EXER)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DIET)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DRUG)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MARI)
        if (gender == '1' or gender == '2'):
            self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PREG)
            self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_BIRTH)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SEX)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_STD)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DIAB_HIS)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_HIS)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_HIS)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_HIS)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CANC_HIS)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_HIS)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_HIS)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ADMI)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SURG)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MEDI)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOD)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_LATEX)
        self.pr.enter(other_str, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ENVI)
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_BUT)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_OK)
        
    def verify_data(self, gender, dob, dia_type, other_str, year):
        if other_str == '':
            str_year = ''
        else:
            str_year = year
        self.assertEqual(gender, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER))
        self.assertEqual(dob, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DOB))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CC))
        self.assertEqual(dia_type, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE))
        self.assertEqual(dob, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSYC_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ANEM_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ASTH_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_OTHER))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_NEUR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_NEPH))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_RETI))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOT))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_COLO_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MOLE_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC))
        self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_VACC_YEAR))
        if (gender == '1' or gender == '2'):
            self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM))
            self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM_YEAR))
            self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP))
            self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP_YEAR))
        if (gender == '0' or gender == '2'):
            self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA))
            self.assertEqual(str_year, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA_YEAR))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SMOKE))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ALCO))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_EXER))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DIET))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DRUG))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MARI))
        if (gender == '1' or gender == '2'):
            self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PREG))
            self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_BIRTH))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SEX))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_STD))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DIAB_HIS))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_HYPE_HIS))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_DYSL_HIS))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_THYR_HIS))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CANC_HIS))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD_HIS))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVA_HIS))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ADMI))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SURG))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MEDI))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_FOOD))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_LATEX))
        self.assertEqual(other_str, self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_ENVI))
        
    def clear_all_data(self):
        gender = self.pr.text(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        for field in data.PR_PATIENT_RECORD_MEDICAL_HISTORY_FIELDLIST:
            try:
                self.pr.clear(field)
            except NoSuchElementException:
                if (gender == '0' and field in \
                    [data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP, \
                    data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PREG, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_BIRTH]):
                    pass
                elif (gender == '1' and field == data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA):
                    pass
                else:
                    raise NoSuchElementException
                
    def data_sync_check(self, gender, dob, dia_type, year):
        gender_str = {
                      '0':'Male', '1':'Female', '2':'Other',
                     }
        type_str = {
                    '0':'Pre-diabetic', '1':'Type 1', '2':'Type 2', '3':'Other', '4':'Gestational',
                   }
        self.pr.select(gender, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)  
        self.pr.driver.execute_script("document.getElementsByClassName('medical_history')[0].getElementsByClassName('row')[2].getElementsByClassName('group')[2].getElementsByTagName('input')[0].value='%s'" %dob)  
        self.pr.select(dia_type, data.PR_PATIENT_RECORD_MEDICAL_HISTORY_TYPE)
        self.pr.driver.execute_script('document.getElementsByName("diagnosis_date")[0].value="%s"' %year)
        self.pr.enter('others', data.PR_PATIENT_RECORD_MEDICAL_HISTORY_CVD)
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_BUT)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_OK)
        patient_info = self.pr.text(data.PR_INFO_PATIENT_DATA)
        patient_info = patient_info.split(',')
        age = self.calc_age(dob)
        year = self.calc_age(year)
        self.assertTrue(gender_str[gender] in patient_info[0])
        self.assertTrue(age in patient_info[1])
        self.assertTrue(type_str[dia_type] in patient_info[2])
        self.assertTrue(year in patient_info[2])
        self.pr.refresh()
        self.pr.verify(data.PR_INFO_PATIENT_DATA)
        patient_info = self.pr.text(data.PR_INFO_PATIENT_DATA)
        patient_info = patient_info.split(',')
        if gender == '2':
            self.assertTrue('N/A' in patient_info[0])
        else:
            self.assertTrue(gender_str[gender] in patient_info[0])
        self.assertTrue(age in patient_info[1])
        self.assertTrue(type_str[dia_type] in patient_info[2])
        if dia_type != '3':
            self.assertTrue(year in patient_info[2])
        
        
    def test_urgent_fill_all_data(self):
        '''
        111063
        This test is for '111063 Fill all fields in Medical History tab'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.fill_all_data('2', '1987-01-02', '1', 'abc', '2010')
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.verify_data('2', '1987-01-02', '1', 'abc', '2010')
        
    def test_urgent_edit_all_data(self):
        '''
        111065
        This test is for '111065 Fill all fields in Medical History tab'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.fill_all_data('2', '1987-01-02', '1', 'abc', '2010')
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.clear_all_data()
        self.fill_all_data('0', '1987-01-09', '4', 'abcd', '2011')
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.verify_data('0', '1987-01-09', '4', 'abcd', '2011')
        
    def test_normal_delete_data(self):
        '''
        111064
        This test is for '111064 Delete data in Medical History tab'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.fill_all_data('2', '1987-01-02', '1', 'abc', '2010')
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.clear_all_data()
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_BUT)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_SAVE_OK)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.verify_data('2', '1987-01-02', '1', '', '2010')
        
    def test_normal_gender_fields(self):
        '''
        111066
        This test is for '111066 Different fields shown according to gender info'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        
        # Check Male fields
        self.pr.select('0', data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM).is_displayed())
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP).is_displayed())
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PREG).is_displayed())
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_BIRTH).is_displayed())
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA).is_displayed())
        
        # Check Female fields
        self.pr.select('1', data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM).is_displayed())
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP).is_displayed())
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PREG).is_displayed())
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_BIRTH).is_displayed())
        self.assertFalse(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA).is_displayed())
        
        # Check Other fields
        self.pr.select('2', data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_MAMM).is_displayed())
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PAP).is_displayed())
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PREG).is_displayed())
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_BIRTH).is_displayed())
        self.assertTrue(self.pr.focus(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_PSA).is_displayed())
        
    def test_normal_data_sync(self):
        '''
        111067 111004
        This test is for '111067 Sync data from Medical History tab'
        This test is for '111004 Modify patient gender'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_MEDICAL_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_MEDICAL_HISTORY_GENDER)
        self.data_sync_check('0', '1986-07-08', '0', '2010-01-01')
        self.data_sync_check('1', '1986-07-08', '1', '2010-01-01')
        self.data_sync_check('2', '1986-07-08', '2', '2010-01-01')
        self.data_sync_check('0', '1986-07-08', '3', '2010-01-01')
        self.data_sync_check('0', '1986-07-08', '4', '2010-01-01')
        
if __name__ == '__main__':
    unittest.main()