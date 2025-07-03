import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from pages.home_page import HomePage

def test_product_detail_page(driver):
    base = BasePage(driver)
    driver.get("https://dealo.com.pk/home/islamabad")

    lifestyle = driver.find_element(By.LINK_TEXT, "Lifestyle")
    lifestyle.click()
    time.sleep(2)

    product = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[@class='online_store_grid_sec']//div[2]/div[1]"))
    )
    product.click()

    title = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "product-title"))).text
    img = driver.find_element(By.CSS_SELECTOR, ".carousel-inner img").get_attribute("src")
    dropdown = driver.find_element(By.CSS_SELECTOR, "select")

    assert title.strip(), "Product title is missing"
    assert any(img.endswith(ext) for ext in [".jpg", ".jpeg", ".png", ".webp"]), "Invalid product image"
    assert dropdown.is_displayed(), "Outlet dropdown not shown"

    base.scroll_to_bottom()
    base.scroll_to_top()
    base.take_screenshot("product_detail_scrolled.png", driver.capabilities['browserName'])
