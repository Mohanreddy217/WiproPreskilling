from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

# =========================
# SETUP DRIVER
# =========================
driver = webdriver.Chrome()
driver.maximize_window()

# =========================
# 1. IMPLICIT WAIT
# =========================
driver.implicitly_wait(10)   # waits up to 10 seconds for elements
print("Implicit wait set to 10 seconds")

driver.get("https://the-internet.herokuapp.com/dynamic_controls")

# =========================
# 2. EXPLICIT WAIT (Element Clickable)
# =========================
enable_button = driver.find_element(By.XPATH, "//button[text()='Enable']")

explicit_wait = WebDriverWait(driver, 10)
explicit_wait.until(EC.element_to_be_clickable(enable_button))

print("Element is clickable (Explicit Wait)")
enable_button.click()

# =========================
# 3. FLUENT WAIT (Polling Interval)
# =========================
fluent_wait = WebDriverWait(
    driver,
    timeout=15,
    poll_frequency=2,              # polling every 2 seconds
    ignored_exceptions=[NoSuchElementException]
)

textbox = fluent_wait.until(
    EC.element_to_be_clickable((By.XPATH, "//input[@type='text']"))
)

print("Element available using Fluent Wait")
textbox.send_keys("Fluent wait successful")

# =========================
# CLEANUP
# =========================
time.sleep(2)
driver.quit()
