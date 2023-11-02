import time
from selenium.webdriver.common.by import By
from green_cart_assignment.generic_functions.selenium_functions import selenium_wrapper
class pm_cl_gk(selenium_wrapper):
   search_field = ((By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']"), 'ca')
   search_button = (By.CSS_SELECTOR, "button[class='search-button']")
   items = (By.XPATH, "//div[@class='product']")
   add_to_cart_btn = (By.XPATH, "//button[text()='ADD TO CART']")
   cart_button = (By.CSS_SELECTOR, "img[alt='Cart']")
   check_out_link = (By.XPATH, "//div/button[text()='PROCEED TO CHECKOUT']")
   each_item_costs = (By.XPATH, "//tbody/tr/td[5]/p")
   total_amount_page = (By.XPATH, "//span[@class='totAmt']")
   place_order_button = (By.XPATH, "//button[text()='Place Order']")
   country_dd = (By.XPATH, "//div/select")
   t_cond_ch_box = (By.XPATH, "//input[@type='checkbox' and @class='chkAgree']")
   chk_out_prc_btn = (By.XPATH, "//div/button[text()='Proceed']")
   screen_shot_path = r"C:\development\pom_frame_work\green_cart_assignment\Results"
   order_confirm_msg = (By.XPATH, "//div[@class='wrapperTwo']/span")
   def searching_ca_items(self):
       self.enter_text(*self.search_field)

   def click_search(self):
       self.click_element(self.search_button)

   def fetcing_total_items(self):
       total_items = self.finding_elements(self.items)
       print(len(total_items))

   def adding_items_to_cart(self):
       time.sleep(3)
       items_add_to_cart = self.finding_elements(self.add_to_cart_btn)
       for item in items_add_to_cart:
           item.click()

   def click_on_cart_button(self):
       self.click_element(self.cart_button)

   def click_on_check_out_link(self):
       self.click_element(self.check_out_link)

   def price_validation_check_out_page(self):
       item_costs = self.finding_elements(self.each_item_costs)
       total_cost_expected = sum([int(item.text) for item in item_costs])
       print(total_cost_expected)
       total_cost_from_total = int(self.finding_element(self.total_amount_page).text)
       print(total_cost_from_total)
       assert total_cost_expected == total_cost_from_total

   def click_on_place_order(self):
       self.mouse_hover_to_element_and_click(self.place_order_button)

   def country_select(self):
       self.select_items(self.country_dd, "India")

   def agree_terms_conditions_check_box(self):
       self.click_element(self.t_cond_ch_box)

   def click_on_proceed(self):
       self.click_element(self.chk_out_prc_btn)

   def taking_screen_shot_order_confirmation(self):
       self.screen_shot_capture(self.screen_shot_path)

   def printing_order_confirm_text(self):
       print(self.finding_element(self.order_confirm_msg).text)
