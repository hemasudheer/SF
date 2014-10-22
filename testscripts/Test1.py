'''
Created on Oct 22, 2014

@author: hemasudheer
'''
from pages.SFDriverScript import SFDriverScript


class CheckTest1(SFDriverScript):

    def test_name1(self):
        self.driver.get("https://login.salesforce.com/")
        print self.driver.title
        print "this is from my mbp"