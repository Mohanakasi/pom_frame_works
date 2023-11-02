from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://demowebshop.tricentis.com/")
# locat_ = (By.CLASS_NAME, "ico-register")
# wait = WebDriverWait(driver,50)
# displayed = expected_conditions.visibility_of_element_located(locat_)
# print(type(displayed))
# wait.until(displayed)
# enabled = expected_conditions.element_to_be_clickable(locat_)
# print(enabled)
# wait.until(enabled)
# driver.find_element(By.CLASS_NAME, "ico-register").click()
driver.get_screenshot_as_file()