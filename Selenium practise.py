from selenium import webdriver
from selenium.webdriver.support.select import Select
import pickle

driver=webdriver.Chrome(r"C:\Users\janik\Desktop\chromedriver.exe")

driver.get("https://www.timeanddate.com")
driver.find_element_by_id("privacyframe_q2").click()

selectelement = driver.find_element_by_id("month")
months = Select(selectelement)
months.select_by_visible_text("May")

countrypath = driver.find_element_by_id("country")
country = Select(countrypath)
country.select_by_visible_text("China")
driver.find_element_by_xpath("//form[@id='cf']//input[@value='View Calendar']").click()