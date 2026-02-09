from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def get_driver(browser="chrome"):
    if browser.lower() == "chrome":
        options = Options()
        options.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=options)
    else:
        raise ValueError("Browser not supported")

    return driver
