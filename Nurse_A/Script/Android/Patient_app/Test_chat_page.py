#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time
import unittest
from Nurse_A.Scenario.web_scenario import WEB
from Nurse_A.Ext_unittest.Testcase import Case
from Nurse_A.Scenario.android_scenario import ANDROID
from Nurse_A.Settings import keycode, constant, data, setup, mobile_setup

class Chat(Case):

    def setUp(self):
        self.phone = ANDROID()

    def tearDown(self):
        self.phone.logout()
        self.phone.turn_on_wifi()
        self.phone.teardown()

    def test_urgent_send_message(self):
        '''
        This is the test for 'Send a message'
        This is the test for 'Receive a message'
        '''
        provider = WEB()
        provider.login(data.DOCTOR, setup.demo_data[0])
        patient = provider.create_new_patient()
        self.phone.signup(patient[0])
        self.phone.click(data.DM_AND_BOTTOM_CHAT)
        self.phone.verify(data.DM_AND_CHAT_SEND_BTN)
        self.phone.verify(data.DM_AND_CHAT_ICON_LEFT)
        self.phone.verify(data.DM_AND_CHAT_CONTENT)
        self.phone.enter('hello world', data.DM_AND_CHAT_FIELD)
        self.phone.click(data.DM_AND_CHAT_SEND_BTN)
        provider.refresh()
        provider.verify(data.PR_PATIENT_RECORD_CHAT)
        provider.click(data.PR_PATIENT_RECORD_CHAT)
        provider.verify(data.PR_PATIENT_RECORD_CHAT_LATEST_MES)
        self.assertEqual('hello world', provider.text(data.PR_PATIENT_RECORD_CHAT_LATEST_MES))
        provider.enter('hello patient', data.PR_PATIENT_RECORD_CHAT_TEXTAREA)
        provider.click(data.PR_PATIENT_RECORD_CHAT_SEND_BUTTON)
        self.phone.restart()
        self.phone.verify(data.DM_AND_BOTTOM_CHAT)
        self.phone.click(data.DM_AND_BOTTOM_CHAT)
        self.phone.verify('hello patient')
        provider.teardown()

    def test_normal_send_message_when_no_network(self):
        '''
        This is the test for 'Send a message when no network'
        '''
        patient = self.phone.get_new_patient_account(after_sign_up=True)
        self.phone.login(patient['email'])
        self.phone.click(data.DM_AND_BOTTOM_CHAT)
        self.phone.verify(data.DM_AND_CHAT_SEND_BTN)
        self.phone.turn_off_wifi()
        self.phone.enter('hello world', data.DM_AND_CHAT_FIELD)
        self.phone.click(data.DM_AND_CHAT_SEND_BTN)
        self.phone.verify(data.DM_AND_NO_NETWORK_TITLE)
        self.phone.click(data.DM_AND_NO_NETWORK_OK_BTN)
        self.phone.verify(data.DM_AND_CHAT_SEND_BTN)
        self.phone.click(data.DM_AND_CHAT_SEND_BTN)
        self.phone.verify(data.DM_AND_NO_NETWORK_TITLE)
        self.phone.click(data.DM_AND_NO_NETWORK_HELP_BTN)
        self.phone.verify(data.DM_AND_NO_NETWORK_HELP_CONTENT_TITLE)
        self.phone.click(data.DM_AND_NO_NETWORK_HELP_CLOSE_BTN)
        self.phone.verify(data.DM_AND_CHAT_SEND_BTN)
        self.phone.verify(data.DM_AND_NO_NETWORK_BAR)
        self.assertEqual('No internet connection', self.phone.text(data.DM_AND_NO_NETWORK_BAR_TEXT))
        self.phone.click(data.DM_AND_NO_NETWORK_BAR_CLOSE_BTN)
        self.assertFalse(self.phone.is_element_present(data.DM_AND_NO_NETWORK_BAR))
        self.phone.turn_on_wifi()
        sleep(constant.INTERVAL_10)
        self.phone.click(data.DM_AND_CHAT_SEND_BTN)
        self.assertEqual('hello world', self.phone.find(data.DM_AND_CHAT_CONTENT)[-1].text)

if __name__ == '__main__':
    unittest.main()
