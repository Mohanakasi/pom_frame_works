from pytest import fixture
from selenium import webdriver
@fixture(scope='function')
def setup():
    driver = webdriver.Chrome()
    driver.get(r"https://www.ajio.com")
    driver.implicitly_wait(5)
    driver.maximize_window()
    yield driver
    driver.close()


# from selenium import webdriver
# import pytest


# @pytest.fixture(params=["chrome", "firefox"], scope='class')
# def init_driver(request):
#     if request.param == "chrome":
#         driver = webdriver.Chrome()
#         request.cls.driver = driver
#     elif request.param == "firefox":
#         driver = webdriver.Firefox()
#         request.cls.driver = driver
#     yield
#     driver.quit()






