import pytest
from automation_framework.utils.driver_factory import get_driver
from automation_framework.pages.login_page import LoginPage
from automation_framework.config.config import BASE_URL, BROWSER


@pytest.fixture
def setup():
    driver = get_driver(BROWSER)
    driver.get(BASE_URL)
    yield driver
    driver.quit()

def test_invalid_login(setup):
    login_page = LoginPage(setup)
    login_page.login("wrong_user", "wrong_pass")

    error = login_page.get_error_message()
    print("Test Result: ", error)

    assert "Invalid credentials" in error
