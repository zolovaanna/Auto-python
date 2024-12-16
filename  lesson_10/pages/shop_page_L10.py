import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы магазина по URL {url}')
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step('Авторизация с именем пользователя {username} и паролем {password}')
    def login(self, username: str, password: str) -> None:
        self.driver.find_element(By.ID, "user-name").send_keys(username)
        self.driver.find_element(By.ID, "password").send_keys(password)
        self.driver.find_element(By.ID, "login-button").click()

    @allure.step('Добавление товаров в корзину')
    def add_items_to_cart(self) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
        ).click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
        self.driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()

    @allure.step('Переход в корзину')
    def go_to_cart(self) -> None:
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    @allure.step('Оформление заказа')
    def checkout(self) -> None:
        self.driver.find_element(By.ID, "checkout").click()

    @allure.step('Заполнение формы оформления заказа с именем {first_name},'
                 ' фамилией {last_name}, почтовым индексом {postal_code}')
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> None:
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        self.driver.find_element(By.ID, "continue").click()

    @allure.step('Получение итоговой суммы заказа')
    def get_total_price(self) -> str:
        total_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        return total_element.text.split("$")[-1]