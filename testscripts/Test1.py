'''
Created on Oct 22, 2014

@author: hemasudheer
'''
from pages.SFDriverScript import SFDriverScript
from pages.SFLoginPage import SFLoginPage


class CheckTest1(SFDriverScript):

    def test_login_to_portal(self):
        login = SFLoginPage(self.driver)
        login.do_login()
#         assert login.is_logged_in()
