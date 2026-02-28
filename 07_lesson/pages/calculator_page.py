from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get(self.URL)

    def set_delay(self, value):
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(value)

    def click_button(self, value):
        self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        ).click()

    def get_result(self):
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), "15"
            )
        )
        return self.driver.find_element(
            By.CLASS_NAME, "screen"
        ).text