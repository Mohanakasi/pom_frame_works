import time

from selenium.webdriver.common.by import By
from selenium import webdriver
class Login:
    user_name = (By.NAME, "username")
    pass_word = (By.NAME, "password")
    submit_btn = (By.XPATH, "//button[@type='submit']")
    user_drop_down = (By.XPATH, "//span[@class='oxd-userdropdown-tab']")
    log_out_link = (By.XPATH, "//li/a[text()='Logout']")

    def __init__(self, driver):
        self.driver = driver

    def enter_user_name(self, u_name):
        time.sleep(5)
        self.driver.find_element(*self.user_name).send_keys(u_name)

    def enter_pass_word(self, passes):
        time.sleep(4)
        self.driver.find_element(*self.pass_word).send_keys(passes)

    def click_on_submit_button(self):
        time.sleep(3)
        self.driver.find_element(*self.submit_btn).click()

    def click_on_profile(self):
        time.sleep(5)
        self.driver.find_element(*self.user_drop_down).click()

    def log_out(self):
        time.sleep(3)
        self.driver.find_element(*self.log_out_link).click()

