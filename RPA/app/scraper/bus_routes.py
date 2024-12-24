# app/scraper/bus_routes.py
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class BusRoutesScraper:
    def __init__(self, start_text: str, destination_text: str):
        self.start_text = start_text
        self.destination_text = destination_text
        self._driver: webdriver.Chrome | None = None

    @staticmethod
    def setup_driver() -> webdriver.Chrome:
        return webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    @staticmethod
    def type_with_delay(element, text):
        for character in text:
            element.send_keys(character)
            time.sleep(0.3)

    def open_page(self, url):
        self._driver.get(url)

    def accept_cookies(self):
        accept_button = WebDriverWait(self._driver, 3).until(
            EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
        )
        accept_button.click()
        time.sleep(3)

    def click_location_result(self):
        time.sleep(2)
        location_result = WebDriverWait(self._driver, 3).until(
            EC.element_to_be_clickable((By.ID, "location_0"))
        )
        location_result.click()

    def enter_text(self):
        text_field_start = WebDriverWait(self._driver, 3).until(
            EC.presence_of_element_located((By.ID, "position_start"))
        )
        self.type_with_delay(text_field_start, self.start_text)
        self.click_location_result()
        text_field_destination = WebDriverWait(self._driver, 3).until(
            EC.presence_of_element_located((By.ID, "position_end"))
        )
        self.type_with_delay(text_field_destination, self.destination_text)
        self.click_location_result()

    def click_search(self):
        search_button = WebDriverWait(self._driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "search-button"))
        )
        search_button.click()

    def click_inner_element(self):
        minimize_button = WebDriverWait(self._driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "minimize-btn"))
        )
        minimize_button.click()
        agency_span = WebDriverWait(self._driver, 3).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "agency"))
        )
        agency_span.click()
        time.sleep(3)

    def click_result(self) -> list[str]:
        try:
            WebDriverWait(self._driver, 3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "div.content.ng-star-inserted"))
            )
            elements = self._driver.find_elements(By.CSS_SELECTOR, "div.content.ng-star-inserted span")
            lines = [element.text for element in elements if
                     element.get_attribute("class") in ["type ng-star-inserted", "step-title ng-star-inserted",
                                                        "title ng-star-inserted", "text"]]
            return lines
        except Exception as e:
            print("Elemento não encontrado:", e)

    def run(self) -> list[str]:
        self._driver = self.setup_driver()
        try:
            self.open_page("https://moovitapp.com/index/pt-br/transporte_público-Curitiba-942")
            self.accept_cookies()
            self.click_search()
            self.enter_text()
            self.click_inner_element()
            return self.click_result()
        except Exception as e:
            print(e)
        finally:
            self._driver.quit()