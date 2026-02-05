from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Launch browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open alerts page
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
time.sleep(2)

# -----------------------------
# 1. Trigger JavaScript alert
# -----------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
time.sleep(1)

# Switch to alert and print message
alert = driver.switch_to.alert
print("Alert message:", alert.text)

# 2. Accept the alert
alert.accept()
time.sleep(1)

# -----------------------------
# 3. Dismiss confirmation pop-up
# -----------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
time.sleep(1)

confirm_alert = driver.switch_to.alert
print("Confirm message:", confirm_alert.text)

# Dismiss (Cancel)
confirm_alert.dismiss()
time.sleep(1)

# -----------------------------
# 4. Enter text in prompt alert
# -----------------------------
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
time.sleep(1)

prompt_alert = driver.switch_to.alert
print("Prompt message:", prompt_alert.text)

prompt_alert.send_keys("Selenium Test")
prompt_alert.accept()
time.sleep(1)

# -----------------------------
# 5. Verify result displayed
# -----------------------------
result = driver.find_element(By.ID, "result").text
print("Result text on page:", result)

assert "Selenium Test" in result

# Close browser
driver.quit()
