
import pytest
from utilities.driver_factory import get_driver
import os
from datetime import datetime

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Capture screenshot only when test fails
    if report.when == "call" and report.failed:

        driver = item.funcargs.get("setup", None)

        if driver:
            # Create screenshots folder if not exists
            if not os.path.exists("screenshots"):
                os.makedirs("screenshots")

            file_name = f"screenshots/{item.name}.png"

            driver.save_screenshot(file_name)

            print(f"\n📸 Screenshot saved: {file_name}")



def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run tests: chrome, firefox, edge"
    )


@pytest.fixture
def setup(request):
    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    yield driver
    driver.quit()

def pytest_configure(config):
    # Create reports folder if not exists
    if not os.path.exists("reports"):
        os.makedirs("reports")

    # Generate timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    # Set report file path
    report_file = f"reports/report_{timestamp}.html"

    # Automatically add html report option
    config.option.htmlpath = report_file
    config.option.self_contained_html = True

