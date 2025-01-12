from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.from_input = (By.XPATH, "//div[contains(@class, 'location from')]//input[@placeholder='Type to search']")
        self.from_option = (By.XPATH, "//div[contains(text(), 'Chittagong, Bangladesh')]")
        self.to_input = (By.XPATH, "//div[contains(@class, 'location to')]//input[@placeholder='Type to search']")
        self.to_option = (By.XPATH, "//div[contains(text(), 'Dhaka, Bangladesh')]")
        self.traveler_field = (By.XPATH, "//div[@class='box traveler']")
        self.increase_adults = (By.XPATH, "//div[contains(@class, 'adults')]//button[contains(@class, 'btn-link')]/i[contains(@class, 'icon-plus-circle')]/..")
        self.increase_children = (By.XPATH, "//div[contains(@class, 'children')]//button[contains(@class, 'btn-link')]/i[contains(@class, 'icon-plus-circle')]/..")
        self.done_button = (By.XPATH, "//button[contains(@class, 'picker-mb-btn')]")

    def type_in_from_field(self, text):
        self.send_keys_to_element(self.from_input, text)

    def select_from_option(self):
        self.click_element(self.from_option)

    def type_in_to_field(self, text):
        self.send_keys_to_element(self.to_input, text)

    def select_to_option(self):
        self.click_element(self.to_option)

    def click_traveler_field(self):
        self.click_element(self.traveler_field)

    def increase_adults_count(self):
        self.click_element(self.increase_adults)

    def increase_children_count(self):
        self.click_element(self.increase_children)

    def click_done_button(self):
        self.click_element(self.done_button)
