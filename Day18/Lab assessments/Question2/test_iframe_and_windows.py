import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# =========================
# SETUP DRIVER
# =========================
driver = webdriver.Chrome()
driver.maximize_window()

# =========================
# 1. OPEN PAGE WITH IFRAME
# =========================
driver.get("https://the-internet.herokuapp.com/iframe")

# =========================
# 2. SWITCH TO IFRAME & ENTER TEXT
# =========================
driver.switch_to.frame("mce_0_ifr")

text_box = driver.find_element(By.ID, "tinymce")
text_box.clear()
text_box.send_keys("Hello from inside the iframe!")

print("Text entered inside iframe")

# =========================
# 3. SWITCH BACK TO MAIN CONTENT
# =========================
driver.switch_to.default_content()
print("Switched back to main page")

# =========================
# 4. OPEN A NEW WINDOW/TAB
# =========================
driver.execute_script("window.open('https://example.com');")

# =========================
# 5. SWITCH BETWEEN WINDOWS & PRINT TITLES
# =========================
window_handles = driver.window_handles
parent_window = driver.current_window_handle

for window in window_handles:
    driver.switch_to.window(window)
    print("Window Title:", driver.title)
    time.sleep(1)

# =========================
# 6. CLOSE CHILD WINDOW & RETURN TO PARENT
# =========================
for window in window_handles:
    if window != parent_window:
        driver.switch_to.window(window)
        driver.close()
        print("Child window closed")

driver.switch_to.window(parent_window)
print("Returned to parent window:", driver.title)

# =========================
# CLEANUP
# =========================
time.sleep(2)
driver.quit()
