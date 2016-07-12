from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unicodedata
import unittest
import re

browser=webdriver.Firefox()
browser.get("https://dashboard.ticketech.com")
browser.maximize_window()

def clean_numbers(*args):
    clean_array=[int(re.sub("[$,]", "", arg)) for arg in args]
    return clean_array

def find_float_by_id(element_id):
    element=float(browser.find_element_by_id(element_id).text)
    return element

def find_int_by_id(el_id):
    element=int(browser.find_element_by_id(el_id).text)
    return element

def find_el_by_id(el_id):
    element=browser.find_element_by_id(el_id)
    return element

def user_auth():
    username=browser.find_element_by_name("ctl00$ContentPlaceHolder1$txtUserName")
    password=browser.find_element_by_name("ctl00$ContentPlaceHolder1$txtPassword")
    submit_btn=browser.find_element_by_id("ContentPlaceHolder1_btnSubmit")
    username.send_keys("GLEdemo")
    password.send_keys("summer")
    submit_btn.click()


def total_revenue_current():
    total_current_revenue=find_float_by_id("ContentPlaceHolder1_lblAverageRevenueTotal")
    posted_transient=find_float_by_id("ContentPlaceHolder1_lblPostedTotal")
    alternate=find_float_by_id("ContentPlaceHolder1_lblAlternateTotal")
    calculation=posted_transient+alternate
	
    if total_current_revenue==calculation:
    	print "\nTOTAL REVENUE IS CORRECT!\n"
    else:
	print "TOTAL REVENUE ERROR! HERE'S HOW MUCH IT WAS OFF: " +str(total_current_revenue-calculation)+"\n" 

def total_count():
    posted=find_float_by_id("ContentPlaceHolder1_lblPostedVehicleTotal")
    alternate=find_float_by_id("ContentPlaceHolder1_lblAlternateVehicleTotal")
    total_ct=find_float_by_id("ContentPlaceHolder1_lblAverageVehicleTotal")
    calculation=posted+alternate


    if total_ct - calculation < 0.0:
	print "TOTAL COUNT IS CORRECT!\n"
    else:
	print "TOTAL COUNT ERROR! HERE'S HOW MUCH IT WAS OFF: "+str(abs(total_ct-calculation))+"\n"
	
def revenue_percent_change():
    total_rev=find_el_by_id("ContentPlaceHolder1_UltraChartRevenueByWeekActualTotal").get_attribute("title")
    historical_total_rev=find_el_by_id("ContentPlaceHolder1_UltraChartRevenueByWeekActualPrevious").get_attribute("title")
    total_percent_change=find_float_by_id("ContentPlaceHolder1_lblAverageUpDown")
    revenue_list=clean_numbers(total_rev, historical_total_rev)
    calculation=round(((float(revenue_list[0])-float(revenue_list[1]))/float(revenue_list[1]))*100, 1)

    if total_percent_change==calculation:
	print "REVENUE TOTAL PERCENT CHANGE IS CORRECT!\n"
    else:
	print "REVENUE TOTAL PERCENT CHANGE ERROR! HERE'S HOW MUCH IT WAS OFF: "+str(abs(total_percent_change)-abs(calculation))+"\n"

def count_percent_change():
    total_count=find_el_by_id("ContentPlaceHolder1_UltraChartCountByWeekActualTotal").get_attribute("title")
    historical_total_count=find_el_by_id("ContentPlaceHolder1_UltraChartCountByWeekPreviousPrevious").get_attribute("title")
    count_percent_change=find_float_by_id("ContentPlaceHolder1_lblAverageVehicleCount")
    count_list=clean_numbers(total_count, historical_total_count)
    calculation=round(((float(count_list[0])-float(count_list[1]))/float(count_list[1]))*100, 1)
	
    if count_percent_change==calculation:
	print "COUNT TOTAL PERCENT CHANGE IS CORRECT!\n"
    else:
	print "COUNT TOTAL PERCENT CHANGE ERROR! HERE'S HOW MUCH IT WAS OFF: " +str(abs(count_percent_change)-abs(calculation))+"\n"

def check_count_by_weekday_total():
    count_by_weekday_total=find_float_by_id("ContentPlaceHolder1_UltraChartCountByWeekActualTotal")
    total_count=find_float_by_id("ContentPlaceHolder1_lblAverageVehicleTotal")
    
    if count_by_weekday_total == total_count:
        print "COUNT BY WEEKDAY TOTAL IS CORRECT!\n"
    else:
        print "ERROR: COUNT BY WEEKDAY TOTAL IS SUPPOSED TO BE "+str(total_count)+" INSTEAD GOT: "+str(count_by_weekday_total) 

def check_revenue_by_weekday_total():
    revenue_by_weekday_total=find_float_by_id("ContentPlaceHolder1_UltraChartRevenueByWeekActualTotal")
    total_revenue=find_float_by_id("ContentPlaceHolder1_lblAverageRevenueTotal")

    if revenue_by_weekday_total == total_revenue:
        print "REVENUE BY WEEKDAY TOTAL IS CORRECT!\n"
    else:
        print "ERROR: REVENUE BY WEEKDAY TOTAL IS SUPPOSED TO BE "+str(total_revenue)+" INSTEAD GOT: "+str(revenue_by_weekday_total)

# ----------SCRIPT---------------
user_auth()
total_revenue_current()
total_count()
revenue_percent_change()
count_percent_change()
check_count_by_weekday_total()
check_revenue_by_weekday_total()
browser.quit()


	
