from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def login(self, username, password):
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    def add_items_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
        ).click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()

    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    def checkout(self):
        self.driver.find_element(By.ID, "checkout").click()

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    def get_total_price(self):
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        total_value = total_text.split("$")[-1]
        return total_value