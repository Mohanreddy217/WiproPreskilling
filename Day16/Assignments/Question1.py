from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Step 1: Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Open REAL test page
driver.get("https://the-internet.herokuapp.com/login")

# Step 3: Wait
wait = WebDriverWait(driver, 10)

# ID locator
username = wait.until(EC.presence_of_element_located((By.ID, "username")))

# Name locator
password = driver.find_element(By.NAME, "password")

# Class Name locator
submit_btn = driver.find_element(By.CLASS_NAME, "radius")

# Enter text
username.send_keys("tomsmith")
password.send_keys("SuperSecretPassword!")

# Click submit
submit_btn.click()

# Step 4: Validate message using XPath
message_xpath = wait.until(
    EC.presence_of_element_located((By.XPATH, "//div[@id='flash']"))
)

# CSS Selector locator (same message)
message_css = driver.find_element(By.CSS_SELECTOR, "#flash")

expected_text = "You logged into a secure area!"
actual_text = message_xpath.text

assert expected_text in actual_text, "Test Failed: Message not matched"

print("✅ Test Passed: Validation successful")

time.sleep(2)

# Step 5: Close browser
driver.quit()
