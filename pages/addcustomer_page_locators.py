from selenium.webdriver.common.by import By


class AddCustomerLocators:
    BACKGROUND_RADIO_BUTTON = (By.XPATH, "//*[@id='main']/div/form/div/div[1]/label")
    NAME_TEXT_BOX = (By.ID, 'fname')
    LASTNAME_TEXT_BOX = (By.ID, "lname")
    EMAIL_TEXT_BOX = (By.ID, "email")
    ADDRESS_TEXT_BOX = (By.XPATH, "//textarea[@id='message']")
    TELEPHONE_TEXT_BOX = (By.ID, "telephoneno")
    SUBMIT_BUTTON = (By.NAME, "submit")
