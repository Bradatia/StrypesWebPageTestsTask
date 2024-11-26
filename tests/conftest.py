import pytest
from drivers.webdriver_config import get_driver
from pages.homepage import HomePage
from pages.contact_page import ContactPage
from utils.locators import *

# Fixture to set up and tear down the driver
@pytest.fixture(scope="function")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

# Fixtures for the page objects
@pytest.fixture
def home_page(driver):
    locator = HomePageLocators
    driver.get(locator.URL)
    return HomePage(driver)

@pytest.fixture
def contact_page(driver):
    locator = ContactPageLocators
    driver.get(locator.URL)
    return ContactPage(driver)
