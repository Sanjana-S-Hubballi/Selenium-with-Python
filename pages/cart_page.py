from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_table = (By.ID, "cart_info_table")
        self.product_price = (By.CSS_SELECTOR, "#product-1 .cart_price p")
        self.product_quantity = (By.CSS_SELECTOR, "#product-1 .cart_quantity button")
        self.product_total = (By.CSS_SELECTOR, "#product-1 .cart_total p")

    def is_product_in_cart(self, product_name):
        xpath = f'//a[contains(text(),"{product_name}")]'
        return self.driver.find_element(By.XPATH, xpath).is_displayed()

    def get_product_price(self):
        return self.driver.find_element(*self.product_price).text

    def get_product_quantity(self):
        return self.driver.find_element(*self.product_quantity).text

    def get_product_total(self):
        return self.driver.find_element(*self.product_total).text