#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time
import unittest
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case
from Nurse_A.Scenario.android_scenario import ANDROID
from Nurse_A.Settings import keycode, constant, data, setup, mobile_setup

class Sign_up(Case):

    def setUp(self):
        self.phone = ANDROID()

    def tearDown(self):
        self.phone.logout()
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

    def _fill_time(self, location, hour=None, minute=None, apm=None):
        self.phone.click(location)
        self.phone.verify(data.DM_AND_SET_MEALTIME_HOUR)
        if hour != None:
            self.phone.clear(data.DM_AND_SET_MEALTIME_HOUR)
            self.phone.enter(hour, data.DM_AND_SET_MEALTIME_HOUR)
        if minute != None:
            self.phone.clear(data.DM_AND_SET_MEALTIME_MINUTE)
            self.phone.enter(minute, data.DM_AND_SET_MEALTIME_MINUTE)
        if apm != None:
            self.phone.clear(data.DM_AND_SET_MEALTIME_APM)
            self.phone.enter(apm, data.DM_AND_SET_MEALTIME_APM)
        self.phone.click(data.DM_AND_SET_MEALTIME_SET_BTN)

    def test_urgent_normal_sign_up(self):
        '''
        This is the test for 'Normal sign up process'
        '''
        patient = self.phone.get_new_patient_account()
        self.phone.signup(patient['email'])

    def test_urgent_normal_sign_up_for_med_goals_patient(self):
        '''
        This is the test for 'Sign up process for has-med_goals patient'
        '''
        patient = self.phone.get_new_patient_account(bg=0b1010101, med=0b100)
        self.phone.signup(patient['email'])
        self.phone.accept_med_change()

    def test_urgent_log_in(self):
        '''
        This is the test for 'Normal log in process and log out function'
        '''
        self.phone.login(mobile_setup.patient_clean['email'])

    def test_normal_log_in_validation(self):
        '''
        This is the test for 'Validation check for email and password in log in process'
        '''
        self.phone.verify(data.DM_AND_WELCOME_ENTER)
        self.phone.click(data.DM_AND_WELCOME_ENTER)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_SIGN_IN_BUTTON))
        
        # Validation check for invalid email address
        self.phone.verify(data.DM_AND_SIGN_IN_TITLE)
        self.phone.enter('abc', data.DM_AND_SIGN_IN_FIELD)
        self.phone.click(data.DM_AND_SIGN_IN_BUTTON)
        self.phone.verify(data.DM_AND_SIGN_IN_ERROR)
        self.assertEqual(data.EM_DM_SIGN_IN_INVALID_EMAIL, self.phone.text(data.DM_AND_SIGN_IN_ERROR))
        self.phone.clear(data.DM_AND_SIGN_IN_FIELD)

        # Validation check for non-registered email
        self.phone.enter('1111j@kkk.cc3', data.DM_AND_SIGN_IN_FIELD)
        self.assertFalse(self.phone.is_element_present(data.DM_AND_SIGN_IN_ERROR))
        self.phone.click(data.DM_AND_SIGN_IN_BUTTON)
        self.phone.verify(data.DM_AND_SIGN_IN_ERROR)
        self.assertEqual(data.EM_DM_SIGN_IN_NOT_REGISTER_EMAIL, self.phone.text(data.DM_AND_SIGN_IN_ERROR))

        self.phone.clear(data.DM_AND_SIGN_IN_FIELD)
        self.phone.enter(mobile_setup.patient_clean['email'], data.DM_AND_SIGN_IN_FIELD)
        self.phone.click(data.DM_AND_SIGN_IN_BUTTON)
        self.phone.verify(data.DM_AND_PASSWORD_TITLE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_PASSWORD_SIGN_IN_BTN))

        # Validation check for invalid password
        self.phone.enter('   ', data.DM_AND_PASSWORD_FIELD)
        self.phone.click(data.DM_AND_PASSWORD_SIGN_IN_BTN)
        self.phone.verify(data.DM_AND_PASSWORD_ERROR)
        self.assertEqual(data.EM_DM_PASSWORD_INVALID_INPUT, self.phone.text(data.DM_AND_PASSWORD_ERROR))
        self.phone.clear(data.DM_AND_PASSWORD_FIELD)

        # Validation check for non-match password
        self.phone.enter('aaaxxx', data.DM_AND_PASSWORD_FIELD)
        self.assertFalse(self.phone.is_element_present(data.DM_AND_PASSWORD_ERROR))
        self.phone.click(data.DM_AND_PASSWORD_SIGN_IN_BTN)
        self.phone.verify(data.DM_AND_PASSWORD_ERROR)
        self.assertEqual(data.EM_DM_PASSWORD_NOT_MATCH, self.phone.text(data.DM_AND_PASSWORD_ERROR))

    def test_normal_sign_up_validation(self):
        '''
        This is the test for 'Validation check for sign up process'
        '''
        patient = self.phone.get_new_patient_account()
        self.phone.verify(data.DM_AND_WELCOME_ENTER)
        self.phone.click(data.DM_AND_WELCOME_ENTER)
        self.phone.verify(data.DM_AND_SIGN_IN_TITLE)
        self.phone.enter(patient['email'], data.DM_AND_SIGN_IN_FIELD)
        self.phone.click(data.DM_AND_SIGN_IN_BUTTON)
        self.phone.verify(data.DM_AND_SET_PASSWORD_TITLE)

        # Validation check for short password
        self.phone.enter('aa', data.DM_AND_SET_PASSWORD_PASSWORD_FIELD)
        self.phone.click(data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.phone.verify(data.DM_AND_SET_PASSWORD_FIRST_FIELD_ERROR)
        self.assertEqual(data.EM_DM_SET_PASSWORD_SHORT_ERROR, self.phone.text(data.DM_AND_SET_PASSWORD_FIRST_FIELD_ERROR))
        self.phone.clear(data.DM_AND_SET_PASSWORD_PASSWORD_FIELD)
        self.phone.enter('123456', data.DM_AND_SET_PASSWORD_PASSWORD_FIELD)
        self.phone.enter('aa', data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.phone.click(data.DM_AND_SET_PASSWORD_PASSWORD_FIELD)
        self.phone.verify(data.DM_AND_SET_PASSWORD_SECOND_FIELD_ERROR)
        self.assertEqual(data.EM_DM_SET_PASSWORD_SHORT_ERROR, self.phone.text(data.DM_AND_SET_PASSWORD_SECOND_FIELD_ERROR))

        # Validation check for unmatch password
        self.phone.clear(data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.phone.enter('123455', data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.phone.click(data.DM_AND_SET_PASSWORD_BUTTON)
        self.phone.verify(data.DM_AND_SET_PASSWORD_SECOND_FIELD_ERROR)
        self.assertEqual(data.EM_DM_SET_PASSWORD_NOT_MATCH, self.phone.text(data.DM_AND_SET_PASSWORD_SECOND_FIELD_ERROR))
        self.phone.clear(data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.phone.enter('123456', data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.phone.click(data.DM_AND_SET_PASSWORD_BUTTON)

        # Validation check for patient number 
        self.phone.verify(data.DM_AND_PERSONAL_INFO_TITLE)
        self._validation_check_for_number(data.DM_AND_PERSONAL_INFO_COUNTRY_US, 10,
                                          data.DM_AND_PERSONAL_INFO_COUNTRY_CODE,
                                          data.DM_AND_PERSONAL_INFO_CELL_NUMBER,
                                          data.DM_AND_PERSONAL_INFO_CELL_ERROR,
                                          data.DM_AND_PERSONAL_INFO_BUTTON
                                          )
        self._validation_check_for_number(data.DM_AND_PERSONAL_INFO_COUNTRY_IN, 10,
                                          data.DM_AND_PERSONAL_INFO_COUNTRY_CODE,
                                          data.DM_AND_PERSONAL_INFO_CELL_NUMBER,
                                          data.DM_AND_PERSONAL_INFO_CELL_ERROR,
                                          data.DM_AND_PERSONAL_INFO_BUTTON
                                          )
        self._validation_check_for_number(data.DM_AND_PERSONAL_INFO_COUNTRY_CH, 11,
                                          data.DM_AND_PERSONAL_INFO_COUNTRY_CODE,
                                          data.DM_AND_PERSONAL_INFO_CELL_NUMBER,
                                          data.DM_AND_PERSONAL_INFO_CELL_ERROR,
                                          data.DM_AND_PERSONAL_INFO_BUTTON
                                          )
        self._validation_check_for_number(data.DM_AND_PERSONAL_INFO_COUNTRY_HK, 8,
                                          data.DM_AND_PERSONAL_INFO_COUNTRY_CODE,
                                          data.DM_AND_PERSONAL_INFO_CELL_NUMBER,
                                          data.DM_AND_PERSONAL_INFO_CELL_ERROR,
                                          data.DM_AND_PERSONAL_INFO_BUTTON
                                          )
        self.phone.clear(data.DM_AND_PERSONAL_INFO_CELL_NUMBER)
        self.phone.enter('12345678', data.DM_AND_PERSONAL_INFO_CELL_NUMBER)
        self.phone.click(data.DM_AND_PERSONAL_INFO_BUTTON)

        # Validation check for lo email
        self.phone.verify(data.DM_AND_LOVED_ONE_TITLE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_LOVED_ONE_NEXT_BUTTON))
        self.phone.enter('last', data.DM_AND_LOVED_ONE_LAST_NAME)
        self.phone.enter('first', data.DM_AND_LOVED_ONE_FIRST_NAME)
        self.phone.click(data.DM_AND_LOVED_ONE_COUNTRY_CODE)
        self.phone.verify(data.DM_AND_LOVED_ONE_COUNTRY_HK)
        self.phone.verify(data.DM_AND_LOVED_ONE_COUNTRY_IN)
        self.phone.click(data.DM_AND_LOVED_ONE_COUNTRY_IN)
        self.phone.enter('1234567899', data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.enter('email', data.DM_AND_LOVED_ONE_EMAIL)
        self.phone.click(data.DM_AND_LOVED_ONE_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_LOVED_ONE_EMAIL_ERROR)
        self.assertEqual(data.EM_DM_LOVED_ONE_INVALID_EMAIL, self.phone.text(data.DM_AND_LOVED_ONE_EMAIL_ERROR))
        self.phone.clear(data.DM_AND_LOVED_ONE_EMAIL)
        self.phone.enter('lo@test.com', data.DM_AND_LOVED_ONE_EMAIL)
        
        # Validation check for lo cell number
        self._validation_check_for_number(data.DM_AND_LOVED_ONE_COUNTRY_US, 10,
                                          data.DM_AND_LOVED_ONE_COUNTRY_CODE,
                                          data.DM_AND_LOVED_ONE_CELL_NUMBER,
                                          data.DM_AND_LOVED_ONE_CELL_ERROR,
                                          data.DM_AND_LOVED_ONE_NEXT_BUTTON
                                          )
        self._validation_check_for_number(data.DM_AND_LOVED_ONE_COUNTRY_IN, 10,
                                          data.DM_AND_LOVED_ONE_COUNTRY_CODE,
                                          data.DM_AND_LOVED_ONE_CELL_NUMBER,
                                          data.DM_AND_LOVED_ONE_CELL_ERROR,
                                          data.DM_AND_LOVED_ONE_NEXT_BUTTON
                                          )
        self._validation_check_for_number(data.DM_AND_LOVED_ONE_COUNTRY_CH, 11,
                                          data.DM_AND_LOVED_ONE_COUNTRY_CODE,
                                          data.DM_AND_LOVED_ONE_CELL_NUMBER,
                                          data.DM_AND_LOVED_ONE_CELL_ERROR,
                                          data.DM_AND_LOVED_ONE_NEXT_BUTTON
                                          )
        self._validation_check_for_number(data.DM_AND_LOVED_ONE_COUNTRY_HK, 8,
                                          data.DM_AND_LOVED_ONE_COUNTRY_CODE,
                                          data.DM_AND_LOVED_ONE_CELL_NUMBER,
                                          data.DM_AND_LOVED_ONE_CELL_ERROR,
                                          data.DM_AND_LOVED_ONE_NEXT_BUTTON
                                          )
        self.phone.clear(data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.enter('12345678', data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.click(data.DM_AND_LOVED_ONE_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_LOVED_ONE_CELL_ERROR)
        self.assertEqual(data.EM_DM_LOVED_ONE_CONFLICT_NUMBER, self.phone.text(data.DM_AND_LOVED_ONE_CELL_ERROR))
        self.phone.clear(data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.enter('12345677', data.DM_AND_LOVED_ONE_CELL_NUMBER)
        self.phone.click(data.DM_AND_LOVED_ONE_NEXT_BUTTON)

        # Validation for mealtimes
        self.phone.verify(data.DM_AND_SET_MEALTIME_TITLE)
        self._fill_time(data.DM_AND_SET_MEALTIME_LUN, hour=3, apm='AM')
        self.phone.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_MEALTIME_BRK_ERROR)
        self.assertEqual(data.EM_DM_SET_MEALTIME_BRK_AFTER_LUN, self.phone.text(data.DM_AND_SET_MEALTIME_BRK_ERROR))
        self._fill_time(data.DM_AND_SET_MEALTIME_LUN, hour=1, apm='PM')

        self._fill_time(data.DM_AND_SET_MEALTIME_DIN, hour=3, apm='AM')
        self.phone.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_MEALTIME_BRK_ERROR)
        self.assertEqual(data.EM_DM_SET_MEALTIME_BRK_AFTER_DIN, self.phone.text(data.DM_AND_SET_MEALTIME_BRK_ERROR))
        self._fill_time(data.DM_AND_SET_MEALTIME_DIN, hour=9, apm='PM')

        self._fill_time(data.DM_AND_SET_MEALTIME_NIG, hour=3, apm='AM')
        self.phone.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_MEALTIME_BRK_ERROR)
        self.assertEqual(data.EM_DM_SET_MEALTIME_BRK_AFTER_NIG, self.phone.text(data.DM_AND_SET_MEALTIME_BRK_ERROR))
        self._fill_time(data.DM_AND_SET_MEALTIME_NIG, hour=11, apm='PM')

        self._fill_time(data.DM_AND_SET_MEALTIME_DIN, hour=12, apm='PM')
        self.phone.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_MEALTIME_LUN_ERROR)
        self.assertEqual(data.EM_DM_SET_MEALTIME_LUN_AFTER_DIN, self.phone.text(data.DM_AND_SET_MEALTIME_LUN_ERROR))
        self._fill_time(data.DM_AND_SET_MEALTIME_DIN, hour=9, apm='PM')

        self._fill_time(data.DM_AND_SET_MEALTIME_NIG, hour=12, apm='PM')
        self.phone.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_MEALTIME_LUN_ERROR)
        self.assertEqual(data.EM_DM_SET_MEALTIME_LUN_AFTER_NIG, self.phone.text(data.DM_AND_SET_MEALTIME_LUN_ERROR))
        self._fill_time(data.DM_AND_SET_MEALTIME_NIG, hour=11, apm='PM')

        self._fill_time(data.DM_AND_SET_MEALTIME_NIG, hour=8, apm='PM')
        self.phone.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_SET_MEALTIME_DIN_ERROR)
        self.assertEqual(data.EM_DM_SET_MEALTIME_DIN_AFTER_NIG, self.phone.text(data.DM_AND_SET_MEALTIME_DIN_ERROR))
        self._fill_time(data.DM_AND_SET_MEALTIME_NIG, hour=11, apm='PM')
        
        self.phone.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)

    def test_normal_sign_up_prefilled_data(self):
        '''
        This is the test for 'Prefilled data check in sign up process'
        '''
        patient = self.phone.get_new_patient_account()
        self.phone.click(data.DM_AND_WELCOME_ENTER)
        self.phone.verify(data.DM_AND_SIGN_IN_TITLE)
        self.phone.enter(patient['email'], data.DM_AND_SIGN_IN_FIELD)
        self.phone.click(data.DM_AND_SIGN_IN_BUTTON)
        self.phone.verify(data.DM_AND_SET_PASSWORD_TITLE)
        self.phone.enter('123456', data.DM_AND_SET_PASSWORD_PASSWORD_FIELD)
        self.phone.enter('123456', data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.phone.click(data.DM_AND_SET_PASSWORD_BUTTON)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_TITLE)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_COUNTRY_IN)
        self.phone.verify('1234567890')
        self.phone.verify(data.DM_AND_PERSONAL_INFO_MALE)
        self.phone.verify('1965-09-12')
        self.phone.click(data.DM_AND_PERSONAL_INFO_BUTTON)
        self.phone.verify(data.DM_AND_LOVED_ONE_TITLE)
        self.phone.verify(data.DM_AND_LOVED_ONE_COUNTRY_IN)
        self.phone.verify('1234567891')
        self.phone.click(data.DM_AND_LOVED_ONE_SKIP_BUTTON)
        self.phone.verify(data.DM_AND_SET_MEALTIME_TITLE)
        self.phone.verify(data.VALUE_DM_SET_MEALTIME_BRK_IN)
        self.phone.verify(data.VALUE_DM_SET_MEALTIME_LUN_IN)
        self.phone.verify(data.VALUE_DM_SET_MEALTIME_DIN_IN)
        self.phone.verify(data.VALUE_DM_SET_MEALTIME_NIG_IN)

    def test_normal_sign_up_go_back(self):
        '''
        This is the test for 'Go back function in sign up process'
        This is the test for 'Interrupt sign up progress'
        '''
        patient = self.phone.get_new_patient_account()
        self.phone.click(data.DM_AND_WELCOME_ENTER)
        self.phone.verify(data.DM_AND_SIGN_IN_TITLE)
        self.phone.enter(patient['email'], data.DM_AND_SIGN_IN_FIELD)
        self.phone.click(data.DM_AND_SIGN_IN_BUTTON)
        self.phone.verify(data.DM_AND_SET_PASSWORD_TITLE)
        self.phone.press('Back')
        self.phone.verify(data.DM_AND_SIGN_IN_TITLE)
        self.phone.click(data.DM_AND_SIGN_IN_BUTTON)
        self.phone.verify(data.DM_AND_SET_PASSWORD_TITLE)
        self.phone.click(data.DM_AND_SIGN_IN_BACK)
        self.phone.verify(data.DM_AND_SIGN_IN_TITLE)
        self.phone.click(data.DM_AND_SIGN_IN_BUTTON)
        self.phone.verify(data.DM_AND_SET_PASSWORD_TITLE)
        self.phone.enter('123456', data.DM_AND_SET_PASSWORD_PASSWORD_FIELD)
        self.phone.enter('123456', data.DM_AND_SET_PASSWORD_CONFIRM_FIELD)
        self.phone.click(data.DM_AND_SET_PASSWORD_BUTTON)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_TITLE)
        self.phone.click(data.DM_AND_PERSONAL_INFO_BUTTON)
        self.phone.verify(data.DM_AND_LOVED_ONE_TITLE)
        self.phone.click(data.DM_AND_LOVED_ONE_SKIP_BUTTON)
        self.phone.verify(data.DM_AND_SET_MEALTIME_TITLE)
        self.phone.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_USER_AGREE_TITLE)
        self.phone.click(data.DM_AND_USER_AGREE_BACK)
        self.phone.verify(data.DM_AND_SET_MEALTIME_TITLE)
        self.phone.click(data.DM_AND_SET_MEALTIME_BACK)
        self.phone.verify(data.DM_AND_LOVED_ONE_TITLE)
        self.phone.click(data.DM_AND_LOVED_ONE_BACK)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_TITLE)
        self.phone.click(data.DM_AND_PERSONAL_INFO_BUTTON)
        self.phone.verify(data.DM_AND_LOVED_ONE_TITLE)
        self.phone.click(data.DM_AND_LOVED_ONE_SKIP_BUTTON)
        self.phone.verify(data.DM_AND_SET_MEALTIME_TITLE)
        self.phone.click(data.DM_AND_SET_MEALTIME_NEXT_BUTTON)
        self.phone.verify(data.DM_AND_USER_AGREE_TITLE)
        self.phone.press('Back')
        self.phone.verify(data.DM_AND_SET_MEALTIME_TITLE)
        self.phone.press('Back')
        self.phone.verify(data.DM_AND_LOVED_ONE_TITLE)
        self.phone.press('Back')
        self.phone.verify(data.DM_AND_PERSONAL_INFO_TITLE)
        self.phone.close_app()
        self.phone.launch_app()
        self.phone.verify(data.DM_AND_WELCOME_ENTER)
        self.phone.click(data.DM_AND_WELCOME_ENTER)
        self.phone.verify(data.DM_AND_SIGN_IN_TITLE)
        self.phone.enter(patient['email'], data.DM_AND_SIGN_IN_FIELD)
        self.phone.click(data.DM_AND_SIGN_IN_BUTTON)
        self.phone.verify(data.DM_AND_PASSWORD_TITLE)
        self.phone.enter('123456', data.DM_AND_PASSWORD_FIELD)
        self.phone.click(data.DM_AND_PASSWORD_SIGN_IN_BTN)
        self.phone.verify(data.DM_AND_PERSONAL_INFO_TITLE)

if __name__ == '__main__':
    unittest.main()
