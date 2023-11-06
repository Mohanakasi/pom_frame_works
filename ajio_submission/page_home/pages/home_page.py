import time
from ajio_submission.Testbase.selenium_methods import Selenium_re_use_functions
# from ajio_submission.page_home.utilities.locators_all import home_page_locators
from ajio_submission.page_home.utilities.excel_read_data import Excel_test_data


# path = r"C:\development\pom_frame_work\ajio_submission\Results\menu_list"

class menu_header_validation(Selenium_re_use_functions, Excel_test_data):


    def mouse_hovering_to_men_menu(self):
        self.mouse_hover_to_element(self.men_menu_list)

    def mouse_hovering_to_woomen_menu(self):
        self.mouse_hover_to_element(self.women_menu_list)


    def mouse_hoverig_to_kids_menu(self):
        self.mouse_hover_to_element(self.kids_menu_list)

    def mouse_hoverig_to_indie_menu(self):
        self.mouse_hover_to_element(self.indie_men_list)


    def mouse_hoverig_to_home_kitechen_menu(self):
        self.mouse_hover_to_element(self.home_and_kitchen_menu_list)

