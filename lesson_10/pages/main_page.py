from selenium.webdriver.common.by import By


class MainPage:
    """
		Этот класс представляет собой набор функций для 
        поиска и добавления товаров в корзину
	"""

    def __init__(self, driver) -> None:
        """
			Эта функция инициализирует веб-драйвер
		"""
        self.driver = driver

    def add_item(self, item_id: str) -> None:
        """
			Эта функция принимает на ввод один параметр(маркер по ID), 
            по которому ищет кнопки на странице и кликает на них.
		""" 
        self.driver.find_element(By.ID, item_id).click()

    def go_to_cart(self) -> None:
        """
			Эта функция кликает на кнопку корзины на странице сайта
		"""
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()