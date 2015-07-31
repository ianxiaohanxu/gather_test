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
from Nurse_A.Settings import keycode, constant, data
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case

class Visit(Case):
    
    def setUp(self):
        self.pr = WEB(server = data.SERVER)
        self.pr.driver.maximize_window()
        
    def tearDown(self):
        self.pr.delete_test_demo(self.demo[1])
        self.pr.teardown()
        
    def enter_data(self, value, location, confirm_location):
        element = self.pr.focus(location)
        tag = element.tag_name
        if tag in ('input', 'textarea'):
            element.clear()
            element.send_keys(value)
        elif tag == 'select':
            self.pr.select(value, location)
        else:
            raise Exception('Tag "%s" is not supported.' %tag)
        self.pr.click(confirm_location)
        
    def delete_data(self, location):
        self.pr.click(location)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_DELETE_CONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_DELETE_CONFIRM_Y)
        self.pr.wait_until_not(data.PR_PATIENT_RECORD_VISIT_DELETE_CONFIRM)
    
    def select_one_day_in_last_month(self):
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_DATE)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_DATE_LAST_MONTH)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_DATE_LAST_MONTH)
        sleep(constant.INTERVAL_1)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_DATE_SOME_DAY)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        
    def delete_all_data(self):
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        delete_button_group = [
            data.PR_PATIENT_RECORD_VISIT_NOTES_DELETE,
            data.PR_PATIENT_RECORD_VISIT_HEIGHT_DELETE,
            data.PR_PATIENT_RECORD_VISIT_WEIGHT_DELETE,
            data.PR_PATIENT_RECORD_VISIT_WAIST_DELETE,
            data.PR_PATIENT_RECORD_VISIT_TEMPERATURE_DELETE,
            data.PR_PATIENT_RECORD_VISIT_BGROUP_DELETE,
            data.PR_PATIENT_RECORD_VISIT_RHBGROUP_DELETE,
            # data.PR_PATIENT_RECORD_VISIT_TOBACCO_DELETE,
            # data.PR_PATIENT_RECORD_VISIT_ALCOHOL_DELETE,
            # data.PR_PATIENT_RECORD_VISIT_EXERCISE_DELETE,
            # data.PR_PATIENT_RECORD_VISIT_DIET_DELETE,
            data.PR_PATIENT_RECORD_VISIT_EYE_DELETE,
            data.PR_PATIENT_RECORD_VISIT_FOOT_DELETE,
            data.PR_PATIENT_RECORD_VISIT_ALBUMIN_DELETE,
            data.PR_PATIENT_RECORD_VISIT_CREATININE_DELETE,
            data.PR_PATIENT_RECORD_VISIT_ACR_DELETE,
            data.PR_PATIENT_RECORD_VISIT_EGFR_DELETE,
            data.PR_PATIENT_RECORD_VISIT_BUN_DELETE,
            data.PR_PATIENT_RECORD_VISIT_URIC_DELETE,
            data.PR_PATIENT_RECORD_VISIT_TSH_DELETE,
            data.PR_PATIENT_RECORD_VISIT_T3_DELETE,
            data.PR_PATIENT_RECORD_VISIT_T4_DELETE,
            data.PR_PATIENT_RECORD_VISIT_BG_FASTING_DELETE,
            data.PR_PATIENT_RECORD_VISIT_BG_POST_DELETE,
            data.PR_PATIENT_RECORD_VISIT_BG_RANDOM_DELETE,
            data.PR_PATIENT_RECORD_VISIT_BP_DELETE,
            data.PR_PATIENT_RECORD_VISIT_HBA1C_DELETE,
            data.PR_PATIENT_RECORD_VISIT_HDL_DELETE,
            data.PR_PATIENT_RECORD_VISIT_LDL_DELETE,
            data.PR_PATIENT_RECORD_VISIT_VLDL_DELETE,
            data.PR_PATIENT_RECORD_VISIT_TRI_DELETE,
            data.PR_PATIENT_RECORD_VISIT_CALCIUM_DELETE,
            data.PR_PATIENT_RECORD_VISIT_VITB12_DELETE,
            data.PR_PATIENT_RECORD_VISIT_VITD_DELETE,
            data.PR_PATIENT_RECORD_VISIT_ECG_DELETE,
            data.PR_PATIENT_RECORD_VISIT_C_PEP_DELETE,
            data.PR_PATIENT_RECORD_VISIT_INSULIN_A_DELETE,
            data.PR_PATIENT_RECORD_VISIT_GAD_DELETE,
            data.PR_PATIENT_RECORD_VISIT_AST_DELETE,
            data.PR_PATIENT_RECORD_VISIT_ALT_DELETE,
            data.PR_PATIENT_RECORD_VISIT_PROTEIN_DELETE,
            data.PR_PATIENT_RECORD_VISIT_RBC_DELETE,
            data.PR_PATIENT_RECORD_VISIT_HB_DELETE,
            data.PR_PATIENT_RECORD_VISIT_HCT_DELETE,
            data.PR_PATIENT_RECORD_VISIT_MCV_DELETE,
            data.PR_PATIENT_RECORD_VISIT_MCH_DELETE,
            data.PR_PATIENT_RECORD_VISIT_MCHC_DELETE,
            data.PR_PATIENT_RECORD_VISIT_RDW_DELETE,
            data.PR_PATIENT_RECORD_VISIT_PLATELET_DELETE,
            data.PR_PATIENT_RECORD_VISIT_MPV_DELETE,
            data.PR_PATIENT_RECORD_VISIT_WBC_DELETE,
            data.PR_PATIENT_RECORD_VISIT_NEU_DELETE,
            data.PR_PATIENT_RECORD_VISIT_EOS_DELETE,
            data.PR_PATIENT_RECORD_VISIT_LYM_DELETE,
            data.PR_PATIENT_RECORD_VISIT_MON_DELETE,
            data.PR_PATIENT_RECORD_VISIT_BAS_DELETE,
        ]
        map(self.delete_data, delete_button_group)
        sleep(constant.INTERVAL_5)

        
    def verify_data(self, value, location):
        self.assertEqual(value, self.pr.text(location))
        
    def verify_all_data_empty(self):
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_HEIGHT)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_WEIGHT)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_WAIST)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_TEMPERATURE)
        self.verify_data('-1', data.PR_PATIENT_RECORD_VISIT_BGROUP)
        self.verify_data('-1', data.PR_PATIENT_RECORD_VISIT_RHBGROUP)
        # self.verify_data('-1', data.PR_PATIENT_RECORD_VISIT_TOBACCO)
        # self.verify_data('-1', data.PR_PATIENT_RECORD_VISIT_ALCOHOL)
        # self.verify_data('-1', data.PR_PATIENT_RECORD_VISIT_EXERCISE)
        # self.verify_data('-1', data.PR_PATIENT_RECORD_VISIT_DIET)
        self.verify_data('-1', data.PR_PATIENT_RECORD_VISIT_EYE)
        self.verify_data('-1', data.PR_PATIENT_RECORD_VISIT_FOOT)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_ALBUMIN)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_CREATININE)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_ACR)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_EGFR)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_BUN)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_URIC)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_TSH)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_T3)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_T4)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_BG_FASTING)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_BG_POST)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_BG_RANDOM)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_BP_SYS)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_BP_DIA)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_HBA1C)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_HDL)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_LDL)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_VLDL)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_TRI)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_CALCIUM)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_VITB12)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_VITD)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_ECG)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_C_PEP)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_INSULIN_A)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_GAD)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_AST)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_ALT)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_PROTEIN)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_RBC)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_HB)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_HCT)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_MCV)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_MCH)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_MCHC)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_RDW)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_PLATELET)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_MPV)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_WBC)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_NEU)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_EOS)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_LYM)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_MON)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_BAS)
        
    def full_fill_visit(self):
        # Full fill all data for the new visit
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.enter_data('abc', data.PR_PATIENT_RECORD_VISIT_NOTES, data.PR_PATIENT_RECORD_VISIT_NOTES_CONFIRM)
        self.enter_data('178', data.PR_PATIENT_RECORD_VISIT_HEIGHT, data.PR_PATIENT_RECORD_VISIT_HEIGHT_CONFIRM)
        self.enter_data('67', data.PR_PATIENT_RECORD_VISIT_WEIGHT, data.PR_PATIENT_RECORD_VISIT_WEIGHT_CONFIRM)
        self.enter_data('97', data.PR_PATIENT_RECORD_VISIT_WAIST, data.PR_PATIENT_RECORD_VISIT_WAIST_CONFIRM)
        self.enter_data('37', data.PR_PATIENT_RECORD_VISIT_TEMPERATURE, data.PR_PATIENT_RECORD_VISIT_TEMPERATURE_CONFIRM)
        self.enter_data('1', data.PR_PATIENT_RECORD_VISIT_BGROUP, data.PR_PATIENT_RECORD_VISIT_BGROUP_CONFIRM)
        self.enter_data('1', data.PR_PATIENT_RECORD_VISIT_RHBGROUP, data.PR_PATIENT_RECORD_VISIT_RHBGROUP_CONFIRM)
        # self.enter_data('1', data.PR_PATIENT_RECORD_VISIT_TOBACCO, data.PR_PATIENT_RECORD_VISIT_TOBACCO_CONFIRM)
        # self.enter_data('1', data.PR_PATIENT_RECORD_VISIT_ALCOHOL, data.PR_PATIENT_RECORD_VISIT_ALCOHOL_CONFIRM)
        # self.enter_data('1', data.PR_PATIENT_RECORD_VISIT_EXERCISE, data.PR_PATIENT_RECORD_VISIT_EXERCISE_CONFIRM)
        # self.enter_data('1', data.PR_PATIENT_RECORD_VISIT_DIET, data.PR_PATIENT_RECORD_VISIT_DIET_CONFIRM)
        self.enter_data('1', data.PR_PATIENT_RECORD_VISIT_EYE, data.PR_PATIENT_RECORD_VISIT_EYE_CONFIRM)
        self.enter_data('1', data.PR_PATIENT_RECORD_VISIT_FOOT, data.PR_PATIENT_RECORD_VISIT_FOOT_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_ALBUMIN, data.PR_PATIENT_RECORD_VISIT_ALBUMIN_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_CREATININE, data.PR_PATIENT_RECORD_VISIT_CREATININE_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_ACR, data.PR_PATIENT_RECORD_VISIT_ACR_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_EGFR, data.PR_PATIENT_RECORD_VISIT_EGFR_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_BUN, data.PR_PATIENT_RECORD_VISIT_BUN_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_URIC, data.PR_PATIENT_RECORD_VISIT_URIC_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_TSH, data.PR_PATIENT_RECORD_VISIT_TSH_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_T3, data.PR_PATIENT_RECORD_VISIT_T3_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_T4, data.PR_PATIENT_RECORD_VISIT_T4_CONFIRM)
        self.enter_data('123', data.PR_PATIENT_RECORD_VISIT_BG_FASTING, data.PR_PATIENT_RECORD_VISIT_BG_FASTING_CONFIRM)
        self.enter_data('123', data.PR_PATIENT_RECORD_VISIT_BG_POST, data.PR_PATIENT_RECORD_VISIT_BG_POST_CONFIRM)
        self.enter_data('123', data.PR_PATIENT_RECORD_VISIT_BG_RANDOM, data.PR_PATIENT_RECORD_VISIT_BG_RANDOM_CONFIRM)
        self.pr.enter('120', data.PR_PATIENT_RECORD_VISIT_BP_SYS)
        self.pr.enter('80', data.PR_PATIENT_RECORD_VISIT_BP_DIA)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_BP_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_HBA1C, data.PR_PATIENT_RECORD_VISIT_HBA1C_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_HDL, data.PR_PATIENT_RECORD_VISIT_HDL_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_LDL, data.PR_PATIENT_RECORD_VISIT_LDL_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_VLDL, data.PR_PATIENT_RECORD_VISIT_VLDL_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_TRI, data.PR_PATIENT_RECORD_VISIT_TRI_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_CALCIUM, data.PR_PATIENT_RECORD_VISIT_CALCIUM_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_VITB12, data.PR_PATIENT_RECORD_VISIT_VITB12_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_VITD, data.PR_PATIENT_RECORD_VISIT_VITD_CONFIRM)
        self.enter_data('abc', data.PR_PATIENT_RECORD_VISIT_ECG, data.PR_PATIENT_RECORD_VISIT_ECG_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_C_PEP, data.PR_PATIENT_RECORD_VISIT_C_PEP_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_INSULIN_A, data.PR_PATIENT_RECORD_VISIT_INSULIN_A_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_GAD, data.PR_PATIENT_RECORD_VISIT_GAD_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_AST, data.PR_PATIENT_RECORD_VISIT_AST_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_ALT, data.PR_PATIENT_RECORD_VISIT_ALT_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_PROTEIN, data.PR_PATIENT_RECORD_VISIT_PROTEIN_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_RBC, data.PR_PATIENT_RECORD_VISIT_RBC_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_HB, data.PR_PATIENT_RECORD_VISIT_HB_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_HCT, data.PR_PATIENT_RECORD_VISIT_HCT_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_MCV, data.PR_PATIENT_RECORD_VISIT_MCV_CONFIRM)
        self.enter_data('1.0', data.PR_PATIENT_RECORD_VISIT_MCH, data.PR_PATIENT_RECORD_VISIT_MCH_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_MCHC, data.PR_PATIENT_RECORD_VISIT_MCHC_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_RDW, data.PR_PATIENT_RECORD_VISIT_RDW_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_PLATELET, data.PR_PATIENT_RECORD_VISIT_PLATELET_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_MPV, data.PR_PATIENT_RECORD_VISIT_MPV_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_WBC, data.PR_PATIENT_RECORD_VISIT_WBC_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_NEU, data.PR_PATIENT_RECORD_VISIT_NEU_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_EOS, data.PR_PATIENT_RECORD_VISIT_EOS_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_LYM, data.PR_PATIENT_RECORD_VISIT_LYM_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_MON, data.PR_PATIENT_RECORD_VISIT_MON_CONFIRM)
        self.enter_data('5.0', data.PR_PATIENT_RECORD_VISIT_BAS, data.PR_PATIENT_RECORD_VISIT_BAS_CONFIRM)
        sleep(constant.INTERVAL_5)
        
        self.pr.refresh()
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_NEW_BUTTON).get_attribute('class'))
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_OLD_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE_EXPLAIN)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_AGGREGATE).get_attribute('class'))
        # Verify all data on Aggregate page
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.verify_data('178', data.PR_PATIENT_RECORD_VISIT_HEIGHT)
        self.verify_data('67', data.PR_PATIENT_RECORD_VISIT_WEIGHT)
        self.verify_data('97', data.PR_PATIENT_RECORD_VISIT_WAIST)
        self.verify_data('37', data.PR_PATIENT_RECORD_VISIT_TEMPERATURE)
        self.verify_data('1', data.PR_PATIENT_RECORD_VISIT_BGROUP)
        self.verify_data('1', data.PR_PATIENT_RECORD_VISIT_RHBGROUP)
        # self.verify_data('1', data.PR_PATIENT_RECORD_VISIT_TOBACCO)
        # self.verify_data('1', data.PR_PATIENT_RECORD_VISIT_ALCOHOL)
        # self.verify_data('1', data.PR_PATIENT_RECORD_VISIT_EXERCISE)
        # self.verify_data('1', data.PR_PATIENT_RECORD_VISIT_DIET)
        self.verify_data('1', data.PR_PATIENT_RECORD_VISIT_EYE)
        self.verify_data('1', data.PR_PATIENT_RECORD_VISIT_FOOT)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_ALBUMIN)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_CREATININE)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_ACR)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_EGFR)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_BUN)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_URIC)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_TSH)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_T3)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_T4)
        self.verify_data('123', data.PR_PATIENT_RECORD_VISIT_BG_FASTING)
        self.verify_data('123', data.PR_PATIENT_RECORD_VISIT_BG_POST)
        self.verify_data('123', data.PR_PATIENT_RECORD_VISIT_BG_RANDOM)
        self.verify_data('120', data.PR_PATIENT_RECORD_VISIT_BP_SYS)
        self.verify_data('80', data.PR_PATIENT_RECORD_VISIT_BP_DIA)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_HBA1C)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_HDL)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_LDL)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_VLDL)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_TRI)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_CALCIUM)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_VITB12)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_VITD)
        self.verify_data('abc', data.PR_PATIENT_RECORD_VISIT_ECG)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_C_PEP)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_INSULIN_A)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_GAD)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_AST)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_ALT)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_PROTEIN)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_RBC)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_HB)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_HCT)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_MCV)
        self.verify_data('1.0', data.PR_PATIENT_RECORD_VISIT_MCH)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_MCHC)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_RDW)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_PLATELET)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_MPV)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_WBC)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_NEU)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_EOS)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_LYM)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_MON)
        self.verify_data('5.0', data.PR_PATIENT_RECORD_VISIT_BAS)
        
    def test_urgent_empty_visit_ui(self):
        '''
        103001
        This test is for '103001 Visits view with no visits'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_NEW_BUTTON).get_attribute('class'))
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_OLD_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_EMPTY_HISTORY)
        
    def test_urgent_history_view_with_visits(self):
        '''
        103002
        This test is for '103002 Visits view with some visits'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        self.pr.click(data.PR_FEED_FIRST_WARNING)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_NEW_BUTTON).get_attribute('class'))
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_OLD_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_AGGREGATE).get_attribute('class'))
        
    def test_urgent_edit_visit_history(self):
        '''
        103004
        This test is for '103004 Edit history visit info'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_NEW_BUTTON).get_attribute('class'))
        self.enter_data('175', data.PR_PATIENT_RECORD_VISIT_HEIGHT, data.PR_PATIENT_RECORD_VISIT_HEIGHT_CONFIRM)
        self.enter_data('65', data.PR_PATIENT_RECORD_VISIT_WEIGHT, data.PR_PATIENT_RECORD_VISIT_WEIGHT_CONFIRM)
        self.pr.refresh()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_OLD_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_LATEST_HISTORY)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_LATEST_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_NOTES)
        self.pr.clear(data.PR_PATIENT_RECORD_VISIT_HEIGHT)
        self.enter_data('180', data.PR_PATIENT_RECORD_VISIT_HEIGHT, data.PR_PATIENT_RECORD_VISIT_HEIGHT_CONFIRM)
        self.pr.refresh()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_OLD_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_AGGREGATE).get_attribute('class'))
        self.assertEqual('180', self.pr.text(data.PR_PATIENT_RECORD_VISIT_HEIGHT))
        
    def test_urgent_add_a_new_visit(self):
        '''
        103008
        This test is for '103008 Add a new visit'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_NEW_BUTTON).get_attribute('class'))
        self.full_fill_visit()
        
    def test_urgent_delete_data(self):
        '''
        103016
        This test is for '103016 Delete button'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_NEW_BUTTON).get_attribute('class'))
        self.full_fill_visit()
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_LATEST_HISTORY)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_LATEST_HISTORY)
        self.delete_all_data()
        self.pr.refresh()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_OLD_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_AGGREGATE).get_attribute('class'))
        self.verify_all_data_empty()
        
    def test_urgent_aggregate_update(self):
        '''
        103013
        This test is for '103013 Aggregate by updating visit history'
        '''
        self.demo = self.pr.generate_test_demo()
        self.pr.login(data.DOCTOR, self.demo[0])
        INFO = self.pr.create_new_patient()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_NEW_BUTTON).get_attribute('class'))
        # Input data for today
        self.enter_data('150', data.PR_PATIENT_RECORD_VISIT_HEIGHT, data.PR_PATIENT_RECORD_VISIT_HEIGHT_CONFIRM)
        self.enter_data('0', data.PR_PATIENT_RECORD_VISIT_EYE, data.PR_PATIENT_RECORD_VISIT_EYE_CONFIRM)
        # Input data for some day in last month
        self.select_one_day_in_last_month()
        self.enter_data('aaa', data.PR_PATIENT_RECORD_VISIT_NOTES, data.PR_PATIENT_RECORD_VISIT_NOTES_CONFIRM)
        self.enter_data('160', data.PR_PATIENT_RECORD_VISIT_HEIGHT, data.PR_PATIENT_RECORD_VISIT_HEIGHT_CONFIRM)
        self.enter_data('aaa', data.PR_PATIENT_RECORD_VISIT_ECG, data.PR_PATIENT_RECORD_VISIT_ECG_CONFIRM)
        # Input data for some day in the month befor last month
        self.select_one_day_in_last_month()
        self.enter_data('1', data.PR_PATIENT_RECORD_VISIT_EYE, data.PR_PATIENT_RECORD_VISIT_EYE_CONFIRM)
        self.enter_data('bbb', data.PR_PATIENT_RECORD_VISIT_ECG, data.PR_PATIENT_RECORD_VISIT_ECG_CONFIRM)
        self.enter_data('50', data.PR_PATIENT_RECORD_VISIT_WEIGHT, data.PR_PATIENT_RECORD_VISIT_WEIGHT_CONFIRM)
        sleep(constant.INTERVAL_5)
        # Verify data in aggregate page
        self.pr.refresh()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_OLD_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE_EXPLAIN)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_AGGREGATE).get_attribute('class'))
        self.verify_data('150', data.PR_PATIENT_RECORD_VISIT_HEIGHT)
        self.verify_data('0', data.PR_PATIENT_RECORD_VISIT_EYE)
        self.verify_data('aaa', data.PR_PATIENT_RECORD_VISIT_ECG)
        self.verify_data('50', data.PR_PATIENT_RECORD_VISIT_WEIGHT)
        # Edit data in history entry
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_LATEST_HISTORY)
        sleep(constant.INTERVAL_5)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_NOTES)
        self.enter_data('155', data.PR_PATIENT_RECORD_VISIT_HEIGHT, data.PR_PATIENT_RECORD_VISIT_HEIGHT_CONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_SECOND_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.enter_data('165', data.PR_PATIENT_RECORD_VISIT_HEIGHT, data.PR_PATIENT_RECORD_VISIT_HEIGHT_CONFIRM)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_THIRD_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.enter_data('2', data.PR_PATIENT_RECORD_VISIT_EYE, data.PR_PATIENT_RECORD_VISIT_EYE_CONFIRM)
        self.enter_data('ccc', data.PR_PATIENT_RECORD_VISIT_ECG, data.PR_PATIENT_RECORD_VISIT_ECG_CONFIRM)
        self.enter_data('55', data.PR_PATIENT_RECORD_VISIT_WEIGHT, data.PR_PATIENT_RECORD_VISIT_WEIGHT_CONFIRM)
        sleep(constant.INTERVAL_5)
        # Verify data in aggregate page
        self.pr.refresh()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_OLD_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE_EXPLAIN)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_AGGREGATE).get_attribute('class'))
        self.verify_data('155', data.PR_PATIENT_RECORD_VISIT_HEIGHT)
        self.verify_data('0', data.PR_PATIENT_RECORD_VISIT_EYE)
        self.verify_data('aaa', data.PR_PATIENT_RECORD_VISIT_ECG)
        self.verify_data('55', data.PR_PATIENT_RECORD_VISIT_WEIGHT)
        # Edit data in history entry
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_LATEST_HISTORY)
        sleep(constant.INTERVAL_5)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_NOTES)
        self.delete_data(data.PR_PATIENT_RECORD_VISIT_EYE_DELETE)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_SECOND_HISTORY)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_SECOND_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.delete_data(data.PR_PATIENT_RECORD_VISIT_HEIGHT_DELETE)
        self.delete_data(data.PR_PATIENT_RECORD_VISIT_ECG_DELETE)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_THIRD_HISTORY)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_THIRD_HISTORY)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.delete_data(data.PR_PATIENT_RECORD_VISIT_WEIGHT_DELETE)
        # Verify data in aggregate page
        self.pr.refresh()
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_TAG)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_ECG)
        self.pr.click(data.PR_PATIENT_RECORD_VISIT_OLD_BUTTON)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE_EXPLAIN)
        self.pr.verify(data.PR_PATIENT_RECORD_VISIT_AGGREGATE)
        self.assertTrue('active' in self.pr.focus(data.PR_PATIENT_RECORD_VISIT_AGGREGATE).get_attribute('class'))
        self.verify_data('155', data.PR_PATIENT_RECORD_VISIT_HEIGHT)
        self.verify_data('2', data.PR_PATIENT_RECORD_VISIT_EYE)
        self.verify_data('ccc', data.PR_PATIENT_RECORD_VISIT_ECG)
        self.verify_data('', data.PR_PATIENT_RECORD_VISIT_WEIGHT)
        
if __name__ == '__main__':
    unittest.main()