from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, by, selector):
        return self.driver.find_element(by, selector)

    def find_elements(self, by, selector):
        return self.driver.find_elements(by, selector)

    def wait_for_element(self, by, selector):
        return self.wait.until(EC.presence_of_element_located((by, selector)))

    def wait_for_element_to_be_clickable(self, by, selector):
        return self.wait.until(EC.element_to_be_clickable((by, selector)))

    def wait_element_not_visible(self, by, selector):
        return self.wait.until(EC.invisibility_of_element_located((by, selector)))

    def click(self, by, selector):
        self.find_element(by, selector).click()

    def input_text(self, by, selector, text):
        element = self.wait_for_element(by, selector)
        element.clear()
        element.send_keys(text)

    def get_page_heading(self, selector):
        return self.get_text(By.TAG_NAME, selector)

    def verify_page_heading(self, selector, expected_heading):
        heading = self.get_page_heading(selector)
        assert heading == expected_heading, f"Expected '{expected_heading}', but got '{heading}'"

    def get_text(self, by, selector):
        element = self.wait_for_element(by, selector)
        return element.text

    def get_element_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    def verify_aria_expanded_value(self, element, state):
        aria_expanded_value = self.get_element_attribute(element, "aria-expanded")
        assert aria_expanded_value == state, f"Expected value to be '{state}', but got '{aria_expanded_value}'"

    def move_to_element_and_click_it(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def select_dropdown_menu(self, by, selector):
        dropdown_element = self.find_element(by, selector)
        self.verify_aria_expanded_value(dropdown_element, 'false')

        self.wait_for_element(by, selector)
        self.move_to_element_and_click_it(dropdown_element)

        self.verify_aria_expanded_value(dropdown_element, 'true')

    def select_last_dropdown_menu(self, by, selector):
        dropdown_element = self.find_element(by, selector)
        href_value = self.get_element_attribute(dropdown_element, "href")
        self.wait_for_element(by, selector)
        self.move_to_element_and_click_it(dropdown_element)
        self.verify_current_page_url(href_value)

    def get_current_page_url(self):
        return self.driver.current_url

    def verify_current_page_url(self, expected_url):
        current_url = self.get_current_page_url()
        assert f"{expected_url}" in current_url, f"Expected to be redirected to the contact page, but got '{current_url}'"

    def redirect_to_page(self, by, selector, url, heading):
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        self.wait_for_element(by, selector)
        self.click(by, selector)
        self.verify_current_page_url(url)
        self.verify_page_heading('h1', heading)

