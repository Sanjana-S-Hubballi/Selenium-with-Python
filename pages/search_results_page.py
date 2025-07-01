from selenium.webdriver.common.by import By

class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_product_link = (By.CSS_SELECTOR, 'a[href="/product_details/1"]')

    def view_first_product(self):
        self.driver.find_element(*self.first_product_link).click()