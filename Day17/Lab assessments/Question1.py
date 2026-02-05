from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.techlistic.com/p/selenium-practice-form.html")
time.sleep(2)

# Fill text boxes
driver.find_element(By.NAME, "firstname").send_keys("John")
driver.find_element(By.NAME, "lastname").send_keys("Doe")

# Select radio button
driver.find_element(By.ID, "sex-0").click()

# Select checkbox
driver.find_element(By.ID, "exp-2").click()

# Select profession checkbox
driver.find_element(By.ID, "profession-1").click()

# Select from dropdown
continent = driver.find_element(By.ID, "continents")
select = Select(continent)
select.select_by_visible_text("Asia")

time.sleep(2)
driver.quit()
