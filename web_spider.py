from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import time

options = Options()
options.headless = True
pwd = os.getcwd()

url=raw_input("Enter the URL: ")
pwd=pwd+'/geckodriver'

print("Please wait till I spy on the website...")

driver = webdriver.Firefox(options=options, executable_path=pwd)

driver.get("https://lookup.icann.org/lookup")

	


driver.find_element_by_xpath("//*[@id='input-domain']").send_keys(url)

driver.find_element_by_xpath("//*[@id='domain-form']/div/button").click()
time.sleep(5)
a = driver.find_element_by_xpath("/html/body/rwc-root/div/rwc-lookup-response/div[3]/div[1]/div/div").text

#a = driver.find_element_by_xpath("/html/body/rwc-root/div/rwc-lookup-response/div[3]/div[1]/div/div/rwc-lookup-domain-information/div/div/ul[1]/li[4]/p[1]").text
print("------------------------------------------------------------------")
print(a)
print("------------------------------------------------------------------")
print("There u go!!!  :)")