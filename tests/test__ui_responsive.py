import pytest
import time
from selenium.webdriver.common.by import By

viewports = [
    {"name": "Mobile", "width": 375, "height": 667},      # iPhone 8
    {"name": "Tablet", "width": 768, "height": 1024},     # iPad
    {"name": "Desktop", "width": 1920, "height": 1080},   # Full HD
]

@pytest.mark.parametrize("viewport", viewports)
def test_ui_responsiveness(driver, viewport):
    name = viewport["name"]
    width = viewport["width"]
    height = viewport["height"]

    driver.set_window_size(width, height)
    driver.get("https://dealo.com.pk/home/islamabad")
    time.sleep(2)

    print(f"\n🔍 Testing viewport: {name} ({width}x{height})")

    # Example: Verify header and category tabs exist
    assert driver.find_element(By.TAG_NAME, "header").is_displayed(), f"❌ Header not visible in {name} view"

    # Example: Check tab list/menu exists
    assert driver.find_element(By.CSS_SELECTOR, ".tab-list").is_displayed(), f"❌ Category tabs not visible in {name} view"

    # Scroll like a user
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    driver.execute_script("window.scrollTo(0, 0);")
    time.sleep(1)

    # Take screenshot
    filename = f"screenshots/ui_{name.lower()}.png"
    driver.save_screenshot(filename)
    print(f"📸 Screenshot saved: {filename}")
