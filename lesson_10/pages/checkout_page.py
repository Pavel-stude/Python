from selenium.webdriver.common.by import By


class CheckoutPage:
    """
		Этот класс представляет собой набор функций для ввода
        данных для доставки и возвращает стоисть товаров в корзине
	"""

    def __init__(self, driver) -> None:
        """
			Эта функция инициализирует веб-драйвер
		"""
        self.driver = driver

    def fill_form(self, first: str, last: str, zip_code: int) -> None:
        """
			Эта функция берет три параметра (имя, фамилию и почтовый индекс), 
            вводит и передает их в форму заполнения данных на сайте.
		""" 
        self.driver.find_element(By.ID, "first-name").send_keys(first)
        self.driver.find_element(By.ID, "last-name").send_keys(last)
        self.driver.find_element(By.ID, "postal-code").send_keys(zip_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total(self) -> float:
        """
			Эта функция возвращает итоговую стоимость товаров
		"""
        return self.driver.find_element(
            By.CLASS_NAME, "summary_total_label"
        ).text