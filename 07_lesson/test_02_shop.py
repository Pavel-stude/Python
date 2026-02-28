import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox(
        service=FirefoxService(GeckoDriverManager().install())
    )
    yield driver
    driver.quit()


def test_buy(driver):
    login = LoginPage(driver)
    main = MainPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)

    login.open()
    login.login("standard_user", "secret_sauce")

    main.add_item("add-to-cart-sauce-labs-backpack")
    main.add_item("add-to-cart-sauce-labs-bolt-t-shirt")
    main.add_item("add-to-cart-sauce-labs-onesie")
    main.go_to_cart()

    cart.checkout()
    checkout.fill_form("Pavel", "Aytkulov", "410033")

    total = checkout.get_total()
    assert "$58.29" in total