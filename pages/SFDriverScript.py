'''
Created on Oct 22, 2014

@author: hemasudheer
'''

from selenium import webdriver
import unittest2 as unittest


class SFDriverScript(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        SFDriverScript.driver = webdriver.Firefox()

    @classmethod
    def tearDownClass(cls):
        SFDriverScript.driver.quit()
