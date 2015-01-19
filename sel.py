__author__ = 'bernardo'

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import timer

chromedriver = "./chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver =  webdriver.Chrome(chromedriver)

driver.get("http://minasgerais.olx.com.br/posting.php?pdw=33192&categ_id=832")

elem = driver.find_element_by_name("title")
elem.send_keys("smartphone selenium")
#elem.send_keys(Keys.RETURN)

elem = driver.find_element_by_name("newDescription")
elem.send_keys("smartphone selenium bem conservado e legal")

elem = driver.find_element_by_name("C")
elem.send_keys("5000")

elem = driver.find_element_by_name("contact-name")
elem.send_keys("mauricio")

elem = driver.find_element_by_name("email")
elem.send_keys("bernardoa2003@yahoo.com.br")

elem = driver.find_element_by_name("state")
elem.send_keys("Minas Gera")

elem = driver.find_element_by_name("region_ddd")
elem.send_keys("D")

elem = driver.find_element_by_name("city")
elem.send_keys("Belo Horizonte")
time.sleep( 5 )

# get performance data
#performance = driver.execute_script("return window.performance")
#print performance

#driver.close()