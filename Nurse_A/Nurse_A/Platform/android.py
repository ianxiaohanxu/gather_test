#!/usr/bin/env python
# -*- coding: utf-8 -*-
from mobile import MOB
from time import sleep, strftime, time
import commands
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

    def is_enabled(self, what):
        # Judge if an element is enabled
        element = self.focus(what)
        status_str = element.get_attribute('enabled')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def is_checkabled(self, what):
        # Judge if an element is checkabled
        element = self.focus(what)
        status_str = element.get_attribute('checkable')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def is_checked(self, what):
        # Judge if an element is checked
        element = self.focus(what)
        status_str = element.get_attribute('checked')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def is_focusable(self, what):
        # Judge if an element is focusable
        element = self.focus(what)
        status_str = element.get_attribute('focusable')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def is_focused(self, what):
        # Judge if an element is focused
        element = self.focus(what)
        status_str = element.get_attribute('focused')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def is_clickable(self, what):
        # Judge if an element is clickable
        element = self.focus(what)
        status_str = element.get_attribute('clickable')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def is_longclickable(self, what):
        # Judge if an element is longClickable
        element = self.focus(what)
        status_str = element.get_attribute('longClickable')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def is_scrollable(self, what):
        # Judge if an element is scrollable
        element = self.focus(what)
        status_str = element.get_attribute('scrollable')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def is_selected(self, what):
        # Judge if an element is selected
        element = self.focus(what)
        status_str = element.get_attribute('selected')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def is_displayed(self, what):
        # Judge if an element is displayed
        element = self.focus(what)
        status_str = element.get_attribute('displayed')
        if status_str == 'true':
            return True
        elif status_str == 'false':
            return False

    def resourceID(self, what):
        # Show resource ID for the element
        element = self.focus(what)
        return element.get_attribute('resourceId')

    def className(self, what):
        # Show class name for the element
        element = self.focus(what)
        return element.get_attribute('className')

    def contentDescription(self, what):
        # Show content description for the element
        element = self.focus(what)
        return element.get_attribute('contentDescription')

    def start_app(self, package=None, activity=None):
        # Launch the app
        if package == None:
            package = self.package_name
        if activity == None:
            activity = self.activity_name
        self.driver.start_activity(package, activity)

    def launch_app(self):
        # Launch test app
        self.driver.launch_app()

    def close_app(self):
        # Close test app
        self.driver.close_app()

    def reset_time(self):
        # Set the date and time to current point
        current_time = strftime("%Y%m%d.%H%M%S")
        result = commands.getstatusoutput('adb shell date -s "%s"' %current_time)
        if result[0] != 0:
            raise Exception("Reset time failed!")

    def set_time(self, time_str):
        # Set date and time 
        result = commands.getstatusoutput('adb shell date -s "%s"' %time_str)
        if result[0] != 0:
            raise Exception("Set time failed!")

    def turn_off_wifi(self):
        # Turn off wifi
        result = commands.getstatusoutput('adb shell svc wifi disable')
        assert not result[0], "Fail to turn wifi off"

    def turn_on_wifi(self, WAITTIME=20):
        # Turn on wifi
        result = commands.getstatusoutput('adb shell svc wifi enable')
        assert not result[0], "Fail to turn wifi on"
        expire_time = time() + WAITTIME
        while (time() < expire_time):
            result = commands.getoutput('adb shell ifconfig wlan0')
            result += commands.getoutput('adb shell ifconfig eth1')
            if  'ip' in result:
                return
        raise Exception("Fail to turn wifi on")

