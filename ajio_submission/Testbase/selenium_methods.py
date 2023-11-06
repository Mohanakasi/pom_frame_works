import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from datetime import datetime
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.expected_conditions import visibility_of_element_located, element_to_be_clickable
from ajio_submission.page_home.utilities.excel_read_data import Excel_test_data, locators_fetch_from_excel
class El_vis_enab_check():
    def __call__(self, locator_):
        self.locator_ = locator_
        displayed = visibility_of_element_located(locator_)
        enabled = element_to_be_clickable(locator_)
        return displayed,enabled


def wait_deco(func):
    def wrapper(*args, **kwargs):
        instance_ = args[0]
        locat_ =    args[1]
        wait_ = WebDriverWait(instance_.driver, 50)
        v = El_vis_enab_check()(locat_)
        wait_.until(v[0])
        wait_.until(v[1])
        return func(*args, **kwargs)
    return wrapper

class Selenium_re_use_functions:


    def __init__(self, driver):
        self.driver = driver
        locators_fetch_from_excel()


    @wait_deco
    def finding_an_element(self, locator):
        return self.driver.find_element(*locator)

    @wait_deco
    def finding_elements(self, locator):
        return self.driver.find_elements(*locator)

    @wait_deco
    def clicking_an_element(self, locator):
        self.driver.find_element(*locator).click()

    @wait_deco
    def entering_text_into_text_field(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @wait_deco
    def selecting_a_item_from_frop_down(self, locator, value):
        web_el_l_box = self.driver.find_element(*locator)
        drop_down = Select(web_el_l_box)
        if isinstance(value, str):
            drop_down.select_by_visible_text(value)
        elif isinstance(value, int):
            drop_down.select_by_index(value)
        else:
            raise TypeError

    @wait_deco
    def mouse_hover_to_element(self, locator):
        A_ch_obj = ActionChains(self.driver)
        web_el = self.driver.find_element(*locator)
        A_ch_obj.move_to_element(web_el).perform()

    @wait_deco
    def mouse_hover_and_click_on_element(self, locator):
        A_ch_obj = ActionChains(self.driver)
        web_el = self.driver.find_element(*locator)
        A_ch_obj.move_to_element(web_el).click().perform()


    def page_screen_shot_capture(self, path,s_shot_name):
        time.sleep(4)
        t_stamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_name = s_shot_name+t_stamp+'.png'
        self.driver.get_screenshot_as_file(path+file_name)
