#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoSuchFrameException
from selenium.common.exceptions import NoSuchWindowException
from time import sleep, time
from Nurse_A.Settings import keycode, constant


class Web(object):
    """
    Include common web actions with wrapping selenium methods
    """ 
    def teardown(self, DRIVER_QUIT = True, HOMEPAGE = True):
        # Close the session, or just go to homepage, or keep the current page
        if DRIVER_QUIT == True:
            self.driver.quit()
        elif HOMEPAGE == True:
            self.driver.get(self.HOMEPAGE)
        else:
            return
        
    def focus(self, what):
        # Find element by different methods, if no element found, raise NoSuchElementException.
        # For 'what', you can use link text, css, class name, id, name, partial link text and xpath.
        try:
            element = self.driver.find_element(by = By.LINK_TEXT, value = what)
            return element
        except NoSuchElementException:
            pass
        try:
            element = self.driver.find_element(by = By.CSS_SELECTOR, value = what)
            return element
        except NoSuchElementException:
            pass
        try:
            element = self.driver.find_element(by = By.CLASS_NAME, value = what)
            return element
        except NoSuchElementException:
            pass
        try:
            element = self.driver.find_element(by = By.ID, value = what)
            return element
        except NoSuchElementException:
            pass
        try:
            element = self.driver.find_element(by = By.NAME, value = what)
            return element
        except NoSuchElementException:
            pass
        try:
            element = self.driver.find_element(by = By.PARTIAL_LINK_TEXT, value = what)
            return element
        except NoSuchElementException:
            pass
        try:
            element = self.driver.find_element(by = By.XPATH, value = what)
            return element
        except NoSuchElementException:
            raise NoSuchElementException('Element not found by "%s"' %what)
            
    def find(self, what):
        # Find elements by what
        elements = self.driver.find_elements(by = By.LINK_TEXT, value = what)
        if not len(elements) == 0:
            return elements
        elements = self.driver.find_elements(by = By.CSS_SELECTOR, value = what)
        if not len(elements) == 0:
            return elements
        elements = self.driver.find_elements(by = By.CLASS_NAME, value = what)
        if not len(elements) == 0:
            return elements
        elements = self.driver.find_elements(by = By.ID, value = what)
        if not len(elements) == 0:
            return elements
        elements = self.driver.find_elements(by = By.NAME, value = what)
        if not len(elements) == 0:
            return elements
        elements = self.driver.find_elements(by = By.PARTIAL_LINK_TEXT, value = what)
        if not len(elements) == 0:
            return elements
        elements = self.driver.find_elements(by = By.XPATH, value = what)
        if not len(elements) == 0:
            return elements
        raise NoSuchElementException('Element not found by "%s"' %what)        
            
    def click(self, what):
        # Click something, e.g. link, button
        self.focus(what).click()
        
    def enter(self, what, where):
        # Enter something to edit field
        element = self.focus(where)
        element.send_keys(what)
        
    def clear(self, where):
        # Clear edit field
        element = self.focus(where)
        element.clear()
        
    def select(self, what, where):
        # Select from drop down list
        element = self.focus(where)
        Select(element).select_by_value(what)
        
    def verify(self, what, WAITTIME = 10):
        # Verify element is shown on page
        end_time = time() + WAITTIME
        while time() < end_time:
            try:
                assert self.focus(what).is_displayed()
                return
            except:
                pass
        raise NoSuchElementException('"%s" is not found' %what)
        
    def text(self, where):
        # Text content of element
        element = self.focus(where)
        value = element.get_attribute('value')
        text = element.text
        if element.tag_name == 'input':
            return value
        else:
            return text
    
    @property    
    def title(self):
        # Title of the page
        return self.driver.title
        
    def is_selected(self, where):
        # Check ridio box or check box selected or not
        element = self.focus(where)
        return element.is_selected()
        
    def back(self):
        # Go back
        self.driver.back()
        
    def forward(self):
        # Go forward
        self.driver.forward()
        
    def refresh(self):
        # Refresh the page
        self.driver.refresh()
                   
    def is_element_present(self, what):
        # Make a judgement, if the element is present or not
        try:
            element = self.focus(what)
        except NoSuchElementException:
            return False
        try:
            assert element.is_displayed()
            return True
        except AssertionError:
            return False