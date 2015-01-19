# -*- coding: utf-8 -*-
__author__ = 'bernardo'

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display
import proxy
from selenium.webdriver.common.proxy import *

#display = Display(visible=0, size=(800, 600))
#display.start()

def post_ad(title, descri, price, username, phone):
    driver =  webdriver.Firefox() #
    #driver = proxy.my_proxy("127.0.0.1", 8118)#webdriver.Firefox()
    service_args = [
    '--proxy=111.7.129.162:8123',
    '--proxy-type=socks5',
    ]
    #browser = webdriver.PhantomJS('phantomjs',service_args=service_args)
    #driver = webdriver.PhantomJS(executable_path='./phantomjs')

    port = "8118" #The Privoxy (HTTP) port
    myProxy = "127.0.0.1:"+port
    proxy = Proxy({
        'proxyType': ProxyType.MANUAL,
        'httpProxy': myProxy,
        'ftpProxy': myProxy,
        'sslProxy': myProxy,
        'noProxy': ''
    })
    #driver = webdriver.Firefox(proxy=proxy)


    driver.set_window_size(800, 600)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(-1)
    driver.implicitly_wait(-1)
    straturl = "http://minasgerais.olx.com.br/posting.php?pdw=33192&categ_id=832"
    try:
        driver.get(straturl)
    except:
        #
        driver.execute_script("window.stop();")
        print "TIMED OUT"
    print "running"
    driver.save_screenshot('screen.png')
    elem = driver.find_element_by_name("title")
    elem.send_keys(title)

    elem = driver.find_element_by_name("newDescription")
    elem.send_keys(descri)

    elem = driver.find_element_by_name("C")
    elem.send_keys(price)

    elem = driver.find_element_by_name("contact-name")
    elem.send_keys(username)

    elem = driver.find_element_by_name("phone")
    elem.clear()
    elem.send_keys(phone)

    elem = driver.find_element_by_name("email")
    elem.send_keys("email@trbvm.com")

    elem = driver.find_element_by_name("state")
    #elem.send_keys("Minas Gera")

    select = Select(driver.find_element_by_name("region_ddd"))
    select.select_by_value("25")
    time.sleep(5)
    select = Select(driver.find_element_by_name("city"))

    select.select_by_value("52491") # BElo horizonte
    time.sleep(5)
    driver.find_element_by_class_name("olx-ui-button").click();
    print "sent, now waiting"
    while driver.current_url == straturl:
        time.sleep(1)
    time.sleep(10)
    driver.quit()


post_ad("Celular sony xperia M2", u"muito bem criado pela sony estou agora é vendendo", "250", "flavi cardoso", "3100364628")