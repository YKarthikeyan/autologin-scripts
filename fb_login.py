#! /usr/bin/env python3
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.facebook.com")
time.sleep(3)
browser.find_element_by_name('email').send_keys("<USER NAME>")
browser.find_element_by_name('pass').send_keys("<PASSWORD")
browser.find_element_by_id("u_0_2").click()


