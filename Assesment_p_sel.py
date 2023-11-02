from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get(r"https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.XPATH, "//input[@placeholder='Search for Vegetables and Fruits']").send_keys("ca")
driver.find_element(By.CSS_SELECTOR, "button[class='search-button']").click()
sleep(5)
total_items = driver.find_elements(By.XPATH, "//div[@class='product']")
print(len(total_items))
items_add_cart = driver.find_elements(By.XPATH, "//button[text()='ADD TO CART']")
sleep(5)
for item in items_add_cart:
    item.click()
sleep(5)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//div/button[text()='PROCEED TO CHECKOUT']").click()
item_costs = driver.find_elements(By.XPATH, "//tbody/tr/td[5]/p")
# driver.find_elements(By.XPATH, "//tbody/tr/td[1]/../../..//tbody/tr/td[5]/p") #dependent independent
total_cost_expected = sum([int(item.text) for item in item_costs])
print(total_cost_expected)
total_amount_in_page = int(driver.find_element(By.XPATH, "//span[@class='totAmt']").text)
print(total_amount_in_page)
assert total_cost_expected == total_amount_in_page
sleep(5)
# driver.find_element(By.XPATH, "//button[text()='Place Order']").click()
A_ch = ActionChains(driver)
A_ch.move_to_element(driver.find_element(By.XPATH, "//button[text()='Place Order']")).perform()
A_ch.click().perform()
country_dd = Select(driver.find_element(By.XPATH, "//div/select"))
country_dd.select_by_visible_text("India")
driver.find_element(By.XPATH, "//input[@type='checkbox' and @class='chkAgree']").click()
driver.find_element(By.XPATH, "//div/button[text()='Proceed']").click()
sleep(1)
driver.get_screenshot_as_file(r"C:\development\python_slenium\practice\confirm.png")
order_confirm_messege = driver.find_element(By.XPATH, "//div[@class='wrapperTwo']/span").text
print(order_confirm_messege)
