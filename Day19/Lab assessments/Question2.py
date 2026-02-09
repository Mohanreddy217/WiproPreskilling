from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions

# =========================
# SELENIUM GRID HUB URL
# =========================
GRID_URL = "http://localhost:4444/wd/hub"
TEST_URL = "https://example.com"
EXPECTED_TITLE = "Example Domain"

# =========================
# BROWSERS TO RUN
# =========================
browser_options = {
    "chrome": ChromeOptions(),
    "firefox": FirefoxOptions()
}

# =========================
# RUN TEST ON EACH BROWSER
# =========================
for browser_name, options in browser_options.items():
    print(f"\nStarting test on: {browser_name}")

    driver = webdriver.Remote(
        command_executor=GRID_URL,
        options=options
    )

    driver.get(TEST_URL)

    # Fetch browser & platform info
    caps = driver.capabilities
    print("Browser :", caps.get("browserName"))
    print("Platform:", caps.get("platformName"))

    # Verify title
    assert driver.title == EXPECTED_TITLE
    print("Page title verified successfully")

    driver.quit()
