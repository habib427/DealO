from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService

def get_driver(browser="chrome"):
    browser = browser.lower()
    if browser == "chrome":
        return webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser == "firefox":
        return webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    elif browser == "edge":
        return webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))
    else:
        raise Exception("Unsupported browser: choose chrome, firefox, or edge")
