from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    EMAIL = (By.ID, "email")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[data-test='login-submit']")
    ACCOUNT_ICON = (By.CSS_SELECTOR, "a[data-test='nav-account']")
    LOGOUT_BUTTON = (By.XPATH, "//a[contains(text(),'Logout')]")

    def login(self, email, password):

        # Wait until login form appears
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "form[data-test='login-form']"))
        )

        # Fill email
        email_field = self.wait.until(
            EC.visibility_of_element_located(self.EMAIL)
        )
        email_field.clear()
        email_field.send_keys(email)

        # Fill password
        password_field = self.wait.until(
            EC.visibility_of_element_located(self.PASSWORD)
        )
        password_field.clear()
        password_field.send_keys(password)

        # Click login button
        login_btn = self.wait.until(
            EC.element_to_be_clickable(self.LOGIN_BUTTON)
        )
        login_btn.click()

        # Wait until redirected to account page
        self.wait.until(
            EC.url_contains("account")
        )

        print("✔ Login Successful")




    def is_login_successful(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.ACCOUNT_ICON)
            ).is_displayed()
        except:
            return False

    # def logout(self):

    # # Click account dropdown (Mohan Nelamala)
    #     account_icon = self.wait.until(
    #         EC.element_to_be_clickable((By.ID, "menu"))
    #     )
    #     account_icon.click()

    # # Click Sign Out
    #     sign_out = self.wait.until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='nav-sign-out']"))
    #     )
    #     sign_out.click()

    # # Wait for login page
    #     self.wait.until(
    #         EC.url_contains("login")
    #     )

    #     print("✔ Logout Successful")

    # 
    
    def logout(self):

    # Wait for any toast notification to disappear
        self.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ngx-toastr"))
        )
        self.slow(1)

    # Click account dropdown
        account_icon = self.wait.until(
            EC.element_to_be_clickable((By.ID, "menu"))
        )
        account_icon.click()
        self.slow(1)

    # Click Sign out
        sign_out = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='nav-sign-out']"))
        )
        sign_out.click()
        self.slow(1)

    # Wait until Sign in button appears (logout confirmation)
        self.wait.until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a[data-test='nav-sign-in']"))
        )

        print("✔ Logout Successful")

