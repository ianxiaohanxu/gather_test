#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
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

class Patient_record(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        self.demo = setup.demo_data
        
    def tearDown(self):
        # self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
    
    def test_urgent_add_med_goals(self):
        '''
        111014 111015 111016 111060 111061
        This test is for '111014 Add new medication - with a exist medication name'
        This test is for '111015 Add new medication - with a non exist medication name'
        This test is for '111016 add new medication - with different type
        This test is for '111060 add new medication - with different units
        This test is for '111061 add new medication - with different Frequency'
        '''
        now = datetime.datetime.now()
        date_str = now.strftime('%b %d, %Y')
        if date_str[4] == '0':
            date_str = date_str.replace('0', '', 1)
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.pr.click(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.pr.verify(data.PR_PRESCRIPTION_DIALOG)
        self.pr.add_med_goals(data.MED_GOALS)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_INFO)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_PRESCRIPTION_UNCONFIRM)
        goals = self.pr.get_med_goals()
        self.pr.same_list(goals, data.MED_GOALS)
        self.pr.click(data.PR_PATIENT_RECORD_SUMMARY_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_SUMMARY_MED_LAST_HISTORY)
        self.assertEqual(date_str, self.pr.text(data.PR_PATIENT_RECORD_SUMMARY_MED_LAST_HISTORY))

    def test_urgent_add_bg_goals(self):
        '''
        111020 111021
        This test is for '111020 Add BG Goals'
        This test is for '111021 Edit BG Goals'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_SMBG)
        self.pr.click(data.PR_PATIENT_RECORD_SMBG)
        self.pr.verify(data.PR_PATIENT_RECORD_SMBG_TITLE)
        map(self.pr.click, data.PR_ADD_PATIENT_EVERY)
        self.pr.click(data.PR_BG_GOALS_SAVE_BUTTON)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_SMBG_TITLE)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_INFO)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.assertTrue('49' in self.pr.text(data.PR_PATIENT_RECORD_SMBG_COUNTER))
        self.pr.click(data.PR_PATIENT_RECORD_SMBG)
        self.pr.verify(data.PR_PATIENT_RECORD_SMBG_TITLE)
        self.pr.click(data.PR_ADD_PATIENT_EVERY_PRE_BRK)
        self.pr.click(data.PR_ADD_PATIENT_EVERY_NIGHT)
        self.pr.click(data.PR_BG_GOALS_SAVE_BUTTON)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_SMBG_TITLE)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_INFO)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.assertTrue('35' in self.pr.text(data.PR_PATIENT_RECORD_SMBG_COUNTER))

    def test_urgent_delete_med_goals(self):
        '''
        111017
        This test is for '111017 delete medication'
        '''
        original_goals = [
                          ['G1', '2', '', '4', 'abc', '8', '0', '5', '6', '5', '5', '5', '09:00'],
                          ['ABC', '4', '5', '1', 'abc', '9', '0', '5', '5', '5', '5', '5', '20:00'],
                         ]
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.pr.click(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.pr.verify(data.PR_PRESCRIPTION_DIALOG)
        self.pr.add_med_goals(original_goals)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_INFO)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_PRESCRIPTION_UNCONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.pr.verify(data.PR_PRESCRIPTION_DIALOG)
        deletes = self.pr.find(data.PR_PRESCRIPTION_ENTRY_DELETE)
        deletes[-1].click()
        lunch_amounts = self.pr.find(data.PR_PRESCRIPTION_ENTRY_DOSAGE_LUN)
        lunch_amounts[-1].clear()
        self.pr.click(data.PR_PRESCRIPTION_SAVE)
        self.pr.verify(data.PR_PRESCRIPTION_CONFIRM_DIALOG)
        self.pr.click(data.PR_PRESCRIPTION_CONFIRM_SAVE)
        self.pr.wait_until_not_present(data.PR_PRESCRIPTION_CONFIRM_DIALOG)
        goals = self.pr.get_med_goals()
        original_goals = original_goals[:-1]
        original_goals[-1][8] = ''
        self.assertEqual(goals, original_goals)
        
    def test_normal_medication_sort(self):
        '''
        111062
        This test is for '111062 Medication sort'
        '''
        MED_GOALS = [
            ['G2', '6', '5', '1', 'abc', '8', '0', '5', '6', '5', '5', '5', '09:00'],
            ['G1', '2', '', '4', 'abc', '8', '0', '5', '6', '5', '5', '5', '09:00'],
            ['G3', '3', '5', '1', 'abc', '8', '0', '5', '6', '5', '5', '5', '09:00'],
            ['G4', '9', '5', '1', 'abc', '8', '0', '5', '6', '5', '5', '5', '09:00'],
        ]
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.pr.click(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.pr.verify(data.PR_PRESCRIPTION_DIALOG)
        self.pr.add_med_goals(MED_GOALS)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_INFO)
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_PRESCRIPTION_UNCONFIRM)
        med_names = self.pr.find(data.PR_PATIENT_RECORD_MEDICATION_NAMES)
        med_names = [item.text for item in med_names]
        self.assertEqual(med_names, ['G1', 'G2', 'G3', 'G4'])
        
    def test_normal_prescription_validation(self):
        '''
        111019
        This test is for '111019 validation check during add medication goals'
        '''
        # self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.pr.click(data.PR_PATIENT_RECORD_PRESCRIPTION)
        self.pr.verify(data.PR_PRESCRIPTION_DIALOG)
        entry = self.pr.find(data.PR_PRESCRIPTION_ENTRY)[1]
        
        # Check validation message for Medication name
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_TYPE).click()
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_REQUIRED)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_NAME).send_keys('abc')
        
        # Check validation message for Medication type
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_STRENGTH).click()
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_REQUIRED)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        Select(entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_TYPE)).select_by_value('3')
        
        # Check validation message for Medication strength
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_UNIT).click()
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_STRENGTH)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_STRENGTH).send_keys('5')
        
        # Check validation message for Medication unit
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_PRE_POST).click()
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_REQUIRED)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        Select(entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_UNIT)).select_by_value('1')
        
        # Check validation message for Medication timing
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_FREQUENCY).click()
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_REQUIRED)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        Select(entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_PRE_POST)).select_by_value('8')
        
        # Check validation message for Medication frequency
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_BRE).click()
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_REQUIRED)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        Select(entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_FREQUENCY)).select_by_value('0')
        
        # Check validation message for Medication dosage
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_BRE).send_keys('abc')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_BRE).clear()
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_BRE).send_keys('0\t')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE_NON_ZERO)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_BRE).clear()
        
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_LUN).send_keys('abc')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_LUN).clear()
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_LUN).send_keys('0\t')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE_NON_ZERO)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_LUN).clear()
        
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_DIN).send_keys('abc')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_DIN).clear()
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_DIN).send_keys('0\t')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE_NON_ZERO)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_DIN).clear()
        
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_NIG).send_keys('abc')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_NIG).clear()
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_NIG).send_keys('0\t')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE_NON_ZERO)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_NIG).clear()
        
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_TIME).send_keys('abc')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_TIME).clear()
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_TIME).send_keys('0\t')
        self.pr.verify(data.PR_PRESCRIPTION_ENTRY_VALIDATION)
        self.assertEqual(self.pr.text(data.PR_PRESCRIPTION_ENTRY_VALIDATION), data.EM_PR_PRESCRIPTION_DOSAGE_NON_ZERO)
        self.assertFalse(self.pr.focus(data.PR_PRESCRIPTION_SAVE).is_enabled())
        entry.find_element_by_css_selector(data.PR_PRESCRIPTION_ENTRY_DOSAGE_TIME).clear()
        
    def test_normal_edit_patient_name(self):
        '''
        111003
        This test is for '111003 Modify patient name'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.verify(data.PR_PATIENT_RECORD_NAME)
        self.pr.click(data.PR_PATIENT_RECORD_NAME)
        self.pr.verify(data.PR_PATIENT_RECORD_NAME_DIALOG)
        self.pr.clear(data.PR_PATIENT_RECORD_NAME_SURNAME)
        self.pr.enter('patient_surname', data.PR_PATIENT_RECORD_NAME_SURNAME)
        self.pr.clear(data.PR_PATIENT_RECORD_NAME_GIVEN_NAME)
        self.pr.enter('patient_given', data.PR_PATIENT_RECORD_NAME_GIVEN_NAME)
        self.pr.click(data.PR_PATIENT_RECORD_NAME_SAVE)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_NAME_DIALOG)
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_NAME)
        self.assertTrue('patient_given'+' '+'patient_surname' in self.pr.text(data.PR_PATIENT_RECORD_NAME))
        self.pr.driver.get(data.DIRECTORY_PATH)
        self.pr.verify(data.PR_DIRECTORY_FIRST_PATIENT)
        last_name = [item.text for item in self.pr.find(data.PR_DIRECTORY_LAST_NAME)]
        first_name = [item.text for item in self.pr.find(data.PR_DIRECTORY_FIRST_NAME)]
        self.assertTrue('patient_surname' in last_name)
        self.assertTrue('patient_given' in first_name)

    def test_urgent_add_bp_goals(self):
        '''
        This test is for 'Add BP goals'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_NONE)
        self.pr.click(data.PR_PATIENT_RECORD_BP_NONE)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_DIALOG)
        self.assertEqual(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_NEVER, self.pr.text(data.PR_PATIENT_RECORD_BP_DIALOG_FREQUENCY))
        self.pr.select(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_DAILY, data.PR_PATIENT_RECORD_BP_DIALOG_FREQUENCY)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_DIALOG_DAILY_TABLE)
        self.pr.click(data.PR_PATIENT_RECORD_BP_DIALOG_EVERY_PRE_LUN)
        self.pr.click(data.PR_PATIENT_RECORD_BP_DIALOG_EVERY_PRE_DIN)
        self.pr.click(data.PR_PATIENT_RECORD_BP_DIALOG_EVERY_NIGHT)
        self.pr.click(data.PR_PATIENT_RECORD_BP_DIALOG_SAVE_BTN)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BP_DIALOG)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_COUNTER)
        self.assertEqual(data.VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_1 %'21', self.pr.text(data.PR_PATIENT_RECORD_BP_COUNTER))

        self.pr.click(data.PR_PATIENT_RECORD_BP_COUNTER)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_DIALOG)
        self.assertEqual(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_DAILY, self.pr.text(data.PR_PATIENT_RECORD_BP_DIALOG_FREQUENCY))
        self.pr.select(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_2WEEK, data.PR_PATIENT_RECORD_BP_DIALOG_FREQUENCY)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_DIALOG_WEEKDAY)
        self.pr.select(data.WEEKDAY[2], data.PR_PATIENT_RECORD_BP_DIALOG_WEEKDAY)
        self.assertTrue('Wednesday' in self.pr.text(data.PR_PATIENT_RECORD_BP_DIALOG_NEXT_DAY))
        self.pr.click(data.PR_PATIENT_RECORD_BP_DIALOG_SAVE_BTN)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BP_DIALOG)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_COUNTER)
        self.assertEqual(data.VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_2, self.pr.text(data.PR_PATIENT_RECORD_BP_COUNTER))

        self.pr.click(data.PR_PATIENT_RECORD_BP_COUNTER)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_DIALOG)
        self.assertEqual(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_2WEEK, self.pr.text(data.PR_PATIENT_RECORD_BP_DIALOG_FREQUENCY))
        self.pr.select(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_4WEEK, data.PR_PATIENT_RECORD_BP_DIALOG_FREQUENCY)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_DIALOG_WEEKDAY)
        self.pr.select(data.WEEKDAY[4], data.PR_PATIENT_RECORD_BP_DIALOG_WEEKDAY)
        self.assertTrue('Friday' in self.pr.text(data.PR_PATIENT_RECORD_BP_DIALOG_NEXT_DAY))
        self.pr.click(data.PR_PATIENT_RECORD_BP_DIALOG_SAVE_BTN)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BP_DIALOG)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_COUNTER)
        self.assertEqual(data.VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_3, self.pr.text(data.PR_PATIENT_RECORD_BP_COUNTER))

        self.pr.click(data.PR_PATIENT_RECORD_BP_COUNTER)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_DIALOG)
        self.assertEqual(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_4WEEK, self.pr.text(data.PR_PATIENT_RECORD_BP_DIALOG_FREQUENCY))
        self.pr.select(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_NEVER, data.PR_PATIENT_RECORD_BP_DIALOG_FREQUENCY)
        self.pr.click(data.PR_PATIENT_RECORD_BP_DIALOG_SAVE_BTN)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_BP_DIALOG)
        self.pr.verify(data.PR_PATIENT_RECORD_BP_NONE)
        
    def test_urgent_add_weight_goals(self):
        '''
        This test is for 'Add Weight goals'
        '''
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_INFO)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_NONE)
        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_NONE)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_DIALOG)
        self.assertEqual(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_NEVER, self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_FREQUENCY))
        self.pr.select(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_DAILY, data.PR_PATIENT_RECORD_WEIGHT_DIALOG_FREQUENCY)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_DAILY_TABLE)
        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_EVERY_PRE_BRK)
        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_EVERY_PRE_LUN)
        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_EVERY_PRE_DIN)
        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_EVERY_NIGHT)
        self.pr.enter('70', data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET)
        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_SAVE_BTN)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_WEIGHT_DIALOG)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_COUNTER)
        self.assertEqual(data.VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_1 %'28', self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_COUNTER))
        self.assertEqual('70', self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_TARGET))

        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_COUNTER)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_DIALOG)
        self.assertEqual(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_DAILY, self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_FREQUENCY))
        self.assertEqual('70', self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET))
        self.pr.select(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_2WEEK, data.PR_PATIENT_RECORD_WEIGHT_DIALOG_FREQUENCY)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_WEEKDAY)
        self.pr.select(data.WEEKDAY[0], data.PR_PATIENT_RECORD_WEIGHT_DIALOG_WEEKDAY)
        self.assertTrue('Monday' in self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_NEXT_DAY))
        self.pr.clear(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET)
        self.pr.enter('80', data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET)
        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_SAVE_BTN)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_WEIGHT_DIALOG)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_COUNTER)
        self.assertEqual(data.VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_2, self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_COUNTER))
        self.assertEqual('80', self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_TARGET))

        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_COUNTER)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_DIALOG)
        self.assertEqual(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_2WEEK, self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_FREQUENCY))
        self.assertEqual('80', self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET))
        self.pr.select(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_4WEEK, data.PR_PATIENT_RECORD_WEIGHT_DIALOG_FREQUENCY)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_WEEKDAY)
        self.pr.select(data.WEEKDAY[1], data.PR_PATIENT_RECORD_WEIGHT_DIALOG_WEEKDAY)
        self.assertTrue('Tuesday' in self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_NEXT_DAY))
        self.pr.clear(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET)
        self.pr.enter('90', data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET)
        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_SAVE_BTN)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_WEIGHT_DIALOG)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_COUNTER)
        self.assertEqual(data.VALUE_PATIENT_RECORD_BPWEIGHT_FREQUENCY_3, self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_COUNTER))
        self.assertEqual('90', self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_TARGET))

        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_COUNTER)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_DIALOG)
        self.assertEqual(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_4WEEK, self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_FREQUENCY))
        self.assertEqual('90', self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET))
        self.pr.select(data.VALUE_PATIENT_BPWEIGHT_FREQUENCY_NEVER, data.PR_PATIENT_RECORD_WEIGHT_DIALOG_FREQUENCY)
        self.pr.clear(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET)
        self.pr.enter('100', data.PR_PATIENT_RECORD_WEIGHT_DIALOG_TARGET)
        self.pr.click(data.PR_PATIENT_RECORD_WEIGHT_DIALOG_SAVE_BTN)
        self.pr.wait_until_not_present(data.PR_PATIENT_RECORD_WEIGHT_DIALOG)
        self.pr.verify(data.PR_PATIENT_RECORD_WEIGHT_NONE)
        self.assertEqual('100', self.pr.text(data.PR_PATIENT_RECORD_WEIGHT_TARGET))


if __name__ == '__main__':
    unittest.main()
        
