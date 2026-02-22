# import pytest
# import time
# from selenium.webdriver.common.by import By
# from utilities.driver_factory import get_driver
# from utilities.csv_reader import read_test_data
# from pages.register_page import RegisterPage
# from pages.login_page import LoginPage
# from pages.search_page import SearchPage
# from pages.product_page import ProductPage
# from pages.cart_page import CartPage







# test_data = read_test_data("data/test_data.csv")


# @pytest.fixture
# def setup():
#     driver = get_driver()
#     driver.get("https://practicesoftwaretesting.com/")
#     yield driver
#     driver.quit()


# @pytest.mark.parametrize("data", test_data)
# def test_registration_and_login(setup, data):

#     driver = setup

#     # ===== REGISTRATION =====
#     register = RegisterPage(driver)
#     register.open()

#     assert "register" in driver.current_url.lower()

#     # Generate unique email
#     unique_email = f"{data['first_name'].lower()}{int(time.time())}@testmail.com"
#     data["email"] = unique_email

#     register.register(data)

#     # Confirm redirected to login page
#     assert "login" in driver.current_url.lower()

#     # ===== LOGIN =====
#     login = LoginPage(driver)
#     login.login(data["email"], data["password"])

#     assert login.is_login_successful() is True

# # Navigate to homepage after login
#     driver.get("https://practicesoftwaretesting.com/")

#     time.sleep(2)

# # ===== SEARCH PRODUCT =====
#     search = SearchPage(driver)
#     search.search_product(data["search_product"])
#     assert search.is_results_displayed() is True
#     print("✔ Product Search - PASSED")

#     time.sleep(5)
#     # ===== ADD TO CART =====
#     search.open_first_product()

#     product = ProductPage(driver)
#     product.add_to_cart()

#     assert product.is_product_added() is True
#     print("✔ Add to Cart - PASSED")

#     time.sleep(5)


#     # ===== CART MANAGEMENT =====
#     cart = CartPage(driver)
#     cart.open_cart()

#     cart.update_quantity(2)
#     #print("✔ Quantity Updated")
#     print("Updated Quantity Text:",
#       driver.find_element(By.CSS_SELECTOR, "input[type='number']").get_attribute("value"))


#     time.sleep(2)

#     #driver.get("https://practicesoftwaretesting.com/checkout")
    

#     # print("CURRENT URL BEFORE REMOVE:", driver.current_url)

#     cart.remove_product()

#     assert cart.is_cart_empty() is True
#     print("✔ Cart Management - PASSED")

#     time.sleep(5)


#     # ===== LOGOUT =====
#     login.logout()

#     assert "login" in driver.current_url.lower()
#     print("✔ Logout - PASSED")


    



import pytest
import time
from selenium.webdriver.common.by import By
from utilities.driver_factory import get_driver
from utilities.csv_reader import read_test_data
from pages.register_page import RegisterPage
from pages.login_page import LoginPage
from pages.search_page import SearchPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage


test_data = read_test_data("data/test_data.csv")






@pytest.mark.parametrize("data", test_data)
def test_registration_and_login(setup, data):

    driver = setup

    # ================= REGISTRATION =================
    register = RegisterPage(driver)
    register.open()

    assert "register" in driver.current_url.lower(), "Register page did not open"

    unique_email = f"{data['first_name'].lower()}{int(time.time())}@testmail.com"
    data["email"] = unique_email

    register.register(data)

    assert "login" in driver.current_url.lower(), "Registration failed or no redirect to login"

    # ================= LOGIN =================
    login = LoginPage(driver)
    login.login(data["email"], data["password"])

    assert "account" in driver.current_url.lower(), "Login failed - not redirected to account page"
    print("✔ Login - PASSED")

    # ================= SEARCH PRODUCT =================
    driver.get("https://practicesoftwaretesting.com/")

    search = SearchPage(driver)
    search.search_product(data["search_product"])

    assert search.is_results_displayed(), "Search results not displayed"
    print("✔ Product Search - PASSED")

    # ================= ADD TO CART =================
    search.open_first_product()

    product = ProductPage(driver)
    product.add_to_cart()

    assert product.is_product_added(), "Product was not added to cart"
    print("✔ Add to Cart - PASSED")

    # ================= CART MANAGEMENT =================
    cart = CartPage(driver)
    cart.open_cart()

    assert "checkout" in driver.current_url.lower(), "Cart page did not open"


    cart.update_quantity(2)

    updated_qty = driver.find_element(By.CSS_SELECTOR, "input[type='number']").get_attribute("value")
    assert updated_qty == "2", "Quantity update failed"
    print("✔ Quantity Updated")

    cart.remove_product()

    assert cart.is_cart_empty(), "Cart is not empty after removing product"
    print("✔ Cart Management - PASSED")

    # ================= LOGOUT =================
    login.logout()

    assert "sign-in" in driver.page_source.lower(), "Logout failed"

    print("✔ Logout - PASSED")

    def pytest_addoption(parser):
        parser.addoption(
            "--browser",
            action="store",
            default="chrome",
            help="Browser to run tests"
        )

