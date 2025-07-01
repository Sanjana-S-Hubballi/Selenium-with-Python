import pytest
from selenium import webdriver
import os

@pytest.fixture
def driver():
    # ✅ Launch Chrome
    driver = webdriver.Chrome()   # Make sure chromedriver is in PATH
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Take screenshot on failure — same logic as your Playwright version.
    """
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if driver:
            # Make sure screenshots folder exists
            os.makedirs("screenshots", exist_ok=True)
            screenshot_path = f"screenshots/{item.name}.png"
            driver.save_screenshot(screenshot_path)
            print(f"\n[Selenium] Screenshot saved to: {screenshot_path}")