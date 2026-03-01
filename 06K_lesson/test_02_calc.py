import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calculator(driver):
    driver.get(
        "https://bonigarcia.dev/"
        "selenium-webdriver-java/slow-calculator.html"
    )

    delay = driver.find_element(By.CSS_SELECTOR, "#delay")
    delay.clear()
    delay.send_keys("45")

    driver.find_element(By.XPATH, "//span[text()='7']").click()
    driver.find_element(By.XPATH, "//span[text()='+']").click()
    driver.find_element(By.XPATH, "//span[text()='8']").click()
    driver.find_element(By.XPATH, "//span[text()='=']").click()

    result = WebDriverWait(driver, 50).until(
        EC.text_to_be_present_in_element(
            (By.CSS_SELECTOR, "div.screen"),
            "15",
        )
    )

    assert result