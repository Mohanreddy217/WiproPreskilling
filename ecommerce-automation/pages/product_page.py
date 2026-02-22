from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProductPage(BasePage):

    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[data-test='add-to-cart']")
    CART_BADGE = (By.CSS_SELECTOR, "span[data-test='cart-quantity']")

    def add_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.ADD_TO_CART_BUTTON)
        ).click()

    def is_product_added(self):
        badge = self.wait.until(
            EC.visibility_of_element_located(self.CART_BADGE)
        )
        return int(badge.text) > 0
