import json
import random
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Practice.POM_Project1.a_login_page import LoginPage
from Practice.POM_Project1.b_products import ProductsPage
from Practice.POM_Project1.c_cart_page import CartPage
from Practice.POM_Project1.d_checkout_page import CheckoutPage

test_path = "C:\\Users\\Manasa\\PycharmProjects\\PythonProject\\Practice\\test_Project.json"
with open(test_path) as b:
    test_data = json.load(b)
    test_data_set = test_data["data"]

@pytest.mark.parametrize("test_one" ,test_data_set)
def test_project(browser, test_one):
    driver = browser

    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.login()
    expected_count = products.add_items_by_price("$15.99")

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))

    cart.open_cart()
    cart_items = cart.get_cart_prices()

    # Count Validation
    assert len(cart_items) == expected_count
    # Price Validation
    for item in cart_items:
        assert item.text == "$15.99"

    checkout.complete_checkout(test_one["firstName"], test_one["lastName"], test_one["postalName"])
    assert "order" in checkout.get_confirmation_text().lower()








