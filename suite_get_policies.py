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

def find_el_by_id(el_id):
	element=browser.find_element_by_id(el_id)
	return element

def user_auth():
	username=browser.find_element_by_name("ctl00$PrincipalPanel$loginControl$UserName")
	password=browser.find_element_by_name("ctl00$PrincipalPanel$loginControl$Password")
	submit_btn=browser.find_element_by_id("PrincipalPanel_loginControl_LoginButton")
	username.send_keys("Gabrielm")
	password.send_keys("obama")
	submit_btn.click()

def click_conf_center():
	conf_center_btn=browser.find_element_by_partial_link_text('Conf.')
	conf_center_btn.click()

def search_for_garage():
	wait = WebDriverWait(browser, 20)
	search_bar= wait.until(EC.presence_of_element_located((By.NAME,'ctl00$LeftPanel$txtSearch')))
	search_btn=find_el_by_id("LeftPanel_btnSearch__5")
	search_bar.send_keys("mlh350")
	search_btn.click()

def click_transmission():
	time.sleep(10)
	browser.get("http://suite.ticketech.com/ConfCenter/Transmission/ExportPolicies/TransExportPolicies.aspx") 
	
def check_send_full_policies_box():
	check_box=find_el_by_id("Contents_chkSendFullPolicies")
	check_box.click()

def click_export_policies_btn():
	export_policies_btn=find_el_by_id("Contents_btnExportPolicies")
	export_policies_btn.click()

#--------------------SCRIPT-----------------------------------
if sys.argv==False:
    print "you must provide options"
    print "-f is for full policies"
    print "also provide location codes"

user_auth()
click_conf_center()
search_for_garage()
click_transmission()
if sys.argv and "-f" in sys.argv:
    check_send_full_policies_box()

click_export_policies_btn()
