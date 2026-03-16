import pytest
import allure
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.webdriver import WebDriver
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


@allure.epic("Lesson 7")
@allure.severity("critical")
@allure.id("Test 2")
@allure.feature("Shop")
@allure.title("Покупка товаров на сайте онлайн магазина")
@allure.description("Автотест на проверку авторизации и полного цикла покупки товаров на сайте")
def test_buy(driver: WebDriver):
    with allure.step("Назначить переменую для класса LoginPage"):
        login = LoginPage(driver)

    with allure.step("Назначить переменую для класса MainPage"):
        main = MainPage(driver)

    with allure.step("Назначить переменую для класса CartPage"):
        cart = CartPage(driver)

    with allure.step("Назначить переменую для класса CheckoutPage"):
        checkout = CheckoutPage(driver)
    
    with allure.step("Открыть страницу сайта"):
        login.open()

    with allure.step("Авторизоваться на сайте"):
        login.login("standard_user", "secret_sauce")
    
    with allure.step("Добавить товар в корзиеу по ID"):
        main.add_item("add-to-cart-sauce-labs-backpack")

    with allure.step("Добавить товар в корзиеу по ID"):
        main.add_item("add-to-cart-sauce-labs-bolt-t-shirt")

    with allure.step("Добавить товар в корзиеу по ID"):
        main.add_item("add-to-cart-sauce-labs-onesie")

    with allure.step("Перейти в корзину"):
        main.go_to_cart()
    
    with allure.step("Нажать на кнопку опратить товары (Checkout)"):
        cart.checkout()

    with allure.step("Заполнить данные в форме"):
        checkout.fill_form("Pavel", "Aytkulov", 410033)

    with allure.step("Назначить переменую для функции, возвращающей итоговую стоимость"):
        total = checkout.get_total()
    with allure.step("Проверить результат"):
        assert "$58.29" in total