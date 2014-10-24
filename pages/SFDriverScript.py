'''
Created on Oct 22, 2014

@author: hemasudheer
'''

from pages.SFSetup import browser, chromedriver
from selenium import webdriver
import os
import unittest2 as unittest


class SFDriverScript(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if browser == "firefox":
            SFDriverScript.driver = webdriver.Firefox()
        elif browser == "chrome":
            os.environ["webdriver.chrome.driver"] = chromedriver
            SFDriverScript.driver = webdriver.Chrome(chromedriver)

    @classmethod
    def tearDownClass(cls):
        SFDriverScript.driver.quit()
