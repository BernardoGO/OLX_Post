__author__ = 'bernardo'

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display
import proxy

#display = Display(visible=0, size=(800, 600))
#display.start()
"""
chromedriver = "./phantomjs"
os.environ["webdriver.phantomjs.driver"] = chromedriver
driver =  webdriver.PhantomJS(chromedriver)

"""

#chromedriver = "./chromedriver"
#os.environ["webdriver.chrome.driver"] = chromedriver

driver =  proxy.my_proxy("210.61.12.12", 3128)#webdriver.Firefox()
driver.set_page_load_timeout(20)

driver.get("http://minasgerais.olx.com.br/posting.php?pdw=33192&categ_id=832")

elem = driver.find_element_by_name("title")
elem.send_keys("smartphone selenium quad core")

elem = driver.find_element_by_name("newDescription")
elem.send_keys("bem conservado comprei amanha")

elem = driver.find_element_by_name("C")
elem.send_keys("5000")

elem = driver.find_element_by_name("contact-name")
elem.send_keys("sergio")

elem = driver.find_element_by_name("phone")
elem.clear()
elem.send_keys("3193665458")

elem = driver.find_element_by_name("email")
elem.send_keys("c4048413@trbvm.com")

elem = driver.find_element_by_name("state")
#elem.send_keys("Minas Gera")

select = Select(driver.find_element_by_name("region_ddd"))
select.select_by_value("25")
time.sleep(5)
select = Select(driver.find_element_by_name("city"))

select.select_by_value("52491")

driver.find_element_by_class_name("olx-ui-button").click();
print "sent"
time.sleep(10)
driver.quit()
# get performance data
#performance = driver.execute_script("return window.performance")
#print performance

#driver.close()