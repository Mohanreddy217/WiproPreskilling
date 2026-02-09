from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://letcode.in/frame")

driver.switch_to.frame(0)

driver.find_element(By.NAME, "fname").send_keys("saiprakash")
driver.find_element(By.NAME, "lname").send_keys("reddy")

driver.quit()