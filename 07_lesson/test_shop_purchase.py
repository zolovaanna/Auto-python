import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from shop_page import ShopPage  # Импортируем класс страницы


@pytest.fixture(scope="module")  # Используем scope="module" для оптимизации
def driver():
    # Запуск Chrome-драйвера с использованием ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_shop_purchase(driver):
    # Создаем объект страницы магазина
    shop_page = ShopPage(driver)

    # Открываем сайт магазина
    shop_page.open("https://www.saucedemo.com/")

    # Авторизация
    shop_page.login("standard_user", "secret_sauce")

    # Добавление товаров в корзину
    shop_page.add_items_to_cart()

    # Переход в корзину
    shop_page.go_to_cart()

    # Нажимаем на кнопку Checkout
    shop_page.checkout()

    # Заполняем форму для оформления
    shop_page.fill_checkout_form("Иван", "Петров", "123456")

    # Получаем итоговую сумму
    total_value = shop_page.get_total_price()

    # Проверка итоговой суммы
    assert total_value == "58.29", (
        f"Expected total to be $58.29, but got ${total_value}. "
        "Проверьте итоговую сумму в корзине."
    )