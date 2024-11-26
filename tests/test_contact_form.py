import time
from utils.locators import *
from selenium.webdriver.common.by import By

def test_contact_form_empty_fields(contact_page):
    locator = ContactPageLocators
    contact_page.verify_on_contact_page()

    contact_page.submit_empty_contact_form()

    contact_page.input_correct_email()
    contact_page.click(By.XPATH, locator.AGREE_CHECKBOX_SELECTOR)
    contact_page.verify_warning_message_cleared(By.XPATH, locator.AGREE_WARNING_SELECTOR)
    contact_page.verify_warning_message_cleared(By.XPATH, locator.GENERAL_WARNING_SELECTOR)

def test_contact_form_wrong_email(contact_page):
    locator = ContactPageLocators

    contact_page.verify_on_contact_page()
    contact_page.submit_contact_form_with_wrong_email_credentials()
    contact_page.input_correct_email()


