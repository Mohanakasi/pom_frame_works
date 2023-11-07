import pytest
from selenium.webdriver.common.by import By

from ajio_submission.page_home.pages.home_page import menu_header_validation
from ajio_submission.page_home.pages.items_list_page import home_items_list_page
from time import sleep

@pytest.mark.usefixtures('setup')
class Test_cart_validations:

    def test_cart_item_check_item_and_home_page(self, setup):
        cart_obj1 = home_items_list_page(setup)
        cart_obj1.select_item_from_list()
        cart_obj1.clicking_item_in_sungasses()
        cart_obj1.mouse_hover_to_sunglass_and_click_proceed_to_bag()
        cart_obj1.switching_to_home_page()
        cart_obj1.checking_cart_in_home_page()


    def test_adding_cart_delete(self, setup):
        cart_obj2 = home_items_list_page(setup)
        cart_obj2.select_item_from_list()
        cart_obj2.clicking_item_in_sungasses()
        cart_obj2.deleting_an_item_shipping_page(cart_obj2.mouse_hover_to_sunglass_and_click_proceed_to_bag())

    def test_ajio_logo_test(self, setup):
        cart_obj3 = home_items_list_page(setup)
        cart_obj3.select_item_from_list()
        cart_obj3.clicking_item_in_sungasses()
        cart_obj3.navigating_to_ajio_home(cart_obj3.mouse_hover_to_sunglass_and_click_proceed_to_bag())
