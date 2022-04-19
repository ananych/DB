#%%
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pandas as pd
from tqdm import tqdm
import csv
chrome = webdriver.Chrome('./chromedriver')
chrome.get("https://rent.591.com.tw/?region=1")

time.sleep(2)
name_to=[]
tek_to=[]
typ_to=[]
typ2_to=[]
rule_to=[]



for j in tqdm(range(400)):
    for i in tqdm(range(30)):
        chrome.switch_to.window(chrome.window_handles[0])
        while len(chrome.find_elements(By.CLASS_NAME,'vue-list-rent-item'))<1:
            b = 0



        a=chrome.find_elements(By.CLASS_NAME,'vue-list-rent-item')[i]
        a.click()

        b=0
        chrome.switch_to.window(chrome.window_handles[1])
        while len(chrome.find_elements(By.CLASS_NAME,'name'))<1:
            time.sleep(2)
            b=b+1
            if b==3:
                b = 0
                chrome.refresh()

        names = chrome.find_elements(By.CLASS_NAME,'name')
        name=names[-1].text
        # print(name)
        # print(j*30+i+1)
        name_to.append(name)

        tels = chrome.find_elements(By.CLASS_NAME,'tel-txt')
        tel=tels[-1].text
        # print(tel)
        tek_to.append(tel)
        
        # typs = chrome.find_elements(By.CLASS_NAME,'house-pattern')
        # typ=typs[0].text
        typ=chrome.find_elements_by_xpath('//*[@id="houseInfo"]/div[3]/span[1]')[0].text
        # print(typ)
        typ_to.append(typ)
        

        typ2=chrome.find_elements_by_xpath('//*[@id="houseInfo"]/div[3]/span[7]')[0].text
        # print(typ)
        typ2_to.append(typ2)


        rules = chrome.find_elements(By.CLASS_NAME,'service-rule')
        if len(rules)==0:
            rule='no'
            # print(rule)
        else:
            rule=rules[0].text
            # print(rule)
        rule_to.append(rule)
        
        chrome.close()




    chrome.switch_to.window(chrome.window_handles[0])
    chrome.find_elements(By.CLASS_NAME,'pageNext')[0].click()
name_to=pd.DataFrame(name_to)
tek_to=pd.DataFrame(tek_to)
typ_to=pd.DataFrame(typ_to)
typ2_to=pd.DataFrame(typ2_to)
rule_to=pd.DataFrame(rule_to)

name_to.to_csv('tp_name_to.csv')
tek_to.to_csv('tp_tek_to.csv')
typ_to.to_csv('tp_typ_to.csv')
typ2_to.to_csv('tp_typ2_to.csv')
rule_to.to_csv('tp_rule_to.csv')

# chrome.switch_to.window(chrome.window_handles[0])
# a=chrome.find_elements(By.CLASS_NAME,'vue-list-rent-item')[1]
# a.click()
# chrome.switch_to.window(chrome.window_handles[1])
# while len(chrome.find_elements(By.CLASS_NAME,'name'))<1:
#     a=0
# names = chrome.find_elements(By.CLASS_NAME,'name')
# name=names[-1].text
# print(name)

# tels = chrome.find_elements(By.CLASS_NAME,'tel-txt')
# tel=tels[-1].text
# print(tel)

# typs = chrome.find_elements(By.CLASS_NAME,'house-pattern')
# typ=typs[0].text
# print(typ)

# rules = chrome.find_elements(By.CLASS_NAME,'service-rule')
# rule=rules[0].text
# print(rule)

# chrome.close()