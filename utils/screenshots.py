import os
import time

def take_screenshot(driver, name):
    """Save a screenshot with timestamp + browser name"""
    folder = "screenshots"
    if not os.path.exists(folder):
        os.makedirs(folder)

    browser_name = driver.capabilities.get("browserName", "unknown")
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{browser_name}_{name}_{timestamp}.png"
    filepath = os.path.join(folder, filename)

    driver.save_screenshot(filepath)
    print(f"📸 Screenshot saved: {filepath}")
