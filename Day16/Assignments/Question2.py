from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Step 1: Open browser
driver = webdriver.Chrome()
driver.maximize_window()

# Step 2: Navigate to example.com
driver.get("https://example.com")
print("Page Title:", driver.title)
time.sleep(2)

# Step 3: Navigate to another page on the same site
driver.get("https://www.iana.org/domains/example")
print("Page Title:", driver.title)
time.sleep(2)

# Step 4: Navigate back
driver.back()
print("Page Title after Back:", driver.title)
time.sleep(2)

# Step 5: Navigate forward
driver.forward()
print("Page Title after Forward:", driver.title)
time.sleep(2)

# Step 6: Refresh the page
driver.refresh()
print("Page Title after Refresh:", driver.title)
time.sleep(2)

# Step 7: Close browser
driver.quit()
