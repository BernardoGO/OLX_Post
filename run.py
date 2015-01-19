# -*- coding: utf-8 -*-

import csv
import mechanize
import re
import time
import BeautifulSoup

"""
ua = 'Mozilla/5.0 (X11; Linux x86_64; rv:18.0) Gecko/20100101 Firefox/18.0 (compatible;)'
browser = mechanize.Browser()
browser.set_handle_robots(False)

browser.addheaders = [('User-agent', 'Firefox')]
start = 0
continuar = True
links = []

browser.open("http://minasgerais.olx.com.br/posting.php?pdw=33192&categ_id=832")
html = browser.response().get_data()


html = html

formcount=0
for frm in browser.forms():
    if str(frm.attrs["id"])=="posting-form-1":
        print "found"
        break
    formcount=formcount+1

browser.select_form(nr=formcount)

browser.form['title'] = "Tablet Lenovo S5000"
browser.form['newDescription'] = "muito novo e conservado"
browser.form['C'] = "500,00"
"""


import requests
from requests import session

payload = {
'action': 'validate',
'_classifiedType':'0',
'formHash':'4cc10e6a25991e69841b8e253c297e16',
'listing_type':'2',
'priority':'',
'ad_language_id':'11',
'categoryID':'832',
'countryID':'30',
'sessionHash':'36731',
'categoryChild':'832',
'categoryParent':'830',
'title':'celular moto x',
'max_orderAux':'1',
'imageQty':'0',
'f[${id}][order]':'21',
'f[${id}][edited]':'0',
'f[${id}][text]':'Descrição da foto (Opcional)',
'sell_session':'14216243477464114431107',
'description':'bem conservado de mulher',
'newDescription':'bem conservado de mulher',
'currency_typeC':'30',
'C':'500,00',
'priceC':'500',
'':'',
'identity':'1',
'contact-name':'romario',
'email':'c4040401@trbvm.com',
'phone':'(31) 9518 6655',
'zip':'',
'state':'6842',
'region_ddd':'25',
'currentZipValue':'',
'city':'52491',
'neighborhood':'0',
'neighborhood_id':'0',
'neighborhood_name':'',
'countryStateCityCase':'1',
'usesAutoComplete':'',
'useNeighborhoodMultiSelector':'',
'streetaddress':'',
'addresslat':'',
'addresslng':'',
'':'',
'security_code':'undefined',
'captchaKey':'undefined}'
}

url1 = 'http://minasgerais.olx.com.br/ajax/posting_in_one_step_ajax.php'


with session() as c:
    c.post(url1, data=payload)

payload = {
'action': 'post',
'_classifiedType':'0',
'formHash':'4cc10e6a25991e69841b8e253c297e16',
'listing_type':'2',
'priority':'',
'ad_language_id':'11',
'categoryID':'832',
'countryID':'30',
'sessionHash':'36731',
'categoryChild':'832',
'categoryParent':'830',
'title':'celular moto x',
'max_orderAux':'1',
'imageQty':'0',
'f[${id}][order]':'21',
'f[${id}][edited]':'0',
'f[${id}][text]':'Descrição da foto (Opcional)',
'sell_session':'14216243477464114431107',
'description':'bem conservado de mulher',
'newDescription':'bem conservado de mulher',
'currency_typeC':'30',
'C':'500,00',
'priceC':'500',
'':'',
'identity':'1',
'contact-name':'romario',
'email':'c4040401@trbvm.com',
'phone':'(31) 9518 6655',
'zip':'',
'state':'6842',
'region_ddd':'25',
'currentZipValue':'',
'city':'52491',
'neighborhood':'0',
'neighborhood_id':'0',
'neighborhood_name':'',
'countryStateCityCase':'1',
'usesAutoComplete':'',
'useNeighborhoodMultiSelector':'',
'streetaddress':'',
'addresslat':'',
'addresslng':'',
'':'',
'security_code':'undefined',
'captchaKey':'undefined}'
}

url1 = 'http://minasgerais.olx.com.br/ajax/posting_in_one_step_ajax.php'


with session() as c:
    c.post(url1, data=payload)

payload = {
'itemid':'774364153',
'sh':'48b0082f4a8c1b625ce27cc938a39f1b'
}

url1 = 'http://minasgerais.olx.com.br/ajax/posting_in_one_step_ajax.php'


with session() as c:
    c.post(url1, data=payload)

#soup = BeautifulSoup.BeautifulSoup(html)

#divList = soup(attrs={'class': 'access_url'})
#prices = soup(attrs={'class': 'price'})

