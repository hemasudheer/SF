'''
Created on Sep 18, 2014

@author: hemasudheer
'''

from saunter.exceptions import ElementVisiblityTimeout
from saunter.po import timeout_seconds
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time


class SFBasePage(object):

    def type_and_press_enter(self, locator, text):
        self.wait_for_available(locator)
        element = self.view_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)
        element.send_keys(Keys.RETURN)

    def read(self, locator):
        self.wait_for_available(locator)
        text = self.driver.find_element_by_locator(locator).text
        return text

    def press(self, locator):
        self.wait_for_available(locator)
        self.view_element(locator).click()

    def tick_box(self, locator, value):
        now = self.get_element_value(locator, "checked")
        #print " now="+str(now)+ " value="+str(value)
        if (value and not now) or (not value and now):
            self.press(locator)

    def check(self, locator):
        self.wait_for_available(locator)
        self.driver.find_element_by_locator(locator).check()

    def hover(self, driver, locator):
        self.wait_for_available(locator)
        action_chains = ActionChains(driver)
        action_chains.move_to_element(\
                     self.driver.find_element_by_locator(locator)).perform()

    def hover_click(self, driver, locator):
        self.wait_for_available(locator)
        action_chains = ActionChains(driver)
        action_chains.move_to_element_with_offset(\
                    self.driver.find_element_by_locator(locator), 20, 20).\
                                                              click().perform()

    def type(self, locator, text):
        self.wait_for_available(locator)
        element = self.view_element(locator)
        element.click()
        element.clear()
        element.send_keys(text)

    def clear_text(self, locator):
        self.wait_for_available(locator)
        element = self.view_element(locator)
        element.clear()

    def get_url(self, url):
        self.driver.get(url)

    def wait_in_seconds(self, seconds):
        time.sleep(seconds)

    def select_option(self, locator, option):
        '''
        select option by order
        '''
        options = self._get_options(locator)
        options[option].click()
        print "Option Text selected is : ", self.get_selected_option(locator)

    def _get_options(self, locator):
        self.wait_for_available(locator)
        select = self.driver.find_element_by_locator(locator)
        return select.find_elements_by_tag_name('option')

    def get_select_options_data(self, locator):
        '''
        This method returns a List of comprehended List consisting of the
        drop down text values for selection
        '''
        data = []
        options = self._get_options(locator)
        data.append([option.text for option in options])
        return data

    def is_alert_present(self, locator, *seconds):
        '''
        This is method can be used to wait for an operation to generate an
        alert and also looks for if that specific operation does not generate
        an alert and also wait for the destination element, if the operation
        is successful.
        '''
        timeout = seconds[0] if seconds else timeout_seconds
        for i in range(timeout):
            try:
                alert = self.switch_to_alert()
                self.wait_in_seconds(1)
                alert.accept()
                return True
            except:
                if self.is_element_present(locator):
                    return False
                else:
                    self.wait_in_seconds(1)
                    continue
        else:
            return False

    def press_and_wait_for(self, button, verify, *args):
        self.press(button)
        if args:
            for i in range(args[0]):
                if self.is_element_available(verify):
                    break
                else:
                    time.sleep(1)
            else:
                raise ElementVisiblityTimeout("%s presence timed out" % verify)
        else:
            self.wait_for_visible(verify)

    def press_until_text_appears(self, button, verify, *seconds):
        timeout = seconds[0] if seconds else timeout_seconds
        interval_seconds = 10
        timeout /= interval_seconds
        for _ in range(timeout):
            self.press(button)
            if self.is_element_present(verify, 5):
                break
            else:
                time.sleep(interval_seconds)
                self.page_back()

    def wait_and_reload_until_element_present(self, cloud_loc, *seconds):
        print 'wait_and_reload_until_element_present call'
        timeout = seconds[0] if seconds else timeout_seconds
        print '{ Total Timeout of [%d] seconds }' % timeout
        interval_seconds = 10
        timeout /= interval_seconds
        print '{ Waiting Interval of [%d] seconds }' % interval_seconds
        for i in range(timeout):
            if self.driver.is_element_present(cloud_loc):
                return True
            else:
                print "Waiting on element presence for [%d] Seconds" % \
                                                        (i * interval_seconds)
                time.sleep(interval_seconds)
                self.page_reload()
        return False
