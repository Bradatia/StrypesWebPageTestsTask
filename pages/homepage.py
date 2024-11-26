from utils.locators import *
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def verify_on_homepage(self):
        locator = HomePageLocators

        self.verify_current_page_url(locator.URL)
        self.verify_page_heading('h1', "We are ICT Strypes")
        self.verify_page_heading('h2', "Our Services")

    def search_for_item(self, selector, search_query):
        search_input = self.find_element(By.ID, selector)
        search_input.send_keys(search_query)
        search_input.submit()

    def get_search_results(self, selector):
        return self.find_elements(By.CSS_SELECTOR, selector)

    def get_search_popup_id_selector(self, selector):
        self.wait_for_element(By.XPATH, selector)
        search_element = self.find_element(By.XPATH, selector)
        return self.get_element_attribute(search_element, 'id')

    def open_search_popup(self):
        locator = HomePageLocators

        self.click(By.XPATH, locator.SEARCH_BUTTON_SELECTOR)
        return self.get_search_popup_id_selector(locator.SEARCH_POPUP_SELECTOR)

    def return_results(self, selector):
        results = self.get_search_results(selector)
        assert len(results) > 0, "No search results found"
        return results

    def search_for_item_and_return_results(self, search_query):
        locator = HomePageLocators

        search_pop_up_id_selector = self.open_search_popup()
        self.search_for_item(search_pop_up_id_selector, search_query)
        self.wait_for_element(By.CSS_SELECTOR, locator.SEARCH_RESULT_SELECTOR)
        return self.return_results(locator.SEARCH_ARTICLE_SELECTOR)
