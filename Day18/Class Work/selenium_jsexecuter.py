from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Edge()
driver.get("https://amazon.in")
driver.maximize_window()
time.sleep(2)

#* --> this is javascript alert message

# driver.execute_script("alert('Hello amazon')")

#* this is js scroll 
#! full window scroll

# driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

#! upto window scroll via length

driver.execute_script("window.scrollBy(0,450)")
time.sleep(2)