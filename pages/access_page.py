from pages.base_page import BasePage
from pages.access_page_locators import AccessPageLocators
from resources.constants import MAX_WAIT_INTERVAL


class AccessPage(BasePage):

    def get_access_success_label(self):
        lbl_access_success_txt = self.explicitly_wait_and_find_element(
            MAX_WAIT_INTERVAL, AccessPageLocators.ACCESS_SUCCESS_LBL).text
        return lbl_access_success_txt


