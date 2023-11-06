import time
from ajio_submission.Testbase.selenium_methods import Selenium_re_use_functions
# from ajio_submission.page_home.utilities.locators_all import home_page_locators
from ajio_submission.page_home.utilities.excel_read_data import Excel_test_data
import re
class home_items_list_page(Selenium_re_use_functions, Excel_test_data):

    def navigating_to_men_menu_and_clicking_backpacks(self):
        self.mouse_hover_to_element(self.men_menu_list)
        self.clicking_an_element(self.men_menu_back_pack)


    def items_list_page_header_validating(self):
        time.sleep(5)
        header_text = self.finding_an_element(self.back_pack_heading).text
        assert header_text.lower() == 'backpacks'


    def select_item_from_list(self):
        self.mouse_hover_to_element(self.men_menu_list)
        self.mouse_hover_and_click_on_element(self.sunglass_men_menu)

    def clicking_item_in_sungasses(self):
        self.mouse_hover_and_click_on_element(self.sunglass_item)

    def mouse_hover_to_sunglass_and_click_proceed_to_bag(self):
        time.sleep(3)
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)
        item_head = self.finding_an_element(self.sun_glass_item_head).text
        item_price = int(''.join(re.findall('[0-9]', self.finding_an_element(self.sun_glass_item_price).text)))
        self.mouse_hover_and_click_on_element(self.add_to_bag_sun_glass_item)
        time.sleep(2)
        cart_quantity = int(self.finding_an_element(self.cart_quantity_fetch).text)
        temp_item_no_deci = self.finding_an_element(self.cart_price_fetch).text
        price_cart = int(''.join(re.findall('[0-9]', temp_item_no_deci[0: len(temp_item_no_deci)-3])))
        assert item_price == price_cart
        assert cart_quantity == 1
        self.finding_an_element(self.cart_added_pop_up).text
        self.mouse_hover_and_click_on_element(self.proceed_to_bag_btn)
        return price_cart

    def switching_to_home_page(self):
        time.sleep(3)
        old_tab = self.driver.window_handles[0]
        self.driver.switch_to.window(old_tab)


    def checking_cart_in_home_page(self):
        self.clicking_an_element(self.ajio_logo_home)
        self.mouse_hover_to_element(self.cart_button_home_page)
        self.finding_an_element(self.cart_added_pop_up).text


    def deleting_an_item_shipping_page(self, item_price_from_item_page_cart):
        time.sleep(5)
        # item_price_from_item_page_cart = self.mouse_hover_to_sunglass_and_click_proceed_to_bag()
        temp_price = self.finding_an_element(self.item_price_shipping_page).text
        item_price_shipping_page = int(''.join(re.findall('[0-9]', temp_price[0:len(temp_price)-3])))
        assert item_price_from_item_page_cart == item_price_shipping_page
        self.clicking_an_element(self.delete_btn_ship_page)

    def navigating_to_ajio_home(self, item_price_cart):
        temp_price = self.finding_an_element(self.item_price_shipping_page).text
        item_price_shipping_page = int(''.join(re.findall('[0-9]', temp_price[0:len(temp_price) - 3])))
        assert item_price_cart == item_price_shipping_page
        self.clicking_an_element(self.ajio_logo_home)
        time.sleep(4)


