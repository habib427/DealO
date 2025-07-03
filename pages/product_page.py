from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_from_lifestyle(self):
        print("Clicking second product from Lifestyle")
        product_xpath = "//body/div/div[@class='online_store_sec online_store_page']/div[@class='container']/div[@class='online_store_grid_sec']/div[@class='row']/div[2]/div[1]"
        first_product = self.wait.until(EC.element_to_be_clickable((By.XPATH, product_xpath)))
        self.driver.execute_script("arguments[0].scrollIntoView(true);", first_product)
        first_product.click()

    def get_product_title(self):
        return self.wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "product-title"))).text

    def get_product_image_url(self):
        return self.driver.find_element(By.CSS_SELECTOR, ".carousel-inner img").get_attribute("src")

    def is_outlet_dropdown_present(self):
        dropdown = self.driver.find_element(By.CSS_SELECTOR, "select")
        return dropdown.is_displayed()
