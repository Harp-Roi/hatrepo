#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


# Use options object to spec out browser
chrome_options = Options()
chrome_options.add_arguement("--headless")







# Firefox testing
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=options)
driver.get("https://onlineservices.ubs.com/olsauth/ex/pbl/ubso/dl")
driver.find_element_by_id("username").send_keys("roivantdi")
driver.find_element_by_id("password").send_keys("****")
driver.find_element_by_id("submit").click()

