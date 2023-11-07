import pytest
from selenium.webdriver.common.by import By

from ajio_submission.page_home.pages.home_page import menu_header_validation
from ajio_submission.page_home.pages.items_list_page import home_items_list_page
from time import sleep

@pytest.mark.usefixtures('setup')
class Test_home_page_header:


    def test_menu_list(self, setup):
        menu_obj1 = menu_header_validation(setup)
        menu_obj1.mouse_hovering_to_men_menu()
        menu_obj1.mouse_hovering_to_woomen_menu()
        menu_obj1.mouse_hoverig_to_kids_menu()
        menu_obj1.mouse_hoverig_to_indie_menu()
        menu_obj1.mouse_hoverig_to_home_kitechen_menu()
    #
    #
    def test_items_list_heading_validation(self, setup):
        heading_obj1 = home_items_list_page(setup)
        heading_obj1.navigating_to_men_menu_and_clicking_backpacks()
        heading_obj1.items_list_page_header_validating()

