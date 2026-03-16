from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    """
		Этот класс представляет собой набор функций для работы с калькулятором
	"""

    URL = "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"

    def __init__(self, driver) -> None:
        """
			Эта функция инициализирует веб-драйвер
		"""
        self.driver = driver

    def open(self) -> None:
        """
			Эта функция открывает страницу по указаному URL
		"""
        self.driver.get(self.URL)

    def set_delay(self, value: int) -> None:
        """
			Эта функция принимает на ввод один числовой параметр, 
            вводит его в окно задержки.
		"""
        delay = self.driver.find_element(By.ID, "delay")
        delay.clear()
        delay.send_keys(value)

    def click_button(self, value: str) -> None:
        """
			Эта функция принимает на ввод один параметр(маркер по тексту), 
            по которому ищет кнопки на странице и кликает на них.
		"""
        self.driver.find_element(
            By.XPATH, f"//span[text()='{value}']"
        ).click()

    def get_result(self) -> int:
        """
			Эта функция возвращает результат после ожидания задержки
		""" 
        WebDriverWait(self.driver, 50).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "screen"), "15"
            )
        )
        return self.driver.find_element(
            By.CLASS_NAME, "screen"
        ).text