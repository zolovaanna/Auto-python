import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lesson10.pages.shop_page_L10 import ShopPage


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.parent_suite("Тесты интернет-магазина")
@allure.suite("Тесты магазина")
@allure.epic("Тестирование интернет-магазина")
@allure.feature("Покупка товаров")
@allure.story("Проверка добавления товаров в корзину и оформления заказа")
@allure.title("Проверка успешного оформления заказа")
@allure.description("""
Этот тест проверяет:
1. Авторизацию пользователя.
2. Добавление товаров в корзину.
3. Проверку итоговой суммы.
4. Успешное оформление заказа.
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("ID", "SHOP-001")
def test_shop_purchase(driver):
    shop_page = ShopPage(driver)

    with allure.step("Открыть сайт магазина"):
        shop_page.open("https://www.saucedemo.com/")

    with allure.step("Авторизоваться"):
        shop_page.login("standard_user", "secret_sauce")

    with allure.step("Добавить товары в корзину"):
        shop_page.add_items_to_cart()

    with allure.step("Перейти в корзину"):
        shop_page.go_to_cart()

    with allure.step("Нажать Checkout"):
        shop_page.checkout()

    with allure.step("Заполнить форму оформления заказа"):
        shop_page.fill_checkout_form("Иван", "Петров", "123456")

    with allure.step("Проверить итоговую сумму"):
        total_value = shop_page.get_total_price()
        assert total_value == "58.29", (
            f"Expected total to be $58.29, but got ${total_value}. "
            "Проверьте итоговую сумму в корзине."
        )