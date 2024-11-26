from utils.locators import *
from selenium.webdriver.common.by import By

def test_redirection_footer_links(home_page):
    locator = HomePageLocators
    home_page.verify_on_homepage()

    home_page.redirect_to_page(By.XPATH, locator.FOOTER_ABOUT_SELECTOR, 'https://ict-strypes.eu/about-strypes/', 'About ICT Strypes')
    home_page.redirect_to_page(By.XPATH, locator.FOOTER_RESOURCES_SELECTOR, 'https://ict-strypes.eu/resources/', 'Resources')
    home_page.redirect_to_page(By.XPATH, locator.FOOTER_SERVICES_SELECTOR, 'https://ict-strypes.eu/services/', 'Our smart services that create business impact')
    home_page.redirect_to_page(By.XPATH, locator.FOOTER_CAREERS_SELECTOR, 'https://ict-strypes.eu/careers/', 'Our awesome team')
    home_page.redirect_to_page(By.XPATH, locator.FOOTER_CONTACT_SELECTOR, 'https://ict-strypes.eu/contact/', 'Get in touch')
    home_page.redirect_to_page(By.XPATH, locator.FOOTER_HOME_SELECTOR, 'https://ict-strypes.eu/', 'We are ICT Strypes')
