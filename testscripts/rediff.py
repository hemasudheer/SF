'''
Created on Sep 18, 2014

@author: hemasudheer
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os.path
import unittest

URL = "http://money.rediff.com/"
locators = {"searchbox": "//*[@id='srchword']",
            "quotebutton": "//*[contains(@class,'btn_srch')]",
            "pageready": "//span[contains(@class, 'moneywizlogo')]",
            "req_company": "//*[@id='for_BSE']/h1"
            }
company_name = "JK Cement Ltd."
path = "~/Documents/Myframeworkprofile"


class Test(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testRediffmoney(self):
        profile = webdriver.FirefoxProfile(os.path.expanduser(path))
        driver = webdriver.Firefox(profile)
        driver.get(URL + "gainers/bse")
        driver.implicitly_wait(10)
        webpagename = driver.find_element_by_xpath(locators['pageready'])
        print "webpage is " + webpagename.text
        assert webpagename.text == "Rediff Moneywiz"
        element = driver.find_element_by_xpath(locators['searchbox'])
        element.send_keys(company_name)
        element.send_keys(Keys.RETURN)
        company = driver.find_element_by_xpath(locators['req_company'])
        print "Current company is " + company.text
        assert company_name in company.text


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testRediffmoney']
    unittest.main()