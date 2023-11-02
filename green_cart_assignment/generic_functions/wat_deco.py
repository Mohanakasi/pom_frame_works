from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from time import sleep
from selenium.webdriver.remote.webelement import WebElement
class   El_v_check():
    def __call__(self, locat_):
        self.locat_ = locat_
        displayed = expected_conditions.visibility_of_element_located(locat_)
        enabled = expected_conditions.element_to_be_clickable(locat_)
        return displayed,enabled

# def element_visible_enable_check(locat_):
#     displayed = expected_conditions.visibility_of_element_located(locat_)
#     print(displayed)
# def element_enable_check(locat_):
#     enabled = expected_conditions.element_to_be_clickable(locat_)
#     print(enabled)
def wait(func):
    def wrapper(*args, **kwargs):
        instan_ = args[0]
        locat_ = args[1]
        print(locat_)
        wait = WebDriverWait(instan_.driver,50)
        v_e = El_v_check()(locat_) #obj = El_v_check()
        wait.until(v_e[0])         #v_e= obj(locat_)
        wait.until(v_e[1])
        return func(*args, **kwargs)
    return wrapper
