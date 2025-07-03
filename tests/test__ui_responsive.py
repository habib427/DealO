import pytest
import time
from selenium.webdriver.common.by import By

viewports = [
    {"name": "Mobile", "width": 375, "height": 667},
    {"name": "Tablet", "width": 768, "height": 1024},
    {"name": "Desktop", "width": 1920, "height": 1080},
]
@pytest.mark.parametrize("viewport", viewports)
def test_ui_responsiveness(driver, viewport):
    name = viewport["name"]
    width = viewport["width"]
    height = viewport["height"]

    driver.set_window_size(width, height)
    driver.get("https://dealo.com.pk/home/islamabad")
    time.sleep(2)

    print(f"Testing viewport: {name} ({width}x{height})")

    assert driver.find_element(By.TAG_NAME, "header").is_displayed(),"Header not visible in {name} view"
    assert driver.find_element(By.CSS_SELECTOR, ".tab-list").is_displayed()," Category tabs not visible in {name} view"

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    filename = f"screenshots/ui_{name.lower()}.png"
    driver.save_screenshot(filename)
    print("Screenshot saved: {filename}")
