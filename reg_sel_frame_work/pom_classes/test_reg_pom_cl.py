from reg_sel_frame_work.generic_functions.selenium_functions import selenium_wrapper
from selenium.webdriver.common.by import By
from random import randint
class pm_cl(selenium_wrapper):
    reg_link = (By.CLASS_NAME, "ico-register")
    gen_male = (By.ID, "gender-male")
    first_name = ((By.ID, "FirstName"), "mohana kasi")
    last_name = ((By.ID, "LastName"), "settipalli")
    email_ = ((By.NAME, "Email"), f"karthiknk{randint(0,100)}@gmail.com")
    password_ = ((By.ID, "Password"), "Mohana1995")
    cnf_password_ = ((By.ID, "ConfirmPassword"), "Mohana1995")
    register_button = (By.ID, "register-button")

    def click_reg_link(self):
        self.click_element(self.reg_link)  # click_element(self,(By.CLASS_NAME,"ico-register"))

    def click_gender_male(self):
        self.click_element(self.gen_male)
    def enter_first_name(self):
        self.enter_text(*self.first_name)
    def enter_last_name(self):
        self.enter_text(*self.last_name)

    def enter_mail(self):
        self.enter_text(*self.email_)
    def enter_password(self):
        self.enter_text(*self.password_)
    def enter_comfirm_password(self):
        self.enter_text(*self.cnf_password_)

    def click_reg_button(self):
        self.click_element(self.register_button)

    def take_screen_shot_success_reg(self):
        self.screen_shot_capture()
