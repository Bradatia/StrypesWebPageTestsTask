from utils.locators import *
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ContactPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_expected_text_value(self, by, selector, expected_value):
        found_value = self.get_text(by, selector)
        assert found_value == expected_value, f"Expected email '{expected_value}',  got '{found_value}'"

    def verify_on_contact_page(self):
        locator = ContactPageLocators

        self.verify_current_page_url(locator.URL)
        self.verify_page_heading('h1', "Get in touch")
        self.verify_expected_text_value(By.XPATH, locator.CONTACT_EMAIL_SELECTOR, locator.CONTACT_EMAIL)

    def verify_empty_form_warning_messages(self):
        locator = ContactPageLocators
        self.wait_for_element(By.XPATH, locator.MAIL_WARNING_SELECTOR)
        self.verify_expected_text_value(By.XPATH, locator.MAIL_WARNING_SELECTOR, 'Please complete this required field.')
        self.wait_for_element(By.XPATH, locator.AGREE_WARNING_SELECTOR)
        self.verify_expected_text_value(By.XPATH, locator.AGREE_WARNING_SELECTOR, 'Please complete this required field.')
        self.wait_for_element(By.XPATH, locator.GENERAL_WARNING_SELECTOR)
        self.verify_expected_text_value(By.XPATH, locator.GENERAL_WARNING_SELECTOR,'Please complete all required fields.')

    def verify_warning_message_cleared(self, by, selector):
        self.wait_element_not_visible(by, selector)

    def submit_empty_contact_form(self):
        locator = ContactPageLocators

        self.wait_for_element(By.XPATH, locator.SEND_BUTTON_SELECTOR)
        self.click(By.XPATH, locator.SEND_BUTTON_SELECTOR)
        self.verify_empty_form_warning_messages()

    def submit_wrong_format_email(self):
        locator = ContactPageLocators

        self.input_text(By.NAME, 'email', 'message')
        # self.click(By.XPATH, locator.SEND_BUTTON_SELECTOR)
        self.wait_for_element(By.XPATH, locator.MAIL_WARNING_SELECTOR)
        self.verify_expected_text_value(By.XPATH, locator.MAIL_WARNING_SELECTOR, 'Email must be formatted correctly.')

    def submit_not_valid_email(self):
        locator = ContactPageLocators

        self.input_text(By.NAME, 'email', 'test@example.com')
        self.wait_for_element(By.XPATH, locator.MAIL_WARNING_SELECTOR)
        self.verify_expected_text_value(By.XPATH, locator.MAIL_WARNING_SELECTOR, 'Please enter a valid email address.')

    def input_correct_email(self):
        locator = ContactPageLocators

        self.input_text(By.NAME, 'email', 'bradatia@gmail.com')
        self.verify_warning_message_cleared(By.XPATH, locator.MAIL_WARNING_SELECTOR)

    def submit_contact_form_with_wrong_email_credentials(self):
        self.submit_wrong_format_email()
        self.submit_not_valid_email()


