import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from pages.calculator_page import CalculatorPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    ) 
    yield driver
    driver.quit()


@allure.epic("Lesson 7")
@allure.severity("normal")
@allure.id("Test 1")
@allure.feature("Calculator")
@allure.title("Проверка результата в калькуляторе")
@allure.description("Автотест на проверку результата в калькуляторе который выводтися с задержкой")
def test_calculator(driver):
    with allure.step("Назначить переменую для класса CalculatorPage"):
        page = CalculatorPage(driver)

    with allure.step("Открыть страницу сайта"):
        page.open()

    with allure.step("Устанавить задержку на получение результата 45 секунд"):
        page.set_delay("45")

    with allure.step("Нажать на калькуляторе кнопку 7"):
        page.click_button("7")

    with allure.step("Нажать на калькуляторе кнопку +"):
        page.click_button("+")

    with allure.step("Нажать на калькуляторе кнопку 8"):
        page.click_button("8")

    with allure.step("Нажать на калькуляторе кнопку ="):
        page.click_button("=")

    with allure.step("Назначить переменую для функции, возвращающей результат после задержки"):
        result = page.get_result()
    
    with allure.step("Проверить результат"):
        assert result == "15"