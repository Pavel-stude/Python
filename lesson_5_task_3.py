from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.fullscreen_window
driver.get("http://the-internet.herokuapp.com/inputs")

field = driver.find_element(By.CSS_SELECTOR, 'input[type="number"]')
field.send_keys("Sky")
sleep(3)
field.clear()
field.send_keys("Pro")

sleep(3)

driver.quit()