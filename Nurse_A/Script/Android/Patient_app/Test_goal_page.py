#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time
import datetime
import unittest
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case
from Nurse_A.Scenario.android_scenario import ANDROID
from Nurse_A.Settings import keycode, constant, data, setup, mobile_setup

class Goals(Case):

    def setUp(self):
        self.phone = ANDROID()

    def tearDown(self):
        self.phone.logout()
        self.phone.turn_on_wifi()
        self.phone.teardown()
        self.phone.reset_time()

    def test_normal_no_goals_page(self):
        '''
        This is the test for "Check Goals page when non-goal"
        This is the test for "Select button "Go to chat"
        '''
        self.phone.login(mobile_setup.patient_clean['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_EMPTY_MESSAGE)
        self.assertEqual('0 of 0 goals', self.phone.text(data.DM_AND_GOAL_STATE_INFO))
        self.phone.verify(data.DM_AND_GOAL_EMPTY_MESSAGE)
        self.assertEqual(data.EM_AND_GOAL_EMPTY_MESSAGE, self.phone.text(data.DM_AND_GOAL_EMPTY_MESSAGE))
        self.phone.click(data.DM_AND_GOAL_GO_TO_CHAT_BTN)
        self.phone.verify(data.DM_AND_CHAT_FIELD)

    def test_urgent_log_normal_bg(self):
        '''
        This is the test for "Log normal BG reading"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.enter('123', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_log_hyper_bg(self):
        '''
        This is the test for "Log hyper BG reading"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.phone.enter('323', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        sleep(constant.INTERVAL_20)     # Waiting for survey
        self.phone.verify(data.DM_AND_GOAL_EDIT_SURVEY_WHY)
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_SURVEY_WHY_HIGH, self.phone.text(data.DM_AND_GOAL_EDIT_SURVEY_WHY))
        for item in data.DM_AND_GOAL_EDIT_SURVEY_HIGH_REASONS:
            self.phone.scroll_action(lambda: self.phone.click(item))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('323', self.phone.text(data.DM_AND_GOAL_VALUE))


    def test_urgent_log_hypo_bg(self):
        '''
        This is the test for "Log Hypo BG reading"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.phone.enter('56', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        sleep(constant.INTERVAL_20)     # Waiting for survey
        self.phone.verify(data.DM_AND_GOAL_EDIT_SURVEY_WHY)
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_SURVEY_WHY_LOW, self.phone.text(data.DM_AND_GOAL_EDIT_SURVEY_WHY))
        for item in data.DM_AND_GOAL_EDIT_SURVEY_LOW_REASONS:
            self.phone.scroll_action(lambda: self.phone.click(item))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('56', self.phone.text(data.DM_AND_GOAL_VALUE))


    def test_urgent_edit_bg_reading(self):
        '''
        This is the test for "Edit BG reading, check BG table"
        '''
        self.test_urgent_log_normal_bg()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_EDIT_VALUE_FIELD))
        self.phone.clear(data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.enter('133', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('133', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_delete_bg_reading(self):
        '''
        This is the test for "Delete BG reading, check BG table"
        '''
        self.test_urgent_log_normal_bg()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_EDIT_VALUE_FIELD))
        self.phone.scroll_action(lambda: self.phone.verify(data.DM_AND_GOAL_EDIT_DELETE_BTN))
        self.phone.click(data.DM_AND_GOAL_EDIT_DELETE_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_UNCOMPLETED_STATUS)
        self.assertEqual('log', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))

    def test_urgent_log_oral_med(self):
        '''
        This is the test for "Log oral MED goal"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b10, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))

    def test_urgent_log_insulin(self):
        '''
        This is the test for "Log insulin MED goal"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b100, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MED_NAME))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))

    def test_normal_special_amount_of_med(self):
        '''
        This is the test for "Log special amount MED goal"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b1000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        items = self.phone.find(data.DM_AND_GOAL_ITEM)
        for item in items:
            item.click()
        sleep(constant.INTERVAL_10)     # Wait animation finish
        completed_status = self.phone.find(data.DM_AND_GOAL_COMPLETED_STATUS)
        hint_texts = self.phone.find(data.DM_AND_GOAL_HINT_LOG_EDIT)
        dosages = self.phone.find(data.DM_AND_GOAL_DOSAGE_OR_UNIT)
        self.assertEqual(4, len(completed_status))
        for hint in hint_texts:
            self.assertEqual('edit', hint.text)
        self.assertEqual('4+5 units', dosages[0].text)
        self.assertEqual('4/5 drops x 2/3 mcg', dosages[1].text)
        self.assertEqual('4,5 pieces x 2,3 mg/mL', dosages[2].text)
        self.assertEqual('4.5 powder x 2.3 mL', dosages[3].text)

    def test_urgent_edit_med(self):
        '''
        This is the test for "Edit MED goal"
        '''
        self.test_urgent_log_oral_med()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_TIME))
        self.phone.clear(data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.enter('10', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('10', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_delete_med(self):
        '''
        This the test for "Delete MED goal"
        '''
        self.test_urgent_log_insulin()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_TIME))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_DELETE_BTN))
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_UNCOMPLETED_STATUS)
        self.assertEqual('log', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))


    def test_normal_switch_to_previous_day(self):
        '''
        This is the test for "Switch to previous day"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, med=0b100, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        time_today = datetime.datetime.now()
        time_tomorrow = datetime.datetime.now() + datetime.timedelta(1)
        time_shown_str_today = time_today.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_shown_str_tomorrow = time_tomorrow.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_set_str_tomorrow = time_tomorrow.strftime("%Y%m%d.%H%M%S")
        self.phone.set_time(time_set_str_tomorrow)
        self.phone.restart()
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        self.assertEqual(time_shown_str_tomorrow, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.click(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.is_element_present(data.DM_AND_GOAL_NEXT_DAY_BTN)
        self.phone.is_element_present(data.DM_AND_GOAL_LAST_DAY_BTN)
        self.assertEqual(time_shown_str_today, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.verify(data.DM_AND_GOAL_ITEM)

    def test_normal_log_history_bg_goal(self):
        '''
        This is the test for "Log history BG goal"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        time_today = datetime.datetime.now()
        time_tomorrow = datetime.datetime.now() + datetime.timedelta(1)
        time_shown_str_today = time_today.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_shown_str_tomorrow = time_tomorrow.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_set_str_tomorrow = time_tomorrow.strftime("%Y%m%d.%H%M%S")
        self.phone.set_time(time_set_str_tomorrow)
        self.phone.restart()
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        self.assertEqual(time_shown_str_tomorrow, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.click(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.is_element_present(data.DM_AND_GOAL_NEXT_DAY_BTN)
        self.phone.is_element_present(data.DM_AND_GOAL_LAST_DAY_BTN)
        self.assertEqual(time_shown_str_today, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.enter('123', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_normal_log_history_oral_med_goal(self):
        '''
        This is the test for "Log histroy oral MED goal"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b10, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        time_today = datetime.datetime.now()
        time_tomorrow = datetime.datetime.now() + datetime.timedelta(1)
        time_shown_str_today = time_today.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_shown_str_tomorrow = time_tomorrow.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_set_str_tomorrow = time_tomorrow.strftime("%Y%m%d.%H%M%S")
        self.phone.set_time(time_set_str_tomorrow)
        self.phone.restart()
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        self.assertEqual(time_shown_str_tomorrow, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.click(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.is_element_present(data.DM_AND_GOAL_NEXT_DAY_BTN)
        self.phone.is_element_present(data.DM_AND_GOAL_LAST_DAY_BTN)
        self.assertEqual(time_shown_str_today, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))

    def test_normal_log_history_insulin_goal(self):
        '''
        This is the test for "Log history insulin goal"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b100, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        time_today = datetime.datetime.now()
        time_tomorrow = datetime.datetime.now() + datetime.timedelta(1)
        time_shown_str_today = time_today.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_shown_str_tomorrow = time_tomorrow.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_set_str_tomorrow = time_tomorrow.strftime("%Y%m%d.%H%M%S")
        self.phone.set_time(time_set_str_tomorrow)
        self.phone.restart()
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        self.assertEqual(time_shown_str_tomorrow, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.click(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.is_element_present(data.DM_AND_GOAL_NEXT_DAY_BTN)
        self.phone.is_element_present(data.DM_AND_GOAL_LAST_DAY_BTN)
        self.assertEqual(time_shown_str_today, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MED_NAME))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))

    def test_normal_edit_history_bg_reading(self):
        '''
        This is the test for "Edit history BG reading"
        '''
        self.test_normal_log_history_bg_goal()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_EDIT_VALUE_FIELD))
        self.phone.clear(data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.enter('133', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('133', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_normal_delete_history_bg_reading(self):
        '''
        This is the test for "Delete history BG reading"
        '''
        self.test_normal_log_history_bg_goal()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_EDIT_VALUE_FIELD))
        self.phone.scroll_action(lambda: self.phone.verify(data.DM_AND_GOAL_EDIT_DELETE_BTN))
        self.phone.click(data.DM_AND_GOAL_EDIT_DELETE_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_UNCOMPLETED_STATUS)
        self.assertEqual('log', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))


    def test_normal_edit_history_med_reading(self):
        '''
        This is the test for "Edit history MED reading"
        '''
        self.test_normal_log_history_insulin_goal()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_TIME))
        self.phone.clear(data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.enter('10', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('10', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_normal_delete_history_med_reading(self):
        '''
        This is the test for "Delete history MED reading"
        '''
        self.test_normal_log_history_oral_med_goal()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_TIME))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_DELETE_BTN))
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_UNCOMPLETED_STATUS)
        self.assertEqual('log', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))

    def test_urgent_self_log_bg_goal(self):
        '''
        This is the test for "Self log BG goal"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_BG)
        self.phone.click(data.DM_AND_SELF_LOG_BG)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.enter('123', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_VALUE))


    def test_normal_self_log_hyper_bg_goal(self):
        '''
        This is the test for "Self log hyper BG goal"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_BG)
        self.phone.click(data.DM_AND_SELF_LOG_BG)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.enter('323', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        sleep(constant.INTERVAL_20)     # Waiting for survey
        self.phone.verify(data.DM_AND_GOAL_EDIT_SURVEY_WHY)
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_SURVEY_WHY_HIGH, self.phone.text(data.DM_AND_GOAL_EDIT_SURVEY_WHY))
        for item in data.DM_AND_GOAL_EDIT_SURVEY_HIGH_REASONS:
            self.phone.scroll_action(lambda: self.phone.click(item))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('323', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_normal_self_log_hypo_bg_goal(self):
        '''
        This is the test for "Self log hypo BG goal"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_BG)
        self.phone.click(data.DM_AND_SELF_LOG_BG)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.enter('56', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        sleep(constant.INTERVAL_20)     # Waiting for survey
        self.phone.verify(data.DM_AND_GOAL_EDIT_SURVEY_WHY)
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_SURVEY_WHY_LOW, self.phone.text(data.DM_AND_GOAL_EDIT_SURVEY_WHY))
        for item in data.DM_AND_GOAL_EDIT_SURVEY_LOW_REASONS:
            self.phone.scroll_action(lambda: self.phone.click(item))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('56', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_self_log_oral_med_goal(self):
        '''
        This is the test for "Self log oral med goal"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b10, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_MED)
        self.phone.click(data.DM_AND_SELF_LOG_MED)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.clear(data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.enter('10', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('10', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_self_log_insulin_goal(self):
        '''
        This is the test for "Self log insulin goal"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b100, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_MED)
        self.phone.click(data.DM_AND_SELF_LOG_MED)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.clear(data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.enter('10', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('10', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_normal_self_log_history_bg_reading(self):
        '''
        This is the test for "Self log history bg reading"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        time_today = datetime.datetime.now()
        time_tomorrow = datetime.datetime.now() + datetime.timedelta(1)
        time_shown_str_today = time_today.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_shown_str_tomorrow = time_tomorrow.strftime("%A, %B %e, %Y").replace('  ', ' ')
        time_set_str_tomorrow = time_tomorrow.strftime("%Y%m%d.%H%M%S")
        self.phone.set_time(time_set_str_tomorrow)
        self.phone.restart()
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        self.assertEqual(time_shown_str_tomorrow, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.click(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.is_element_present(data.DM_AND_GOAL_NEXT_DAY_BTN)
        self.phone.is_element_present(data.DM_AND_GOAL_LAST_DAY_BTN)
        self.assertEqual(time_shown_str_today, self.phone.text(data.DM_AND_GOAL_DATE))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_BG)
        self.phone.click(data.DM_AND_SELF_LOG_BG)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.enter('123', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_self_log_non_goal_bg(self):
        '''
        This is the test for "Self log non-goal BG"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_BG)
        self.phone.click(data.DM_AND_SELF_LOG_BG)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.click(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT)
        self.phone.verify('Pre-breakfast')
        self.phone.verify('Pre-lunch')
        self.phone.click('Pre-lunch')
        self.phone.verify(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT)
        self.assertEqual('Pre-lunch', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.enter('123', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual(2, len(self.phone.find(data.DM_AND_GOAL_ITEM)))
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_self_log_non_goal_oral_med(self):
        '''
        This is the test for "Self log non-gaol oral MED"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b10, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_MED)
        self.phone.click(data.DM_AND_SELF_LOG_MED)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.click(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT)
        self.phone.verify('Pre-breakfast')
        self.phone.verify('Pre-lunch')
        self.phone.click('Pre-lunch')
        self.phone.verify(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT)
        self.assertEqual('Pre-lunch', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.enter('10', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual(2, len(self.phone.find(data.DM_AND_GOAL_ITEM)))
        dosage = self.phone.find(data.DM_AND_GOAL_DOSAGE_OR_UNIT)
        self.assertTrue('10' in dosage[1].text)

    def test_urgent_self_log_non_goal_insulin(self):
        '''
        This is the test for "Self log non-goal insulin"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b100, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.accept_med_change()
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_MED)
        self.phone.click(data.DM_AND_SELF_LOG_MED)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_MEAL_TIME))
        self.assertEqual('Pre-breakfast', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.click(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT)
        self.phone.verify('Pre-breakfast')
        self.phone.verify('Pre-lunch')
        self.phone.click('Pre-lunch')
        self.phone.verify(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT)
        self.assertEqual('Pre-lunch', self.phone.text(data.DM_AND_GOAL_EDIT_MEAL_TIME_TEXT))
        self.phone.enter('10', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual(2, len(self.phone.find(data.DM_AND_GOAL_ITEM)))
        dosage = self.phone.find(data.DM_AND_GOAL_DOSAGE_OR_UNIT)
        self.assertTrue('10' in dosage[1].text)

    def test_urgent_self_log_bp(self):
        '''
        This is the test for "Self log BP"
        '''
        patient = mobile_setup.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_BP)
        self.phone.click(data.DM_AND_SELF_LOG_BP)
        self.phone.verify(data.DM_AND_BP_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertTrue(self.phone.is_enabled(data.DM_AND_BP_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_BP_EDIT_TIME))
        self.phone.enter('120', data.DM_AND_BP_EDIT_SYSTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.enter('80', data.DM_AND_BP_EDIT_DIASTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_BP_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual('120-80', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_normal_self_log_out_of_range_bp(self):
        '''
        This is the test for "Log out of range BP"
        '''
        patient = mobile_setup.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_BP)
        self.phone.click(data.DM_AND_SELF_LOG_BP)
        self.phone.verify(data.DM_AND_BP_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertTrue(self.phone.is_enabled(data.DM_AND_BP_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_BP_EDIT_TIME))
        self.phone.enter('620', data.DM_AND_BP_EDIT_SYSTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.enter('80', data.DM_AND_BP_EDIT_DIASTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_BP_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_BP_EDIT_ABNORMAL_ALERT_TITLE)
        self.assertEqual(data.VALUE_AND_BP_EDIT_ABNORMAL_ALERT_MESSAGE %('620/80 mmHg'), self.phone.text(data.DM_AND_BP_EDIT_ABNORMAL_ALERT_MESSAGE))
        self.phone.click(data.DM_AND_BP_EDIT_ABNORMAL_ALERT_CANCEL_BTN)
        self.phone.clear(data.DM_AND_BP_EDIT_SYSTOLIC_FIELD)
        self.phone.enter('120', data.DM_AND_BP_EDIT_SYSTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.clear(data.DM_AND_BP_EDIT_DIASTOLIC_FIELD)
        self.phone.enter('20', data.DM_AND_BP_EDIT_DIASTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_BP_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_BP_EDIT_ABNORMAL_ALERT_TITLE)
        self.assertEqual(data.VALUE_AND_BP_EDIT_ABNORMAL_ALERT_MESSAGE %('120/20 mmHg'), self.phone.text(data.DM_AND_BP_EDIT_ABNORMAL_ALERT_MESSAGE))
        self.phone.click(data.DM_AND_BP_EDIT_ABNORMAL_ALERT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual('120-20', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_normal_self_log_reverse_bp(self):
        '''
        This is the test for "Self log reverse BP"
        '''
        patient = mobile_setup.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_BP)
        self.phone.click(data.DM_AND_SELF_LOG_BP)
        self.phone.verify(data.DM_AND_BP_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertTrue(self.phone.is_enabled(data.DM_AND_BP_EDIT_DATE))
        self.assertTrue(self.phone.is_enabled(data.DM_AND_BP_EDIT_TIME))
        self.phone.enter('80', data.DM_AND_BP_EDIT_SYSTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.enter('120', data.DM_AND_BP_EDIT_DIASTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_BP_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_BP_EDIT_REVERSE_ALERT_TITLE)
        self.assertEqual(data.VALUE_AND_BP_EDIT_REVERSE_ALERT_MESSAGE, self.phone.text(data.DM_AND_BP_EDIT_REVERSE_ALERT_MESSAGE))
        self.phone.click(data.DM_AND_BP_EDIT_REVERSE_ALERT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual('80-120', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_normal_get_low_bg_alert(self):
        '''
        This is the test for "Get low BG alert"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.phone.enter('26', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        sleep(constant.INTERVAL_20)     # Waiting for survey
        self.phone.verify(data.DM_AND_GOAL_EDIT_SURVEY_WHY)
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_SURVEY_WHY_LOW, self.phone.text(data.DM_AND_GOAL_EDIT_SURVEY_WHY))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_EDIT_LOW_BG_ALERT_TITLE)
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_LOW_BG_ALERT_TITLE, self.phone.text(data.DM_AND_GOAL_EDIT_LOW_BG_ALERT_TITLE))
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_LOW_BG_ALERT_MESSAGE %('26mg/dL'), self.phone.text(data.DM_AND_GOAL_EDIT_LOW_BG_ALERT_MESSAGE))
        self.phone.click(data.DM_AND_GOAL_EDIT_LOW_BG_ALERT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('26', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_normal_get_high_bg_alert(self):
        '''
        This is the test for "Get high Bg alert"
        '''
        patient = mobile_setup.get_new_patient_account(bg=0b1000000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.phone.enter('726', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        sleep(constant.INTERVAL_20)     # Waiting for survey
        self.phone.verify(data.DM_AND_GOAL_EDIT_SURVEY_WHY)
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_SURVEY_WHY_HIGH, self.phone.text(data.DM_AND_GOAL_EDIT_SURVEY_WHY))
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        self.phone.verify(data.DM_AND_GOAL_EDIT_HIGH_BG_ALERT_TITLE)
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_HIGH_BG_ALERT_TITLE, self.phone.text(data.DM_AND_GOAL_EDIT_HIGH_BG_ALERT_TITLE))
        self.assertEqual(data.VALUE_AND_GOAL_EDIT_HIGH_BG_ALERT_MESSAGE %('726mg/dL'), self.phone.text(data.DM_AND_GOAL_EDIT_HIGH_BG_ALERT_MESSAGE))
        self.phone.click(data.DM_AND_GOAL_EDIT_HIGH_BG_ALERT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_GOAL_COMPLETED_STATUS)
        self.assertEqual('edit', self.phone.text(data.DM_AND_GOAL_HINT_LOG_EDIT))
        self.assertEqual('726', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_edit_bp(self):
        '''
        This is the test for "Edit BP"
        '''
        self.test_urgent_self_log_bp()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BP_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertFalse(self.phone.is_enabled(data.DM_AND_BP_EDIT_DATE))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_BP_EDIT_TIME))
        self.phone.clear(data.DM_AND_BP_EDIT_SYSTOLIC_FIELD)
        self.phone.enter('130', data.DM_AND_BP_EDIT_SYSTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.clear(data.DM_AND_BP_EDIT_DIASTOLIC_FIELD)
        self.phone.enter('70', data.DM_AND_BP_EDIT_DIASTOLIC_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_BP_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual('130-70', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_delete_bp(self):
        '''
        This is the test for "Delete BP"
        '''
        self.test_urgent_self_log_bp()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_BP_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertFalse(self.phone.is_enabled(data.DM_AND_BP_EDIT_DATE))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_BP_EDIT_TIME))
        self.phone.click(data.DM_AND_BP_EDIT_DELETE_BTN)
        self.phone.verify(data.DM_AND_GOAL_EMPTY_MESSAGE)

    def test_urgent_log_weight(self):
        '''
        This is the test for "Log weight"
        '''
        patient = mobile_setup.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_BOTTOM_LOG)
        self.phone.click(data.DM_AND_BOTTOM_LOG)
        self.phone.verify(data.DM_AND_SELF_LOG_WEIGHT)
        self.phone.click(data.DM_AND_SELF_LOG_WEIGHT)
        self.phone.verify(data.DM_AND_WEIGHT_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertFalse(self.phone.is_enabled(data.DM_AND_WEIGHT_EDIT_DATE))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_WEIGHT_EDIT_TIME))
        self.phone.enter('67', data.DM_AND_WEIGHT_EDIT_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_WEIGHT_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual('67', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_edit_weight(self):
        '''
        This is the test for "Edit weight"
        '''
        self.test_urgent_log_weight()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_WEIGHT_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertFalse(self.phone.is_enabled(data.DM_AND_WEIGHT_EDIT_DATE))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_WEIGHT_EDIT_TIME))
        self.phone.clear(data.DM_AND_WEIGHT_EDIT_FIELD)
        self.phone.enter('77', data.DM_AND_WEIGHT_EDIT_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_WEIGHT_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual('77', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_delete_weight(self):
        '''
        This is the test for "Delete weight"
        '''
        self.test_urgent_log_weight()
        self.phone.click(data.DM_AND_GOAL_ITEM)
        self.phone.verify(data.DM_AND_WEIGHT_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertFalse(self.phone.is_enabled(data.DM_AND_WEIGHT_EDIT_DATE))
        self.assertFalse(self.phone.is_enabled(data.DM_AND_WEIGHT_EDIT_TIME))
        self.phone.click(data.DM_AND_WEIGHT_EDIT_DELETE_BTN)
        self.phone.verify(data.DM_AND_GOAL_EMPTY_MESSAGE)

    def test_urgent_edit_self_log_bg(self):
        '''
        This is the test for "Edit self-log BG"
        '''
        self.test_urgent_self_log_non_goal_bg()
        self.phone.find(data.DM_AND_GOAL_ITEM)[1].click()
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_EDIT_VALUE_FIELD))
        self.phone.clear(data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.enter('133', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual(2, len(self.phone.find(data.DM_AND_GOAL_ITEM)))
        self.assertEqual('133', self.phone.text(data.DM_AND_GOAL_VALUE))

    def test_urgent_delete_self_log_bg(self):
        '''
        This is the test for "Delete self-log BG"
        '''
        self.test_urgent_self_log_non_goal_bg()
        self.phone.find(data.DM_AND_GOAL_ITEM)[1].click()
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.phone.hide_keyboard()
        self.assertEqual('123', self.phone.text(data.DM_AND_GOAL_EDIT_VALUE_FIELD))
        self.phone.click(data.DM_AND_GOAL_EDIT_DELETE_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual(1, len(self.phone.find(data.DM_AND_GOAL_ITEM)))

    def test_urgent_edit_self_log_oral_med(self):
        '''
        This is the test for "Edit self-log oral MED"
        '''
        self.test_urgent_self_log_non_goal_oral_med()
        self.phone.find(data.DM_AND_GOAL_ITEM)[1].click()
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_TIME))
        self.phone.clear(data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.enter('11', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual(2, len(self.phone.find(data.DM_AND_GOAL_ITEM)))
        dosage = self.phone.find(data.DM_AND_GOAL_DOSAGE_OR_UNIT)
        self.assertTrue('11' in dosage[1].text)

    def test_urgent_delete_self_log_oral_med(self):
        '''
        This is the test for "Delete self-log oral MED"
        '''
        self.test_urgent_self_log_non_goal_oral_med()
        self.phone.find(data.DM_AND_GOAL_ITEM)[1].click()
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_TIME))
        self.phone.click(data.DM_AND_GOAL_EDIT_DELETE_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual(1, len(self.phone.find(data.DM_AND_GOAL_ITEM)))

    def test_urgent_edit_self_log_insulin(self):
        '''
        This is the test for "Edit self-log insulin"
        '''
        self.test_urgent_self_log_non_goal_insulin()
        self.phone.find(data.DM_AND_GOAL_ITEM)[1].click()
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_TIME))
        self.phone.clear(data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.enter('11', data.DM_AND_GOAL_EDIT_VALUE_FIELD)
        self.phone.hide_keyboard()
        self.phone.scroll_action(lambda: self.phone.click(data.DM_AND_GOAL_EDIT_LOG_BTN))
        sleep(constant.INTERVAL_10)     # Wait animation finish
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual(2, len(self.phone.find(data.DM_AND_GOAL_ITEM)))
        dosage = self.phone.find(data.DM_AND_GOAL_DOSAGE_OR_UNIT)
        self.assertTrue('11' in dosage[1].text)

    def test_urgent_delete_self_log_insulin(self):
        '''
        This is the test for "Delete self-log insulin"
        '''
        self.test_urgent_self_log_non_goal_insulin()
        self.phone.find(data.DM_AND_GOAL_ITEM)[1].click()
        self.phone.verify(data.DM_AND_GOAL_EDIT_DATE)
        self.assertFalse(self.phone.is_enabled(data.DM_AND_GOAL_EDIT_TIME))
        self.phone.click(data.DM_AND_GOAL_EDIT_DELETE_BTN)
        self.phone.verify(data.DM_AND_GOAL_ITEM)
        self.assertEqual(1, len(self.phone.find(data.DM_AND_GOAL_ITEM)))

    def test_urgent_decline_med_change(self):
        '''
        This is the test for "Decline MED change"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b10, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_MED_CHANGE_DECLINE_BUTTON)
        self.phone.click(data.DM_AND_MED_CHANGE_DECLINE_BUTTON)
        self.phone.verify(data.DM_AND_CHAT_SEND_BTN)
        self.phone.enter('Hello, I reject the MED change.', data.DM_AND_CHAT_FIELD)
        self.phone.hide_keyboard()
        self.phone.click(data.DM_AND_CHAT_SEND_BTN)
        self.assertTrue(self.phone.is_element_present('Hello, I reject the MED change.'))
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_MED_CHANGE_DECLINE_BUTTON)
        self.phone.click(data.DM_AND_MED_CHANGE_CONFIRM_BUTTON)

    def test_normal_layout_for_special_amount_med_change(self):
        '''
        This is the test for "Layout check for special amount MED change"
        '''
        patient = mobile_setup.get_new_patient_account(med=0b1000, after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.verify(data.DM_AND_BOTTOM_GOALS)
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_MED_CHANGE_DECLINE_BUTTON)
        med_info = self.phone.find(data.DM_AND_MED_CHANGE_MED_INFO)
        med_info_list = [item.text for item in med_info]
        self.phone.swipe_up()
        med_info = self.phone.find(data.DM_AND_MED_CHANGE_MED_INFO)
        med_info_list.extend([item.text for item in med_info])
        med_info_list = list( set( med_info_list ) )
        med_info_list = '_'.join(med_info_list)
        self.assertTrue('4/5 drops x 2/3 mcg' in med_info_list)
        self.assertTrue('4.5 powder x 2.3 mL' in med_info_list)
        self.assertTrue('4,5 pieces x 2,3 mg/mL' in med_info_list)
        self.assertTrue('4+5 units' in med_info_list)
        self.phone.click(data.DM_AND_MED_CHANGE_CONFIRM_BUTTON)

    def test_normal_switch_to_previous_day_when_no_network(self):
        '''
        This is the test for 'Switch to previous day when no network'
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        time_tomorrow = datetime.datetime.now() + datetime.timedelta(1)
        time_set_str_tomorrow = time_tomorrow.strftime("%Y%m%d.%H%M%S")
        self.phone.set_time(time_set_str_tomorrow)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_BOTTOM_GOALS)
        self.phone.verify(data.DM_AND_GOAL_EMPTY_MESSAGE)
        self.phone.verify(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        self.phone.turn_off_wifi()
        self.phone.click(data.DM_AND_GOAL_PREVIOUS_DAY_BTN)
        self.phone.verify(data.DM_AND_GOAL_NO_NETWORK_MORE_INFO)
        self.assertEqual(data.EM_AND_GOAL_NO_NETWORK_MESSAGE, self.phone.text(data.DM_AND_GOAL_NO_NETWORK_MESSAGE))
        self.phone.click(data.DM_AND_GOAL_NO_NETWORK_MORE_INFO)
        self.phone.verify(data.DM_AND_NO_NETWORK_HELP_CONTENT_TITLE)
        self.phone.click(data.DM_AND_NO_NETWORK_HELP_CLOSE_BTN)

if __name__ == '__main__':
    unittest.main()
