from random import random

from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def login(self):
        users = self.driver.find_element(By.XPATH, "//div[@id='login_credentials']").text

        # username
        user_text = users.split("\n")
        # print(user_text)
        user_text.pop(0)
        # print(user_text)

        username = random.choice(user_text)

        # Password
        passw = self.driver.find_element(By.CSS_SELECTOR, "div[class='login_password']").text

        password = (passw.split("\n").pop(1))
        assert "secret" in password

        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input[class='submit-button btn_action']").click()