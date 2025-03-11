from pages.index_page import IndexPage
from pages.addcustomer_page import AddCustomerPage
from pages.access_page import AccessPage
from resources.constants import TEST_SITE_URL,ADD_SUCCESS_ACCESS_PAGE_TXT
from tests.conftest import customer_data


class TestAddCustomer:

    def test_add_customer_button(self,driver):
        index_page = IndexPage(driver)
        index_page.navigate_to(TEST_SITE_URL)
        index_page.wait_and_click_register_button()

    def test_customer_addition(self,driver, customer_data):
        add_customer_page = AddCustomerPage(driver)
        add_customer_page.wait_and_choose_background()
        add_customer_page.wait_and_type_name(customer_data)
        add_customer_page.type_lastname(customer_data)
        add_customer_page.type_email(customer_data)
        add_customer_page.type_address(customer_data)
        add_customer_page.type_telephone(customer_data)
        add_customer_page.click_submit_btn()

        access_page = AccessPage(driver)
        addition_customer_success_lbl = access_page.get_access_success_label()
        assert addition_customer_success_lbl.__contains__(ADD_SUCCESS_ACCESS_PAGE_TXT), "NEW CUSTOMER ADDITION FAILED"