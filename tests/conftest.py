import pytest as pytest
from selenium import webdriver

@pytest.fixture(scope="module")
def driver():
    _driver = webdriver.Chrome()
    yield _driver
    _driver.quit()


@pytest.fixture(scope="function")
def customer_data():
    first_name = "John"
    last_name = "Smith"
    email = "johnsmith@example.com"
    address = "23 Bell street Toronto M3L7B4 Ontario Canada"
    telephone_num = "1234567890"
    return [first_name, last_name, email, address, telephone_num]


