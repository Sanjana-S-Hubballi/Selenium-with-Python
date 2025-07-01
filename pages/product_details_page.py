from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductDetailsPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

        self.product_info = (By.CSS_SELECTOR, '.product-information')
        self.add_to_cart_button = (By.CSS_SELECTOR, 'button.btn.btn-default.cart')
        self.modal_view_cart_button = (By.CSS_SELECTOR, '#cartModal a[href="/view_cart"]')

    def is_product_details_visible(self):
        element = self.wait.until(EC.visibility_of_element_located(self.product_info))
        return element.is_displayed()

    def add_to_cart(self):
        self.driver.find_element(*self.add_to_cart_button).click()
        # Wait for the modal View Cart link to appear
        self.wait.until(EC.visibility_of_element_located(self.modal_view_cart_button))

    def view_cart(self):
        self.driver.find_element(*self.modal_view_cart_button).click()