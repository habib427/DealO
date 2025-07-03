import time
import pytest
from pages.base_page import BasePage
from pages.home_page import HomePage

@pytest.mark.parametrize("category", ["Home", "Food", "Online Stores", "Lifestyle"])
def test_category_navigation(driver, category):
    base = BasePage(driver)
    HomePage(driver).select_city()

    link = driver.find_element("link text", category)
    driver.execute_script("arguments[0].scrollIntoView(true);", link)
    time.sleep(1)
    link.click()
    time.sleep(2)

    base.scroll_like_user()
    base.scroll_to_top()
    base.take_screenshot(f"{category}_page.png", driver.capabilities['browserName'])

    if category != "Home":
        products = driver.find_elements("css selector", ".card.card-product.card-product-list")
        assert len(products) > 0, f"No products found in {category}"
