#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time
import datetime
import unittest
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case
from Nurse_A.Scenario.android_scenario import ANDROID
from Nurse_A.Settings import keycode, constant, data, setup, mobile_setup

class Settings(Case):

    def setUp(self):
        self.phone = ANDROID()

    def tearDown(self):
        self.phone.logout()
        self.phone.turn_on_wifi()
        self.phone.teardown()

    def _generate_numbers(self, length):
        short_number = ''
        for i in range(length-1):
            short_number += '1'
        long_number = ''
        for i in range(length+1):
            long_number += '1'
        return short_number, long_number

    def _validation_for_number(self, number, number_location, error_location, button):
        self.phone.clear(number_location)
        self.phone.enter(number, number_location)
        self.phone.hide_keyboard()
        self.phone.click(button)
        self.phone.verify(error_location)
        self.assertEqual(data.EM_DM_PERSONAL_INFO_INVALID_NUMBER, self.phone.text(error_location))

    def _validation_check_for_number(self, country_code, length, country_code_location, number_location, error_location, button):
        self.phone.click(country_code_location)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_COUNTRY_HK)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_COUNTRY_IN)
        self.phone.click(country_code)
        short_number, long_number = self._generate_numbers(length)
        self._validation_for_number(short_number, number_location, error_location, button)
        self._validation_for_number(long_number, number_location, error_location, button)

    def test_urgent_invite_lo(self):
        '''
        This is the test for "Add a new lo"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_MANAGE_LO)
        self.phone.click(data.DM_AND_OPTIONS_MANAGE_LO)
        self.phone.verify(data.DM_AND_LOVED_ONE_LIST_DESCRIPTION)
        self.phone.click(data.DM_AND_LOVED_ONE_LIST_ADD_BTN)
        self.phone.verify(data.DM_AND_LOVED_ONE_LAST_NAME)
        self.phone.click(data.DM_AND_LOVED_ONE_CLOSE_ICON)
        self.phone.verify(data.DM_AND_LOVED_ONE_LIST_ADD_ICON)
        self.phone.click(data.DM_AND_LOVED_ONE_LIST_ADD_ICON)
        self.phone.verify(data.DM_AND_LOVED_ONE_LAST_NAME)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_LOVED_ONE_INVITE_BTN))
        self.phone.enter('test', data.DM_AND_LOVED_ONE_LAST_NAME)
        self.phone.enter('lo', data.DM_AND_LOVED_ONE_FIRST_NAME)
        self.phone.enter(patient['email'].replace('test', 'lo'), data.DM_AND_LOVED_ONE_EMAIL)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_LOVED_ONE_COUNTRY_CODE)
        self.phone.verify(data.DM_AND_LOVED_ONE_COUNTRY_HK)
        self.phone.verify(data.DM_AND_LOVED_ONE_COUNTRY_IN)
        self.phone.click(data.DM_AND_LOVED_ONE_COUNTRY_IN)
        self.phone.verify(data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.enter('1234567899', data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.hide_keyboard()
        self.assertTrue(self.phone.is_enabled(data.DM_AND_LOVED_ONE_INVITE_BTN))
        self.phone.click(data.DM_AND_LOVED_ONE_INVITE_BTN)
        self.phone.verify(data.DM_AND_LOVED_ONE_LIST_NAME)
        self.phone.verify(data.DM_AND_LOVED_ONE_LIST_PENDING_MARK)

    def test_urgent_delete_lo(self):
        '''
        This is the test for "Delete a LO"
        '''
        self.test_urgent_invite_lo()
        self.phone.click(data.DM_AND_LOVED_ONE_LIST_NAME)
        self.phone.verify(data.DM_AND_LOVED_ONE_DELETE_TITLE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_LOVED_ONE_LAST_NAME))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_LOVED_ONE_FIRST_NAME))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_LOVED_ONE_EMAIL))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_LOVED_ONE_CELL_NUMBER))
        self.phone.click(data.DM_AND_LOVED_ONE_DELETE_BTN)
        self.phone.verify(data.DM_AND_LOVED_ONE_LIST_ADD_BTN)

    def test_normal_validation_check_for_lo(self):
        '''
        This is the test for "Validation check during enter LO info"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_MANAGE_LO)
        self.phone.click(data.DM_AND_OPTIONS_MANAGE_LO)
        self.phone.verify(data.DM_AND_LOVED_ONE_LIST_DESCRIPTION)
        self.phone.click(data.DM_AND_LOVED_ONE_LIST_ADD_BTN)
        self.phone.verify(data.DM_AND_LOVED_ONE_LAST_NAME)

        # Validation check for email
        self.phone.enter('test', data.DM_AND_LOVED_ONE_LAST_NAME)
        self.phone.enter('lo', data.DM_AND_LOVED_ONE_FIRST_NAME)
        self.phone.enter('hello', data.DM_AND_LOVED_ONE_EMAIL)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_LOVED_ONE_COUNTRY_CODE)
        self.phone.verify(data.DM_AND_LOVED_ONE_COUNTRY_HK)
        self.phone.verify(data.DM_AND_LOVED_ONE_COUNTRY_IN)
        self.phone.click(data.DM_AND_LOVED_ONE_COUNTRY_IN)
        self.phone.verify(data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.enter('1234567899', data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_LOVED_ONE_INVITE_BTN)
        self.phone.verify(data.DM_AND_LOVED_ONE_EMAIL_ERROR)
        self.assertEqual(data.EM_DM_LOVED_ONE_INVALID_EMAIL, self.phone.text(data.DM_AND_LOVED_ONE_EMAIL_ERROR))
        self.phone.clear(data.DM_AND_LOVED_ONE_EMAIL)
        self.phone.enter(patient['email'].replace('test', 'lo'), data.DM_AND_LOVED_ONE_EMAIL)
        self.phone.hide_keyboard()

        # Validation check for cell number
        self._validation_check_for_number(data.DM_AND_LOVED_ONE_COUNTRY_HK, 8, data.DM_AND_LOVED_ONE_COUNTRY_CODE, data.DM_AND_LOVED_ONE_CELL_NUMBER, data.DM_AND_LOVED_ONE_CELL_ERROR, data.DM_AND_LOVED_ONE_INVITE_BTN)
        self._validation_check_for_number(data.DM_AND_LOVED_ONE_COUNTRY_US, 10, data.DM_AND_LOVED_ONE_COUNTRY_CODE, data.DM_AND_LOVED_ONE_CELL_NUMBER, data.DM_AND_LOVED_ONE_CELL_ERROR, data.DM_AND_LOVED_ONE_INVITE_BTN)
        self._validation_check_for_number(data.DM_AND_LOVED_ONE_COUNTRY_CH, 11, data.DM_AND_LOVED_ONE_COUNTRY_CODE, data.DM_AND_LOVED_ONE_CELL_NUMBER, data.DM_AND_LOVED_ONE_CELL_ERROR, data.DM_AND_LOVED_ONE_INVITE_BTN)
        self._validation_check_for_number(data.DM_AND_LOVED_ONE_COUNTRY_IN, 10, data.DM_AND_LOVED_ONE_COUNTRY_CODE, data.DM_AND_LOVED_ONE_CELL_NUMBER, data.DM_AND_LOVED_ONE_CELL_ERROR, data.DM_AND_LOVED_ONE_INVITE_BTN)
        self.phone.clear(data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.enter('1234567890', data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_LOVED_ONE_INVITE_BTN)
        self.phone.verify(data.DM_AND_LOVED_ONE_CELL_ERROR)
        self.assertEqual(data.EM_DM_LOVED_ONE_CONFLICT_NUMBER, self.phone.text(data.DM_AND_LOVED_ONE_CELL_ERROR))

    def test_normal_invite_lo_offline(self):
        '''
        This is the test for "Add a lo in offline mode"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_MANAGE_LO)
        self.phone.click(data.DM_AND_OPTIONS_MANAGE_LO)
        self.phone.verify(data.DM_AND_LOVED_ONE_LIST_DESCRIPTION)
        self.phone.click(data.DM_AND_LOVED_ONE_LIST_ADD_BTN)
        self.phone.verify(data.DM_AND_LOVED_ONE_LAST_NAME)
        self.phone.click(data.DM_AND_LOVED_ONE_CLOSE_ICON)
        self.phone.verify(data.DM_AND_LOVED_ONE_LIST_ADD_ICON)
        self.phone.click(data.DM_AND_LOVED_ONE_LIST_ADD_ICON)
        self.phone.verify(data.DM_AND_LOVED_ONE_LAST_NAME)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_LOVED_ONE_INVITE_BTN))
        self.phone.enter('test', data.DM_AND_LOVED_ONE_LAST_NAME)
        self.phone.enter('lo', data.DM_AND_LOVED_ONE_FIRST_NAME)
        self.phone.enter(patient['email'].replace('test', 'lo'), data.DM_AND_LOVED_ONE_EMAIL)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_LOVED_ONE_COUNTRY_CODE)
        self.phone.verify(data.DM_AND_LOVED_ONE_COUNTRY_HK)
        self.phone.verify(data.DM_AND_LOVED_ONE_COUNTRY_IN)
        self.phone.click(data.DM_AND_LOVED_ONE_COUNTRY_IN)
        self.phone.verify(data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.enter('1234567899', data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.hide_keyboard()
        self.phone.turn_off_wifi()
        self.phone.click(data.DM_AND_LOVED_ONE_INVITE_BTN)
        self.phone.verify(data.DM_AND_NO_NETWORK_TITLE)

    def test_normal_delete_lo_offline(self):
        '''
        This is the test for "Delete a LO in offline mode"
        '''
        self.test_urgent_invite_lo()
        self.phone.click(data.DM_AND_LOVED_ONE_LIST_NAME)
        self.phone.verify(data.DM_AND_LOVED_ONE_DELETE_TITLE)
        self.phone.turn_off_wifi()
        self.phone.click(data.DM_AND_LOVED_ONE_DELETE_BTN)
        self.phone.verify(data.DM_AND_NO_NETWORK_TITLE)

    def test_normal_check_faq(self):
        '''
        This is the test for "Check all entries in FAQ"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_FAQ)
        self.phone.click(data.DM_AND_OPTIONS_FAQ)
        self.phone.verify(data.DM_AND_FAQ_QUESTION)
        for item in data.DM_AND_FAQ_QUES_LIST:
            self.phone.scroll_action(lambda: self.phone.click(item))
            try:
                self.assertTrue(self.phone.is_element_present(data.DM_AND_FAQ_ANSWER))
            except:
                self.phone.swipe_up()
                self.assertTrue(self.phone.is_element_present(data.DM_AND_FAQ_ANSWER))
            self.phone.click(item)
            self.assertFalse(self.phone.is_element_present(data.DM_AND_FAQ_ANSWER))

    def test_normal_support_from_faq(self):
        '''
        This is the test for "Launch Freshdesk from FAQ"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_FAQ)
        self.phone.click(data.DM_AND_OPTIONS_FAQ)
        self.phone.verify(data.DM_AND_FAQ_QUESTION)
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_FAQ_SUPPORT_BTN))
        self.phone.verify(data.DM_AND_FRESHDESK_TITLE)

    def test_urgent_edit_my_info(self):
        '''
        This is the test for "Edit personal info"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.click(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_SETTINGS_MY_INFO))
        self.phone.verify(data.DM_AND_PERSONAL_INFO_COUNTRY_CODE)
        self.phone.click(data.DM_AND_PERSONAL_INFO_COUNTRY_CODE)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_COUNTRY_HK)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_COUNTRY_IN)
        self.phone.click(data.DM_AND_PERSONAL_INFO_COUNTRY_CH)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_CELL_NUMBER)
        self.phone.clear(data.DM_AND_PERSONAL_INFO_CELL_NUMBER)
        self.phone.enter('12345678900', data.DM_AND_PERSONAL_INFO_CELL_NUMBER)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_PERSONAL_INFO_GENDER)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_MALE)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_FEMALE)
        self.phone.click(data.DM_AND_PERSONAL_INFO_FEMALE)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_BIRTHDAY)
        self.phone.click(data.DM_AND_PERSONAL_INFO_BIRTHDAY)
        self.phone.clear(data.DM_AND_PERSONAL_INFO_DATE_MONTH)
        self.phone.enter('Oct', data.DM_AND_PERSONAL_INFO_DATE_MONTH)
        self.phone.clear(data.DM_AND_PERSONAL_INFO_DATE_DAY)
        self.phone.enter('10', data.DM_AND_PERSONAL_INFO_DATE_DAY)
        self.phone.clear(data.DM_AND_PERSONAL_INFO_DATE_YEAR)
        self.phone.enter('1966', data.DM_AND_PERSONAL_INFO_DATE_YEAR)
        self.phone.click(data.DM_AND_PERSONAL_INFO_DATE_SET_BTN)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_BUTTON)
        self.phone.click(data.DM_AND_PERSONAL_INFO_BUTTON)
        self.phone.verify(data.DM_AND_SETTINGS_PATIENT_ID)
        self.phone.click(data.DM_AND_SETTINGS_MY_INFO)
        self.assertEqual(data.DM_AND_PERSONAL_INFO_COUNTRY_CH, self.phone.text(data.DM_AND_PERSONAL_INFO_COUNTRY_CODE_TEXT))
        self.assertEqual('12345678900', self.phone.text(data.DM_AND_PERSONAL_INFO_CELL_NUMBER))
        self.assertEqual(data.DM_AND_PERSONAL_INFO_FEMALE, self.phone.text(data.DM_AND_PERSONAL_INFO_GENDER_TEXT))
        self.assertEqual('1966-10-10', self.phone.text(data.DM_AND_PERSONAL_INFO_BIRTHDAY_TEXT))

    # def test_normal_save_personal_info_offline(self):
    #     '''
    #     This is the test for "Save personal info in offline mode"
    #     '''
    #     patient = self.phone.get_new_patient_account(after_sign_up=True)
    #     self.phone.login(patient['email'])
    #     self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
    #     self.phone.verify(data.DM_AND_OPTIONS_SETTINGS)
    #     self.phone.click(data.DM_AND_OPTIONS_SETTINGS)
    #     self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_SETTINGS_MY_INFO))
    #     self.phone.verify(data.DM_AND_PERSONAL_INFO_COUNTRY_CODE)
    #     self.phone.turn_off_wifi()
    #     self.phone.clear(data.DM_AND_PERSONAL_INFO_CELL_NUMBER)
    #     self.phone.enter('1111111111', data.DM_AND_PERSONAL_INFO_CELL_NUMBER)
    #     self.phone.hide_keyboard()
    #     self.phone.click(data.DM_AND_PERSONAL_INFO_BUTTON)
    #     self.phone.verify(data.DM_AND_NO_NETWORK_TITLE)


    def test_normal_validation_check_for_personal_info(self):
        '''
        This is the test for "Validation check for personal info"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.click(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_SETTINGS_MY_INFO))
        self.phone.verify(data.DM_AND_PERSONAL_INFO_COUNTRY_CODE)
        self.phone.clear(data.DM_AND_PERSONAL_INFO_CELL_NUMBER)
        self.phone.hide_keyboard()
        self.assertFalse(self.phone.is_enabled(data.DM_AND_PERSONAL_INFO_BUTTON))

        # Validation check for cell number
        self._validation_check_for_number(data.DM_AND_PERSONAL_INFO_COUNTRY_HK, 8, data.DM_AND_PERSONAL_INFO_COUNTRY_CODE, data.DM_AND_PERSONAL_INFO_CELL_NUMBER, data.DM_AND_PERSONAL_INFO_CELL_ERROR, data.DM_AND_PERSONAL_INFO_BUTTON)
        self._validation_check_for_number(data.DM_AND_PERSONAL_INFO_COUNTRY_US, 10, data.DM_AND_PERSONAL_INFO_COUNTRY_CODE, data.DM_AND_PERSONAL_INFO_CELL_NUMBER, data.DM_AND_PERSONAL_INFO_CELL_ERROR, data.DM_AND_PERSONAL_INFO_BUTTON)
        self._validation_check_for_number(data.DM_AND_PERSONAL_INFO_COUNTRY_CH, 11, data.DM_AND_PERSONAL_INFO_COUNTRY_CODE, data.DM_AND_PERSONAL_INFO_CELL_NUMBER, data.DM_AND_PERSONAL_INFO_CELL_ERROR, data.DM_AND_PERSONAL_INFO_BUTTON)
        self._validation_check_for_number(data.DM_AND_PERSONAL_INFO_COUNTRY_IN, 10, data.DM_AND_PERSONAL_INFO_COUNTRY_CODE, data.DM_AND_PERSONAL_INFO_CELL_NUMBER, data.DM_AND_PERSONAL_INFO_CELL_ERROR, data.DM_AND_PERSONAL_INFO_BUTTON)
        
    def test_normal_check_patient_id(self):
        '''
        This is the test for "Check patient ID"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.click(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_SETTINGS_PATIENT_ID))
        self.phone.verify(data.DM_AND_PATIENT_ID_CONTENT)
        _id = self.phone.text(data.DM_AND_PATIENT_ID_CONTENT)
        self.phone.click(data.DM_AND_PATIENT_ID_BUTTON)
        self.phone.verify(data.DM_AND_SETTINGS_PATIENT_ID)
        self.assertTrue(self.phone.is_element_present(_id))

    def test_normal_check_user_agreement(self):
        '''
        This is the test for "Check User Agreement"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.click(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_SETTINGS_USER_AGREEMENT))
        self.phone.verify(data.DM_AND_TERM_TITLE)
        self.assertEqual(data.VALUE_AND_TERM_TITLE, self.phone.text(data.DM_AND_TERM_TITLE))
        self.phone.click(data.DM_AND_TERM_BUTTON)

    @unittest.skip('Bug not fixed')
    def test_normal_update_language(self):
        '''
        This is the test for "Update language"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.click(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_SETTINGS_LANGUAGE))
        self.phone.verify(data.DM_AND_LANGUAGE_TITLE)
        self.assertEqual(data.VALUE_DM_LANGUAGE_TITLE, self.phone.text(data.DM_AND_LANGUAGE_TITLE))
        self.phone.click(data.DM_AND_LANGUAGE_ZH)
        self.phone.click(data.DM_AND_LANGUAGE_SAVE_BTN)
        self.assertTrue(self.phone.is_element_present('中文（繁體）'))
        self.phone.click('中文（繁體）')
        self.phone.verify(data.DM_AND_LANGUAGE_TITLE)
        self.phone.click(data.DM_AND_LANGUAGE_EN)
        self.phone.click(data.DM_AND_LANGUAGE_SAVE_BTN)
        self.assertTrue(self.phone.is_element_present('English'))

    def test_urgent_set_alert_time(self):
        '''
        This is the test for "Set alert time"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.click(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_SETTINGS_ALERTTIME))
        self.phone.verify(data.DM_AND_SET_ALERT_TITLE)
        self.phone.click(data.DM_AND_SET_ALERT_BRK)
        self.phone.verify(data.DM_AND_SET_ALERT_MINUTE)
        self.phone.clear(data.DM_AND_SET_ALERT_MINUTE)
        self.phone.enter('01', data.DM_AND_SET_ALERT_MINUTE)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_TITLE)
        self.phone.click(data.DM_AND_SET_ALERT_LUN)
        self.phone.verify(data.DM_AND_SET_ALERT_MINUTE)
        self.phone.clear(data.DM_AND_SET_ALERT_MINUTE)
        self.phone.enter('31', data.DM_AND_SET_ALERT_MINUTE)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_TITLE)
        self.phone.click(data.DM_AND_SET_ALERT_DIN)
        self.phone.verify(data.DM_AND_SET_ALERT_MINUTE)
        self.phone.clear(data.DM_AND_SET_ALERT_MINUTE)
        self.phone.enter('01', data.DM_AND_SET_ALERT_MINUTE)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_TITLE)
        self.phone.click(data.DM_AND_SET_ALERT_NIG)
        self.phone.verify(data.DM_AND_SET_ALERT_MINUTE)
        self.phone.clear(data.DM_AND_SET_ALERT_MINUTE)
        self.phone.enter('31', data.DM_AND_SET_ALERT_MINUTE)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.click(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SETTINGS_ALERTTIME_TITLE)
        alert_time = self.phone.text(data.DM_AND_SETTINGS_ALERTTIME)
        self.assertTrue('8:01' in alert_time)
        self.assertTrue('1:31' in alert_time)
        self.assertTrue('9:01' in alert_time)
        self.assertTrue('11:31' in alert_time)

    def test_normal_validation_check_for_alert_time(self):
        '''
        This is the test for "Validation check for alert time"
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_OPTIONS_MENU_BTN)
        self.phone.verify(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.click(data.DM_AND_OPTIONS_SETTINGS)
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_SETTINGS_ALERTTIME))
        self.phone.verify(data.DM_AND_SET_ALERT_TITLE)

        # Validation for breakfast time
        self.phone.click(data.DM_AND_SET_ALERT_LUN)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('AM', data.DM_AND_SET_ALERT_APM)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.click(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_ALERT_BRK_ERROR)
        self.assertEqual(data.EM_DM_SET_ALERT_BRK_AFTER_LUN, self.phone.text(data.DM_AND_SET_ALERT_BRK_ERROR))
        self.phone.click(data.DM_AND_SET_ALERT_LUN)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('PM', data.DM_AND_SET_ALERT_APM)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)

        self.phone.click(data.DM_AND_SET_ALERT_DIN)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('AM', data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_HOUR)
        self.phone.enter('1', data.DM_AND_SET_ALERT_HOUR)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.click(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_ALERT_BRK_ERROR)
        self.assertEqual(data.EM_DM_SET_ALERT_BRK_AFTER_DIN, self.phone.text(data.DM_AND_SET_ALERT_BRK_ERROR))
        self.phone.click(data.DM_AND_SET_ALERT_DIN)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('PM', data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_HOUR)
        self.phone.enter('9', data.DM_AND_SET_ALERT_HOUR)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)

        self.phone.click(data.DM_AND_SET_ALERT_NIG)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('AM', data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_HOUR)
        self.phone.enter('1', data.DM_AND_SET_ALERT_HOUR)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.click(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_ALERT_BRK_ERROR)
        self.assertEqual(data.EM_DM_SET_ALERT_BRK_AFTER_NIG, self.phone.text(data.DM_AND_SET_ALERT_BRK_ERROR))
        self.phone.click(data.DM_AND_SET_ALERT_NIG)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('PM', data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_HOUR)
        self.phone.enter('11', data.DM_AND_SET_ALERT_HOUR)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)

        # Validation for lunch time
        self.phone.click(data.DM_AND_SET_ALERT_DIN)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('AM', data.DM_AND_SET_ALERT_APM)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.click(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_ALERT_LUN_ERROR)
        self.assertEqual(data.EM_DM_SET_ALERT_LUN_AFTER_DIN, self.phone.text(data.DM_AND_SET_ALERT_LUN_ERROR))
        self.phone.click(data.DM_AND_SET_ALERT_DIN)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('PM', data.DM_AND_SET_ALERT_APM)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)

        self.phone.click(data.DM_AND_SET_ALERT_NIG)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('AM', data.DM_AND_SET_ALERT_APM)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.click(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_ALERT_LUN_ERROR)
        self.assertEqual(data.EM_DM_SET_ALERT_LUN_AFTER_NIG, self.phone.text(data.DM_AND_SET_ALERT_LUN_ERROR))
        self.phone.click(data.DM_AND_SET_ALERT_NIG)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_APM)
        self.phone.enter('PM', data.DM_AND_SET_ALERT_APM)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)

        # Validation for dinner time
        self.phone.click(data.DM_AND_SET_ALERT_NIG)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_HOUR)
        self.phone.enter('6', data.DM_AND_SET_ALERT_HOUR)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.click(data.DM_AND_SET_ALERT_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_ALERT_DIN_ERROR)
        self.assertEqual(data.EM_DM_SET_ALERT_DIN_AFTER_NIG, self.phone.text(data.DM_AND_SET_ALERT_DIN_ERROR))
        self.phone.click(data.DM_AND_SET_ALERT_NIG)
        self.phone.verify(data.DM_AND_SET_ALERT_APM)
        self.phone.clear(data.DM_AND_SET_ALERT_HOUR)
        self.phone.enter('11', data.DM_AND_SET_ALERT_HOUR)
        self.phone.click(data.DM_AND_SET_ALERT_SET_BTN)
        self.phone.verify(data.DM_AND_SET_ALERT_NEXT_BUTTON)



















if __name__ == '__main__':
    unittest.main()
