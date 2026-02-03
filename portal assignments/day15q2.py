import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestTC003():

    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)

    def teardown_method(self, method):
        self.driver.quit()

    def test_tC003(self):
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

        # Username
        self.wait.until(EC.visibility_of_element_located((By.NAME, "username"))).send_keys("Admin")

        # Password
        self.wait.until(EC.visibility_of_element_located((By.NAME, "password"))).send_keys("admin123")

        # Login button
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

        # User dropdown
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".oxd-userdropdown-name"))).click()

        # Logout
        self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Logout"))).click()