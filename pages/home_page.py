from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.from_field = (By.XPATH, "//div[@class='box location from']//span[text()='From']")
        self.to_field = (By.XPATH, "//input[@placeholder='Type to search']")
        self.search_button = (By.XPATH, "//button[contains(@class, 'search-btn')]")

    def click_from_field(self):
        self.click_element(self.from_field)

    def type_in_to_field(self, text):
        self.send_keys_to_element(self.to_field, text)

    def click_search_button(self):
        self.click_element(self.search_button)
