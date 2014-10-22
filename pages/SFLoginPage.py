'''
Created on Oct 22, 2014

@author: hemasudheer
'''
from pages.SFBasePage import SFBasePage
locators = {"username": "xpath=//input[@id='username']",
            "password": "xpath=//input[@id='password']",
            "login_button": "xpath=/*[@id='Login']",
            }


class SFLoginPage(SFBasePage):

    def do_login(self):
        self.type(locators("username"), "hsksudheer@gmail.com")
        self.type(locators("username"), "hsksudheer@gmail.com")

