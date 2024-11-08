import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager  # Подключаем менеджер драйвера


@pytest.fixture
def driver():
    # Запуск Chrome-драйвера с использованием ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_shop_purchase(driver):
    # Шаг 1: Открыть сайт магазина
    driver.get("https://www.saucedemo.com/")

    # Шаг 2: Авторизация
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # Шаг 3: Добавление товаров в корзину
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-backpack']"))
    ).click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-bolt-t-shirt']").click()
    driver.find_element(By.XPATH, "//button[@data-test='add-to-cart-sauce-labs-onesie']").click()

    # Шаг 4: Переход в корзину
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

    # Шаг 5: Нажать Checkout
    driver.find_element(By.ID, "checkout").click()

    # Шаг 6: Заполнение формы
    driver.find_element(By.ID, "first-name").send_keys("Иван")
    driver.find_element(By.ID, "last-name").send_keys("Петров")
    driver.find_element(By.ID, "postal-code").send_keys("123456")
    driver.find_element(By.ID, "continue").click()

    # Шаг 7: Прочитать итоговую стоимость
    total_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    total_text = total_element.text
    total_value = total_text.split("$")[-1]

    # Шаг 8: Проверка итоговой суммы
    assert total_value == "58.29", f"Expected total to be $58.29, but got ${total_value}"

    print("Тест успешен!")