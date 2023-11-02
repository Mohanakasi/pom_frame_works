import time
from ajio_submission.Testbase.selenium_methods import Selenium_re_use_functions
# from ajio_submission.page_home.utilities.locators_all import home_page_locators
from ajio_submission.page_home.utilities.excel_read_data import Excel_test_data

class home_items_list_page(Selenium_re_use_functions, Excel_test_data):

    def navigating_to_men_menu_and_clicking_backpacks(self):
        self.mouse_hover_to_element(self.men_menu_list)
        self.clicking_an_element(self.men_menu_back_pack)


    def items_list_page_header_validating(self):
        time.sleep(5)
        header_text = self.finding_an_element(self.back_pack_heading).text
        assert header_text.lower() == 'backpacks'


    def select_item_from_list(self):
        self.mouse_hover_and_click_on_element(self.sunglass_men_menu)

    def clicking_item_in_sungasses(self):
        self.mouse_hover_and_click_on_element(self.sunglass_item)

