

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from selenium.webdriver.common.keys import Keys



class CartPage(BasePage):

    CART_ICON = (By.CSS_SELECTOR, "a[data-test='nav-cart']")
    QUANTITY_INPUT = (By.CSS_SELECTOR, "input[type='number']")
    REMOVE_BUTTON = (By.CSS_SELECTOR, "a.btn.btn-danger")
    EMPTY_CART_MESSAGE = (By.XPATH, "//p[contains(text(),'empty')]")

    
    # def open_cart(self):

    # # Wait for toast message to disappear (VERY IMPORTANT)
    #     self.wait.until(
    #         EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ngx-toastr"))
    #     )

    # # Now click cart icon
    #     cart_icon = self.wait.until(
    #         EC.element_to_be_clickable((By.CSS_SELECTOR, "a[data-test='nav-cart']"))
    #     )

    #     cart_icon.click()

    # # Wait until cart page loads
    #     self.wait.until(
    #         EC.url_contains("checkout")
    #     )

    #     self.wait.until(
    #         EC.visibility_of_element_located(self.QUANTITY_INPUT)
    #     )

    #     print("✔ Cart Page Fully Loaded")



    def open_cart(self):

    # Wait until toast disappears (IMPORTANT)
        self.wait.until(
            EC.invisibility_of_element_located((By.CSS_SELECTOR, ".ngx-toastr"))
        )

    # Wait for cart icon presence
        cart_icon = self.wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-test='nav-cart']"))
        )

    # Scroll to it
        self.driver.execute_script("arguments[0].scrollIntoView(true);", cart_icon)

    # Click using JS (avoids overlay issue)
        self.driver.execute_script("arguments[0].click();", cart_icon)

    # Wait for cart page
        self.wait.until(
            EC.url_contains("checkout")
        )

        print("✔ Cart Opened Successfully")


    


    def update_quantity(self, qty):

    # Wait until quantity input is visible
        qty_input = self.wait.until(
            EC.visibility_of_element_located(self.QUANTITY_INPUT)
        )

    # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", qty_input)

    # Small wait for UI stability
        self.wait.until(
            EC.element_to_be_clickable(self.QUANTITY_INPUT)
        )

        qty_input.clear()
        qty_input.send_keys(str(qty))

        print("✔ Quantity Updated")




    def remove_product(self):
        remove_btn = self.wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "a.btn.btn-danger"))
        )
        remove_btn.click()

    # Wait until cart becomes empty
        self.wait.until(
            EC.invisibility_of_element(remove_btn)
        )




    def is_cart_empty(self):
        try:
            self.wait.until(
                EC.visibility_of_element_located(self.EMPTY_CART_MESSAGE)
            )
            return True
        except:
            return False
