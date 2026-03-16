from selenium.webdriver.common.by import By


class LoginPage:
    """
		Этот класс представляет собой набор функций для 
        авторизации на сайте
	"""

    URL = "https://www.saucedemo.com/"

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

    def login(self, username: str, password: str) -> None:
        """
			Эта функция принимает на ввод два параметра(логин и пароль) и 
            авторизовывает на сайте.
		"""
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()