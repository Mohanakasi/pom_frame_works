import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from reg_sel_frame_work.generic_functions.wat_deco import wait
from datetime import datetime
class selenium_wrapper:
    def __init__(self,driver):
        self.driver = driver

    @wait
    def finding_element(self, locator):
        return self.driver.find_element(*locator)
    @wait
    def finding_elements(self, locator):
        return self.driver.find_elements(*locator)
    @wait #click_element = wait(click_element) #click_element becomes wrapper
    def click_element(self,locator):  #locator--->("class name","ico-register")
        self.driver.find_element(*locator).click() #---> *locator---> "class name","ico-register"
    @wait #enter_text = wait(enter_text)
    def enter_text(self,locator,value):
        self.driver.find_element(*locator).send_keys(value)
    @wait
    def mouse_hover_to_element_and_click(self, locator):
        A_ch = ActionChains(self.driver)
        A_ch.move_to_element(self.driver.find_element(*locator)).perform()
        A_ch.click().perform()

    @wait
    def select_items(self,locator,value):
        web_el = self.driver.find_element(*locator)
        s = Select(web_el)
        if isinstance(value, str):
            s.select_by_visible_text(value)
        elif isinstance(value, int):
            s.select_by_index(value)
        else:
            raise TypeError

    def screen_shot_capture(self, path):
        time.sleep(3)
        t_stamp= datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        file_name = r'\reg_succ'+t_stamp+'.png'
        self.driver.get_screenshot_as_file(path+file_name)