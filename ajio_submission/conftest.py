from pytest import fixture
from selenium import webdriver
@fixture
def _driver():
    driver = webdriver.Chrome()
    driver.get(r"https://www.ajio.com")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.quit()