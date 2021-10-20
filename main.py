import pandas as pd
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as E
from selenium.webdriver.support.ui import WebDriverWait as W



#secotion of retrieving pass and login
file = pd.read_excel('notification.xlsx')
login = file.username[0]
password = file.password[0]

# #setting up driver and landing page
# PATH = '/usr/local/bin/chromedriver'
# browser = webdriver.Chrome(PATH)
# browser.get('https://www.google.com/gmail/about/#')
#
# #loggin in into google
# signinx = "//a[contains(text(),'Sign in')]"
# emailx = "//input[@id='identifierId']"
# nextbtn = "//body/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/button[1]"
# passx = "//input[@name='password']"
# compose = "//div[contains(text(),'Compose')]"
#
#
# frame_id = "gtn-roster-iframe-id"
# frame_id2 = "wblh0.39374292812640177-0"
# frame_id3 = "wblh0.39374292812640177-1"
# frame_name4 = "__HC_94253229"
#
# sendto = "//textarea[@id=':at']"
# textinp = "//div[@id=':bb']"
# inputsubject = "//div[@id=':a5']"
#
# browser.find_element_by_xpath(signinx).click()
# browser.find_element_by_xpath(emailx).send_keys(login)
# browser.find_element_by_xpath(nextbtn).click()
# browser.implicitly_wait(200)
# browser.find_element_by_xpath(passx).send_keys(password)
# browser.find_element_by_xpath(nextbtn).click()
# browser.find_element_by_xpath(compose).click()



# browser.implicitly_wait(1000)
# browser.switch_to.frame(browser.find_element_by_id(frame_id))
# browser.find_element_by_xpath(sendto).send_keys("deniskhomenko@yahoo.com")
# browser.find_element_by_xpath(textinp).send_keys("deniskhomenko@yahoo.com")

# frames = browser.find_elements_by_tag_name("iframe")
#
# for f in frames:
#     print("Frame id:", f.get_attribute("id"), "Frame class:",f.get_attribute("class"), "Frame name:", f.get_attribute("name"),"\n")
