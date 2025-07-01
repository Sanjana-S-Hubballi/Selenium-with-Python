from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class ProductsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.all_products_header = (By.CSS_SELECTOR, 'h2.title.text-center')
        self.products_list = (By.CSS_SELECTOR, '.features_items')
        self.first_product_view_product = (By.XPATH, '(//a[contains(text(),"View Product")])[1]')

    def is_all_products_visible(self):
        element = self.wait.until(EC.visibility_of_element_located(self.all_products_header))
        return element.is_displayed()

    def is_products_list_visible(self):
        element = self.wait.until(EC.visibility_of_element_located(self.products_list))
        return element.is_displayed()

    def view_first_product(self):
        # Wait until clickable
        element = self.wait.until(EC.element_to_be_clickable(self.first_product_view_product))
        
        # Scroll into view
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        
        # Try safe click with ActionChains
        ActionChains(self.driver).move_to_element(element).click().perform()