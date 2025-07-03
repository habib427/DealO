import time
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scroll_to_bottom(driver):
    last_position = driver.execute_script("return window.pageYOffset;")
    while True:
        driver.execute_script("window.scrollBy(0, 300);")
        time.sleep(0.4)
        curr_position = driver.execute_script("return window.pageYOffset;")
        if curr_position == last_position:
            break
        last_position = curr_position

def scroll_to_top(driver):
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

def take_screenshot(driver, name):
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)
    path = os.path.join(folder, f"{name}.png")
    driver.save_screenshot(path)
    print("Screenshot saved: {path}")

def test_scroll_and_capture(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://dealo.com.pk/home/islamabad")
    driver.maximize_window()
    time.sleep(2)

    categories = ["Home", "Food", "Online Stores", "Lifestyle"]

    for category in categories:
        print("Navigating to: {category}")
        try:
            link = wait.until(EC.element_to_be_clickable((By.LINK_TEXT, category)))
            driver.execute_script("arguments[0].scrollIntoView(true);", link)
            link.click()
            time.sleep(3)

            wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".card.card-product.card-product-list")))

            print("Scrolling to down")
            scroll_to_bottom(driver)

            print("Scrolling back to top")
            scroll_to_top(driver)

            take_screenshot(driver, category.replace(" ", "_"))

        except Exception as e:
            print("Error in {category}: {str(e)}")
