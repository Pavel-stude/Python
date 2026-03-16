from selenium.webdriver.common.by import By


class CartPage:
    """
		Этот класс представляет собой набор функций для подтверждения корзины
	"""

    def __init__(self, driver) -> None:
        """
			Эта функция инициализирует веб-драйвер
		"""
        self.driver = driver

    def checkout(self) -> None:
        """
			Эта функция кликает на кнопку "Checkout" на странице сайта
		""" 
        self.driver.find_element(By.ID, "checkout").click()