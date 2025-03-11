from pages.base_page import BasePage
from pages.addcustomer_page_locators import AddCustomerLocators
from resources.constants import MAX_WAIT_INTERVAL
from tests.conftest import customer_data


class AddCustomerPage(BasePage):

    def wait_and_choose_background(self):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCustomerLocators.BACKGROUND_RADIO_BUTTON).click()
        #self.select_radio_btn("ACTIVE", "active")
        #self.explicitly_wait_and_find_element()

    def wait_and_type_name(self,customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL, AddCustomerLocators.NAME_TEXT_BOX).send_keys(
            customer_data[0])

    def type_lastname(self, customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,AddCustomerLocators.LASTNAME_TEXT_BOX).send_keys(
            customer_data[1])

    def type_email(self,customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,AddCustomerLocators.EMAIL_TEXT_BOX).send_keys(
            customer_data[2])

    def type_address(self,customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,AddCustomerLocators.ADDRESS_TEXT_BOX).send_keys(
            customer_data[3])

    def type_telephone(self,customer_data):
        self.explicitly_wait_and_find_element(MAX_WAIT_INTERVAL,AddCustomerLocators.TELEPHONE_TEXT_BOX).send_keys(
            customer_data[4])

    def click_submit_btn(self):
        self.find_element(AddCustomerLocators.SUBMIT_BUTTON).click()
