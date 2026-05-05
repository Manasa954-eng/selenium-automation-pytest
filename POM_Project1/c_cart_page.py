from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[class='shopping_cart_link']").click()

    def get_cart_prices(self):
        return self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")