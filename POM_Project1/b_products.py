from selenium.webdriver.common.by import By


class ProductsPage:

    def __init__(self, driver):
        self.driver = driver

    def add_items_by_price(self, target_price):
        prices = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_price']")

        count = 0
        for b in prices:
            if b.text == target_price:
                count += 1
                # go to parent (inventory_item) and click its button
                b.find_element(By.XPATH, "./ancestor::div[@class='inventory_item']//button").click()


        return count