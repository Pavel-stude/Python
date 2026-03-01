import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture
def driver():
    service = FirefoxService(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    yield driver
    driver.quit()


def test_buy(driver):
    driver.get("https://www.saucedemo.com")

    driver.find_element(By.CSS_SELECTOR, "#user-name").send_keys(
        "standard_user"
    )

    driver.find_element(By.CSS_SELECTOR, "#password").send_keys(
        "secret_sauce"
    )
    
    driver.find_element(By.CSS_SELECTOR, "#login-button").click()

    driver.find_element(
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-backpack",
    ).click()

    driver.find_element(
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-bolt-t-shirt",
    ).click()

    driver.find_element(
        By.CSS_SELECTOR,
        "#add-to-cart-sauce-labs-onesie",
    ).click()

    driver.find_element(
        By.CSS_SELECTOR,
        "a.shopping_cart_link",
    ).click()

    driver.find_element(By.CSS_SELECTOR, "#checkout").click()

    driver.find_element(By.CSS_SELECTOR, "#first-name").send_keys("Pavel")
    driver.find_element(By.CSS_SELECTOR, "#last-name").send_keys("Aytkulov")
    driver.find_element(By.CSS_SELECTOR, "#postal-code").send_keys("410033")
    driver.find_element(By.CSS_SELECTOR, "#continue").click()

    total = driver.find_element(
        By.CSS_SELECTOR,
        "div.summary_total_label",
    ).text

    assert "58.29" in total
