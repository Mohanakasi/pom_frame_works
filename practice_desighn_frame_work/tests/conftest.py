from pytest import fixture
from selenium import webdriver
@fixture
def setup_test():
    driver = webdriver.Chrome()
    driver.get(r"https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    yield driver
    driver.quit()