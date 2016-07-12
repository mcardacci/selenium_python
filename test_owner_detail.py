from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodedata
import unittest
import re

class OwnerSummaryTest(unittest.TestCase):
    
    def find_el_by_id(self,el_id):
        element=self.browser.find_element_by_id(el_id)
        return element
   
    def find_el_by_name(self, el_name):
        element=self.browser.find_element_by_name(el_name)
        return element
   
    def find_float_by_id(self, element_id):
        element=float(self.browser.find_element_by_id(element_id).text)
        return element
   
    def setUp(self):
        self.browser=webdriver.Firefox()
   	self.browser.get("https://dashboard.ticketech.com/login.aspx")
        self.browser.maximize_window()
   	username=self.browser.find_element_by_name("ctl00$ContentPlaceHolder1$txtUserName")
   	password=self.browser.find_element_by_name("ctl00$ContentPlaceHolder1$txtPassword")
   	submit_btn=self.browser.find_element_by_id("ContentPlaceHolder1_btnSubmit")
   	username.send_keys("")
   	password.send_keys("")
   	submit_btn.click()

    def tearDown(self):
        self.browser.quit()
    
    def test_check_title(self):
        title=self.browser.title
        self.assertEqual(title, "Owner Board Detail", "BROWSER TITLE SHOULD BE 'Login Page' INSTEAD GOT: "+self.browser.title)
    
    def test_total_current_revenue(self):
        total_current_revenue=self.find_float_by_id("ContentPlaceHolder1_lblAverageRevenueTotal")
        posted_transient=self.find_float_by_id("ContentPlaceHolder1_lblPostedTotal")
        alternate=self.find_float_by_id("ContentPlaceHolder1_lblAlternateTotal")
        calculation=posted_transient+alternate
		
	self.assertEqual(total_current_revenue, calculation, "THE TOTAL CURRENT REVENUE DOES NOT EQUAL ALTERNATE+POSTED INSTEAD GOT: "+str(calculation))
    
    def test_total_count(self):
        total_count=self.find_float_by_id("ContentPlaceHolder1_lblAverageVehicleTotal")
        posted_vehicle_total=self.find_float_by_id("ContentPlaceHolder1_lblPostedVehicleTotal")
        alternate_vehicle_total=self.find_float_by_id("ContentPlaceHolder1_lblAlternateVehicleTotal")
        calculation=posted_vehicle_total+alternate_vehicle_total

        self.assertEqual(total_count, calculation, "THE TOTAL COUNT DOES NOT EQUAL ALTERNATE+POSTED, INSTEAD GOT: "+str(calculation))


if __name__=="__main__":
	unittest.main()
