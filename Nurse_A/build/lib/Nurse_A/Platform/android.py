#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mobile import MOB
from time import sleep
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from Nurse_A.Settings import keycode, constant

HARDKEY = {
    'Power' : keycode.KEYCODE_POWER,
    'Camera' : keycode.KEYCODE_CAMERA,
    'Volumn_Up' : keycode.KEYCODE_VOLUME_UP,
    'Volumn_Down' : keycode.KEYCODE_VOLUME_DOWN,
    'Home' : keycode.KEYCODE_HOME,
    'Back' : keycode.KEYCODE_BACK,
    'Menu' : keycode.KEYCODE_MENU,
}

class AND(MOB):
    # def __init__(self, PORT = '4723', PKG = 'com.gatherhealth.gatherdm', ACT = '.activity.MainActivity'):
    #     # Create a new session with passed in Port, package and activity
    #     address = 'http://localhost:'+PORT+'/wd/hub'
    #     caps = {
    #         'deviceName' : 'Sony',
    #         'platformName' : 'Android',
    #         'platformVersion' : '4.2',
    #         'appPackage' : PKG,
    #         'appActivity' : ACT,
    #     }
    #     self.driver = webdriver.Remote(address, caps)
    #     # Get resolution
    #     self.X = self.driver.get_window_size()['width']
    #     self.Y = self.driver.get_window_size()['height']
    #     # Package name
    #     self.package_name = PKG
        
    def press(self, keyName, count = 1):
        # Press hardkey, if double press, pass in 'count = 2'
        try:
            assert keyName in HARDKEY.keys()
        except AssertionError:
            raise AssertionError('Hard key name "%s" is wrong.' %keyName)
        while count > 0:
            self.driver.press_keycode(HARDKEY[keyName])
            count-=1
            sleep(constant.INTERVAL_5)
        return
        
    def long_press(self, keyName):
        # Long press hardkey
        try:
            assert keyName in HARDKEY.keys()
        except AssertionError:
            raise AssertionError('Hard key name "%s" is wrong.' %keyName)
        self.driver.long_press_keycode(HARDKEY[keyName])
        return self
      
    def focus(self, what):
        # Find an element, return webelement object. 
        # For 'what', you can use resource id, text, partial text and xpath.
        try:
            item = self.driver.find_element_by_id(self.package_name+':id/'+what)
            return item
        except NoSuchElementException:
            pass
        try:
            item = self.driver.find_element_by_id('android'+':id/'+what)
            return item
        except NoSuchElementException:
            pass
        try:
            item = self.driver.find_element_by_android_uiautomator('text("%s")' %what)
            return item
        except NoSuchElementException:
            pass            
        try:
            item = self.driver.find_element_by_android_uiautomator('description("%s")' %what)
            return item
        except NoSuchElementException:
            pass               
        try:
            item = self.driver.find_element_by_android_uiautomator('textContains("%s")' %what)
            return item
        except NoSuchElementException:
            pass           
        try:
            item = self.driver.find_element_by_android_uiautomator('descriptionContains("%s")' %what)
            return item
        except NoSuchElementException:
            pass
        try:
            item = self.driver.find_element_by_xpath(what)
            return item
        except NoSuchElementException:
            raise NoSuchElementException('Element not found by "%s"' %what)
            
    def find(self, what):
        # Find elements by what
        items = self.driver.find_elements_by_id(self.package_name+':id/'+what)
        if not len(items) == 0:
            return items
        items = self.driver.find_elements_by_id('android'+':id/'+what)
        if not len(items) == 0:
            return items
        items = self.driver.find_elements_by_android_uiautomator('text("%s")' %what)
        if not len(items) == 0:
            return items
        items = self.driver.find_elements_by_android_uiautomator('description("%s")' %what)
        if not len(items) == 0:
            return items
        items = self.driver.find_elements_by_android_uiautomator('textContains("%s")' %what)
        if not len(items) == 0:
            return items
        items = self.driver.find_elements_by_android_uiautomator('descriptionContains("%s")' %what)
        if not len(items) == 0:
            return items
        items = self.driver.find_elements_by_xpath(what)
        if not len(items) == 0:
            return items
        raise NoSuchElementException('Element not found by "%s"' %what)
        
    def login(self, username = 'pt034@test.com', password = 'test'):
        # Log in with an exist patient account
        self.verify('Better')
        self.click('enter')
        self.waituntil('Please enter your e-mail to get started.')
        self.enter(username, 'login_email')
        self.click('next')
        self.waituntil('Please enter your password.')
        self.enter(password, 'login_password')
        self.click('sign in')
        self.waituntil('main_button0_text')