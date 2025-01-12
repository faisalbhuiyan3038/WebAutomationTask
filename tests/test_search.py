import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utils.driver_factory import get_driver
import time

@pytest.fixture(scope="module")
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_search(driver):
    driver.get("https://www.google.com")
    # Wait for search box to be present and locate it
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    # Enter search term and submit
    search_box.send_keys("Gozayyan")
    search_box.submit()

    # Wait for search results and click first link
    first_result = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "div.g a"))
    )
    first_result.click()

    # Wait a few seconds to see the result
    time.sleep(5)

    home_page = HomePage(driver)
    home_page.click_from_field()

    search_page = SearchPage(driver)
    search_page.type_in_from_field("chitt")
    time.sleep(2)  # Wait for the suggestions to load
    search_page.select_from_option()

    search_page.type_in_to_field("dhaka")
    time.sleep(2)  # Wait for the suggestions to load
    search_page.select_to_option()

    search_page.click_traveler_field()
    search_page.increase_adults_count()
    search_page.increase_children_count()
    search_page.click_done_button()

    home_page.click_search_button()
