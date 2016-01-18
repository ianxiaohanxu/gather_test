#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep, time, strftime
import commands
from appium import webdriver
from selenium.common.exceptions import NoSuchElementException
from appium.webdriver.common.touch_action import TouchAction
from Nurse_A.Settings import keycode, constant
from selenium.common.exceptions import TimeoutException

class MOB(object):

    def teardown(self, DRIVER_QUIT = True):
        # Close the session or not
        if DRIVER_QUIT == True:
            self.driver.quit()
        else:
            return

    def scroll_action(self, action, direction=0, times=5):
        # Do the "action", if failed, scroll the screen at the "direction", and do it again.
        # Max scroll time is "times"
        # "direction":
        #       0: scroll up
        #       1: scroll down
        #       2: scroll right
        #       3: scroll left
        while(times>0):
            try:
                result = action()
                return result
            except:
                if direction==0:
                    self.swipe_up()
                elif direction==1:
                    self.swipe_down()
                elif direction==2:
                    self.swipe_right()
                elif direction==3:
                    self.swipe_left()
                times-=1
        raise NoSuchElementException

    def click(self, what, count = 1):
        # Click an element, for double-click, just pass in count=2
        item = self.focus(what)
        while count > 0:
            item.click()
            count-=1
            sleep(constant.INTERVAL_1)

    def long_click(self, what, duration = 1000):
        # Long click an element
        item = self.focus(what)
        action = TouchAction(self.driver)
        action.long_press(el = item, duration = duration)
        action.release()
        action.perform()

    def tap(self, x = None, y = None, count = 1):
        # Tap a coordinates (x,y)
        if (x == None) | (y == None) | (x > self.X) | (y > self.Y):
            raise AssertionError('Please input a correct coordinate')
        while count > 0:
            action = TouchAction(self.driver)
            action.press(x = x, y = y).release()
            action.perform()
            count-=1
            sleep(constant.INTERVAL_1)

    def long_tap(self, x = None, y = None, duration = 1000):
        # Long tap a coordinates (x,y)
        if (x == None) | (y == None) | (x > self.X) | (y > self.Y):
            raise AssertionError('Please input correct coordinates')
        action = TouchAction(self.driver)
        action.long_press(x = x, y = y, duration = duration).release()
        action.perform()

    def enter(self, what, where):
        # Input something into edit field
        element = self.focus(where)
        element.send_keys(what)

    def clear(self, where):
        # Clear the edit field
        element = self.focus(where)
        element.clear()

    def drag(self, origin_el = None, target_el = None, x = None, y = None):
        # Drag something to somewhere
        if not (target_el is None):
            action = TouchAction(self.driver)
            action.\
                long_press(origin_el).\
                move_to(target_el).\
                release().\
                perform()
        elif (x == None) | (y == None) | (x > self.X) | (y > self.Y):
            raise AssertionError('Please input a correct coordinate')
        else:
            action = TouchAction(self.driver)
            action.\
                long_press(origin_el).\
                move_to(x = x, y = y).\
                release().\
                perform()

    def swipe(self, start_x = None, start_y = None, end_x = None, end_y = None):
        # Swip from somewhere to somewhere
        if (start_x == None) | (start_y == None) | \
            (start_x > self.X) | (start_y > self.Y) | \
            (end_x == None) | (end_y == None) | \
            (end_x > self.X) | (end_y > self.Y):
                raise AssertionError('Please input a correct coordinate')
        action = TouchAction(self.driver)
        action\
            .press(x = start_x, y = start_y)\
            .wait()\
            .move_to(x = end_x, y = end_y)\
            .release()
        action.perform()

    def vswipe(self, start_y = None, end_y = None):
        # Vertically swipe
        self.swipe(self.X/2, start_y, self.X/2, end_y)

    def hswipe(self, start_x=None, end_x=None):
        # Horizontal swipe
        self.swipe(start_x, self.Y/2, end_x, self.Y/2)

    def swipe_up(self):
        # Vertically swipe up
        start_y = self.Y/2 + self.Y/5
        end_y = self.Y/2 - self.Y/5
        self.vswipe(start_y, end_y)

    def swipe_down(self):
        # Vertically swipe down
        start_y = self.Y/2 - self.Y/5
        end_y = self.Y/2 + self.Y/5
        self.vswipe(start_y, end_y)

    def swipe_right(self):
        # Horizontal swipe right
        start_x = self.X/2 - self.X/5
        end_x = self.X/2 + self.X/5
        self.hswipe(start_x, end_x)

    def swipe_left(self):
        # Horizontal swipe left
        start_x = self.X/2 + self.X/5
        end_x = self.X/2 - self.X/5
        self.hswipe(start_x, end_x)

    def zoom_in(self, element = None, percent = 200, steps = 50):
        # Zoom in
        self.driver.zoom(element, percent, steps)

    def zoom_out(self, element = None, percent = 200, steps = 50):
        # Zoom out
        self.driver.pinch(element, percent, steps)

    # def capture(self, what):
    #     # Capture a picture for an element
    #     begin = what.location
    #     size = what.size
    #     start_x = begin['x']
    #     start_y = begin['y']
    #     end_x = start_x + size['width']
    #     end_y = start_y + size['height']
    #     name = str(start_x)+'_'+str(start_y)+'_'+str(end_x)+'_'+str(end_y)
    #     box = (start_x, start_y, end_x, end_y)
    #     self.driver.get_screenshot_as_file(tmp + '/' + 'full_screen.png')
    #     image = Image.open(tmp + '/' + 'full_screen.png')
    #     newimage = image.crop(box)
    #     newimage.save(tmp + '/' + name + '.png')
    #     os.popen('rm %s/full_screen.png' %tmp)

    def verify(self, what, WAITTIME = 10):
        # Verify element shown on the screen
        end_time = time() + WAITTIME
        while time() < end_time:
            try:
                self.focus(what)
                return True
            except NoSuchElementException:
                pass
        raise NoSuchElementException('"%s" is not found' %what)

    def is_element_present(self, what, WAITTIME = 1):
        # Make a judgement, if the element is present or not
        end_time = time() + WAITTIME
        while time() < end_time:
            try:
                self.focus(what)
                return True
            except NoSuchElementException:
                pass
        return False

    def do_until_true(self, action, condition, times = 5):
        # Do 'action' until 'condition' is True, or try it for 'times' times
        while(times):
            if condition():
                return
            action()
            times-=1
        raise NoSuchElementException

    def do_until_false(self, action, condition, times = 5):
        # Do 'action' until 'condition' is True, or try it for 'times' times
        while(times):
            if not condition():
                return
            action()
            times-=1
        raise NoSuchElementException

    def text(self, where):
        element = self.focus(where)
        text = element.text
        return text

    def wait_until(self, condition, WAITTIME=10):
        # Wait until condition come true, default timeout is 10s.
        end_time = time() + WAITTIME
        while(time() < end_time):
            if condition():
                return
        raise TimeoutException

    def wait_until_not(self, condition, WAITTIME=10):
        # Wait until condition comes false, default timeout is 10s.
        self.wait_until(lambda: not condition(), WAITTIME=WAITTIME)

    def wait_until_present(self, element):
        # Wait until element present
        self.wait_until(lambda: self.is_element_present(element))

    def wait_until_not_present(self, element):
        # Wait until element not present
        self.wait_until_not(lambda: self.is_element_present(element))

    def hide_keyboard(self):
        # Just hide soft keyboard
        try:
            self.driver.hide_keyboard()
        except:
            return

    def get_server_ip(self):
        # Get server ip
        COMMAND = 'ip_str=$(ifconfig | grep 192.168.0.);if [[ $ip_str =~ ":" ]];then ip_str=$(echo $ip_str | awk -F ":" "{print \$2}");else ip_str=$(echo $ip_str | awk "{print \$2}");fi;ip_str="${ip_str}:8000";echo $ip_str'
        return commands.getoutput(COMMAND)
       


