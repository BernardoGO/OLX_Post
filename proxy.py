__author__ = 'bernardo'
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import Select
from pyvirtualdisplay import Display

def my_proxy(PROXY_HOST,PROXY_PORT):
    fp = webdriver.FirefoxProfile()
    # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
    print PROXY_PORT
    print PROXY_HOST
    fp.set_preference("network.proxy.type", 1)
    fp.set_preference("network.proxy.http",PROXY_HOST)
    fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
    fp.set_preference("general.useragent.override","Android")
    fp.set_preference( "permissions.default.image", 2 )
    fp.update_preferences()
    return webdriver.Firefox(firefox_profile=fp)

#driver = my_proxy("183.207.229.196", 8888)

#driver.get("http://www.meuip.com.br/")