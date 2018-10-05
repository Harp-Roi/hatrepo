#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os


# Use options object to spec out browser
chrome_options = Options()
chrome_options.add_arguement("--headless")
chrome_options.add_argument("--
