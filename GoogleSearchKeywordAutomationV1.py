# -*- coding: utf-8 -*-
"""
Title: Google Search Keyword Automation with Python Selenium 
Version:1.0
Created on Fri Nov 12 15:03:18 2021

@author: tommas.huang
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

driver = webdriver.Chrome(executable_path=os.path.abspath(r"C:\Users\tommas.huang\Desktop\IGCrawler5\chromedriver"))
driver.get("http://www.google.com")

que=driver.find_element_by_xpath("//input[@name='q']")
que.send_keys("tsmc AI")
que.send_keys(Keys.RETURN)