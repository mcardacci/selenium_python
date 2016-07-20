from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
import time
import sys

browser=webdriver.Firefox()
browser.get("http://suite.ticketech.com/login.aspx")
browser.maximize_window()
print sys.argv[1]

def find_el_by_id(el_id):
	element=browser.find_element_by_id(el_id)
	return element

def user_auth():
	username=browser.find_element_by_name("ctl00$PrincipalPanel$loginControl$UserName")
	password=browser.find_element_by_name("ctl00$PrincipalPanel$loginControl$Password")
	submit_btn=browser.find_element_by_id("PrincipalPanel_loginControl_LoginButton")
	username.send_keys("put username here")
	password.send_keys("put password here")
	submit_btn.click()

def click_conf_center():
	conf_center_btn=browser.find_element_by_partial_link_text('Conf.')
	conf_center_btn.click()

def search_for_garage():
        location = sys.argv[1]
	wait = WebDriverWait(browser, 20)
	search_bar= wait.until(EC.presence_of_element_located((By.NAME,'ctl00$LeftPanel$txtSearch')))
	search_btn=find_el_by_id("LeftPanel_btnSearch__5")
	search_bar.send_keys(location)
	search_btn.click()

def click_policies_maitenance():
        time.sleep(10)
        browser.get("http://suite.ticketech.com/ConfCenter/Policies/Policies_v2.aspx")

def click_communications_tab():
        time.sleep(5)
        communications_tab = browser.find_element_by_class_name("igtab_THText")
        communications_tab.click()

def set_transmission_strings():
        export_folder = find_el_by_id("ctl00_Contents_TabsPolicies_tmpl15_txtTMFilesFtpExportFolder")
        import_folder = find_el_by_id("ctl00_Contents_TabsPolicies_tmpl15_txtTMFilesFtpImportFolder")
        save_btn = find_el_by_id("Contents_btnSave")
        import_folder.clear()
        export_folder.clear()
        export_folder.send_keys("ftp://ticketech.iconquikpark.com/Upload/")
        import_folder.send_keys("ftp://ticketech.iconquikpark.com/") 
        save_btn.click()
        time.sleep(20)

def click_transmission_send_policies():
	time.sleep(10)
	browser.get("http://suite.ticketech.com/ConfCenter/Transmission/SendPolicies/TransSendPolicies.aspx") 
	
def click_send_policies_btn():
	send_policies_btn=find_el_by_id("Contents_btnSendPolicies")
	send_policies_btn.click()

#--------------------SCRIPT-----------------------------------

user_auth()
click_conf_center()
search_for_garage()
click_policies_maitenance()
click_communications_tab()
set_transmission_strings()
click_transmission_send_policies()
click_send_policies_btn()
