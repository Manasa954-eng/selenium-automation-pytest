import json
import random
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Practice.POM_Project1.login import LoginPage
from Practice.POM_Project1.b_products_page import ProductsPage
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




