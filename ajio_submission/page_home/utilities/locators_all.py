from selenium.webdriver.common.by import By


class home_page_locators:
    men_menu_list = (By.XPATH, "//a[text()='MEN']")
    back_packs = (By.XPATH, "//span/a[text()='Backpacks']")
    women_menu_list = (By.XPATH, "//a[text()='WOMEN']")
    kids_menu_list = (By.XPATH, "//a[text()='KIDS']")
    indie_men_list = (By.XPATH, "//a[text()='INDIE']")
    home_and_kitchen_menu_list = (By.XPATH, "//a[text()='HOME AND KITCHEN']")
    men_menu_back_pack  =   (By.XPATH, "//span/a[text()='Backpacks']")
    back_pack_heading   = (By.XPATH, "//div[@class='header2' and text()='Backpacks']")


