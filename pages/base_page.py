from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def navigate_to(self, url):
        self.driver.get(url)

    def explicitly_wait_and_find_element(self, interval, locator_type_and_locator_tuple):
        return WebDriverWait(self.driver, interval).until(
            EC.element_to_be_clickable(locator_type_and_locator_tuple))

    def find_element(self, locator_type_and_locator_tuple):
        return self.driver.find_element(*locator_type_and_locator_tuple)

    def select_radio_btn(self, desiredValue, nameAttribute):
        radio_buttons = self.driver.find_elements(By.NAME, nameAttribute)
        for button in radio_buttons:
            if button.get_attribute("value")==desiredValue:
                button.click()
                break


