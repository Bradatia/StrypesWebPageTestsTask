from utils.locators import *
from selenium.webdriver.common.by import By

def test_services_dropdown_menu_and_submenu(home_page):
    locator = HomePageLocators
    home_page.verify_on_homepage()

    home_page.select_dropdown_menu(By.XPATH, locator.SERVICES_SELECTOR)
    home_page.select_dropdown_menu(By.XPATH, locator.DEVOPS_SELECTOR)
    home_page.select_last_dropdown_menu(By.XPATH, locator.CYBERSECURITY_SELECTOR)




