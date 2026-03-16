Автоматизированные тесты Selenium
Описание проекта

Проект содержит автоматизированные UI-тесты, написанные на Python с использованием Selenium и Pytest.
Тесты проверяют работу веб-приложений: калькулятора и интернет-магазина.

Для формирования отчётов используется Allure.

Используемые технологии:
Python
Pytest
Selenium WebDriver
Allure
WebDriver Manager

Установка зависимостей
Перед запуском тестов необходимо установить зависимости:
pip install pytest
pip install selenium
pip install webdriver-manager
pip install allure-pytest

Запуск тестов
Для запуска всех тестов выполните команду:
pytest
В случае когда Python установлен со стандартного магазина Microsoft:
python -m pytest
Для запуска тестов с формированием отчёта Allure:
pytest --alluredir=./allure-results
В случае когда Python установлен со стандартного магазина Microsoft:
python -m pytest --alluredir=./allure-results
После выполнения тестов будет создана папка allure-results, содержащая данные для отчёта.

Просмотр отчёта Allure
Чтобы открыть отчёт, выполните команду:
allure serve allure-results
После этого автоматически откроется браузер с отчётом, где можно посмотреть:
список тестов
статус выполнения
шаги тестов
возможные ошибки