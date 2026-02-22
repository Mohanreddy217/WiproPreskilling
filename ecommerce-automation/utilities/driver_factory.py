# import configparser
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.firefox.service import Service as FirefoxService
# from webdriver_manager.chrome import ChromeDriverManager
# from webdriver_manager.firefox import GeckoDriverManager
# from selenium.webdriver.edge.service import Service as EdgeService
# from webdriver_manager.microsoft import EdgeChromiumDriverManager



# def get_driver(browser):

#     browser = browser.lower()

#     if browser == "chrome":
#         driver = webdriver.Chrome()

#     elif browser == "firefox":
#         driver = webdriver.Firefox()

#     elif browser == "edge":
#         driver = webdriver.Edge()

#     else:
#         raise ValueError("Browser not supported")

#     driver.maximize_window()
#     driver.implicitly_wait(5)

#     # 🔥 IMPORTANT ADD THIS
#     driver.get("https://practicesoftwaretesting.com/")

#     return driver
import configparser
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_driver(browser):

    browser = browser.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument("--start-maximized")

        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        from selenium.webdriver.firefox.service import Service as FirefoxService
        from webdriver_manager.firefox import GeckoDriverManager

        driver = webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install())
        )

    elif browser == "edge":
        from selenium.webdriver.edge.service import Service as EdgeService
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        driver = webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install())
        )

    else:
        raise ValueError("Browser not supported")

    driver.implicitly_wait(5)
    return driver
