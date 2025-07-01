from selenium.webdriver.common.by import By
class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.logo_selector = (By.CSS_SELECTOR, 'img[alt="Website for automation practice"]')
        self.products_link = (By.CSS_SELECTOR, 'a[href="/products"]')

    def goto(self):
        self.driver.get("https://automationexercise.com/")
        # self.page.wait_for_load_state("domcontentloaded")

    def is_home_page_visible(self):
        return self.driver.find_element(*self.logo_selector).is_displayed()

    def goto_products(self):
        self.driver.find_element(*self.products_link).click()