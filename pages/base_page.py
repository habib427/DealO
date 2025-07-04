import time
import os

class BasePage:
    def scroll_like_user(self, pause_time=0.3, step=300):
        last_height = self.driver.execute_script("return document.body.scrollHeight")
        for i in range(0, last_height, step):
            self.driver.execute_script("window.scrollTo(0, {i});")
            time.sleep(pause_time)

    def scroll_to_top(self):
        self.driver.execute_script("window.scrollTo(0, 0);")
        time.sleep(1)

    def take_screenshot(self, name, browser_name):
        folder = "screenshots"
        if not os.path.exists(folder):
            os.makedirs(folder)
        filepath = os.path.join(folder,"{browser_name}_{name}")
        self.driver.save_screenshot(filepath)
        print("Screenshot saved: {filepath}")

    def __init__(self, driver):
        self.driver = driver
