from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

driver.fullscreen_window
driver.get("http://the-internet.herokuapp.com/login")

login_field = driver.find_element(By.CSS_SELECTOR, "#username")
login_field.send_keys("tomsmith")

password_field = driver.find_element(By.CSS_SELECTOR, "#password")
password_field.send_keys("SuperSecretPassword!")

login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
login_button.click()

die = driver.find_element(By.CSS_SELECTOR, "#flash").text
print(die)

sleep(5)

driver.quit()