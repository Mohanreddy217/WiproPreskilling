from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class RegisterPage(BasePage):

    ACCOUNT_ICON = (By.CSS_SELECTOR, "a[data-test='nav-sign-in']")
    REGISTER_LINK = (By.XPATH, "//a[contains(text(),'Register')]")

    FIRSTNAME = (By.ID, "first_name")
    LASTNAME = (By.ID, "last_name")
    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    DOB = (By.ID, "dob")
    STREET = (By.ID, "street")
    POSTCODE = (By.ID, "postal_code")
    CITY = (By.ID, "city")
    STATE = (By.ID, "state")
    COUNTRY = (By.ID, "country")
    PHONE = (By.ID, "phone")

    REGISTER_BTN = (By.CSS_SELECTOR, "button[type='submit']")

    def open(self):

    # Go to homepage first
        self.driver.get("https://practicesoftwaretesting.com/")

    # Wait for page to fully load
        self.wait.until(
            EC.visibility_of_element_located(self.ACCOUNT_ICON)
        )

    # Click account icon
        self.click(self.ACCOUNT_ICON)

    # Wait for register link to appear
        self.wait.until(
            EC.visibility_of_element_located(self.REGISTER_LINK)
        )

    # Click register
        self.click(self.REGISTER_LINK)

    # Wait for register form to load
        self.wait.until(
            EC.url_contains("register")
        )

        print("✔ Register Page Opened")


    def register(self, data):

        self.send_keys(self.FIRSTNAME, data["first_name"])
        self.send_keys(self.LASTNAME, data["last_name"])
        self.send_keys(self.EMAIL, data["email"])
        self.send_keys(self.PASSWORD, data["password"])
        self.send_keys(self.DOB, data["dob"])
        self.send_keys(self.STREET, data["street"])
        self.send_keys(self.POSTCODE, data["postcode"])
        self.send_keys(self.CITY, data["city"])
        self.send_keys(self.STATE, data["state"])

    # Select country
        country_dropdown = Select(
            self.wait.until(EC.element_to_be_clickable(self.COUNTRY))
        )
        country_dropdown.select_by_visible_text(data["country"])

        self.send_keys(self.PHONE, data["phone"])

    # Click register button
        register_button = self.wait.until(
            EC.element_to_be_clickable(self.REGISTER_BTN)
        )

        self.driver.execute_script("arguments[0].scrollIntoView(true);", register_button)
        register_button.click()

        print("✔ Register button clicked")

    # ✅ CORRECT WAIT — wait for URL change
        self.wait.until(EC.url_contains("login"))

        print("✔ Redirected to Login page")
