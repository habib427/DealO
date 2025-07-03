from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def open_home_with_city(self, city="islamabad"):
        self.driver.get(f"https://dealo.com.pk/home/{city}")

