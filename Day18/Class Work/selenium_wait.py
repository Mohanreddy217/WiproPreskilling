from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 

driver=webdriver.Edge()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
wait=WebDriverWait(driver,10)  #! this is explict wait - conditional synchronization
#driver.implicitly_wait(10)   #! this is implict wait -  conditional synchronization
# time.sleep(10)  #! this is unconditional Synchronization

findelement=wait.until(
    EC.visibility_of_element_located((By.NAME,"username"))
).send_keys("Admin")

driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.XPATH,'//button[@type="submit"]').click()