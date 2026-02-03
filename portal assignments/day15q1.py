from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Create a WebDriver instance (Chrome)
driver = webdriver.Chrome()

# 1. Navigate to the website
driver.get("https://example.com")

# 2. Print the page title and URL
print("Page Title:", driver.title)
print("Current URL:", driver.current_url)

# 3. Close the browser
driver.quit()
