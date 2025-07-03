import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_search_functionality(driver):
    driver.get("https://dealo.com.pk/home/islamabad")
    wait = WebDriverWait(driver, 10)

    try:
        search_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[@class='search_pop m-0 mr-2 my-3 p-0 hide_m d-none d-sm-none d-md-none d-lg-block d-xl-block d-xxl-block']//i[@class='fa-solid fa-magnifying-glass']")))
        search_icon.click()
        search_box = wait.until(EC.visibility_of_element_located((By.ID, "search_id")))
        search_box.send_keys("burger")
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
        assert "burger" in driver.page_source.lower(),"Burger not found in page source"
        print("Search test passed.")
    except Exception as e:
        pytest.fail("Test failed: {str(e)}")
