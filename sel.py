__author__ = 'bernardo'

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver =  webdriver.Chrome(chromedriver)

driver.get("http://minasgerais.olx.com.br/posting.php?pdw=33192&categ_id=832")

elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
#elem.send_keys(Keys.RETURN)

# get performance data
performance = driver.execute_script("return window.performance")
print performance

driver.close()