#! /usr/bin/env python3
from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get("https://www.instagram.com/accounts/login/")
time.sleep(3)
browser.find_element_by_name('username').send_keys("<USER NAME>")
browser.find_element_by_name('password').send_keys("<PASSWORD>")
browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/span/button').click()

