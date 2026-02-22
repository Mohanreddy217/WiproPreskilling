


from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class SearchPage(BasePage):

    SEARCH_BOX = (By.CSS_SELECTOR, "input[data-test='search-query']")
    SEARCH_BUTTON = (By.CSS_SELECTOR, "button[data-test='search-submit']")
    PRODUCT_CARD = (By.CSS_SELECTOR, "a.card")

    def search_product(self, product_name):
        # Wait until search box visible
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX)).clear()
        self.slow(1)
        self.wait.until(EC.visibility_of_element_located(self.SEARCH_BOX)).send_keys(product_name)
        self.slow(2)

        # Click search button
        self.wait.until(EC.element_to_be_clickable(self.SEARCH_BUTTON)).click()
        self.slow(8)

    def is_results_displayed(self):
        results = self.wait.until(EC.presence_of_all_elements_located(self.PRODUCT_CARD))
        return len(results) > 0


    FIRST_PRODUCT = (By.CSS_SELECTOR, "a.card")

    def open_first_product(self):
        self.wait.until(
            EC.presence_of_all_elements_located(self.FIRST_PRODUCT)
        )
        products = self.driver.find_elements(*self.FIRST_PRODUCT)
        products[0].click()


