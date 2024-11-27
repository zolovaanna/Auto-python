import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage  # Импортируем класс страницы


@pytest.fixture(scope="module")
def driver():
    # Запуск Chrome-драйвера с использованием ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calculator(driver):
    # Создаем объект страницы
    calculator_page = CalculatorPage(driver)

    # Открыть страницу калькулятора
    calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Установить задержку
    calculator_page.set_delay(45)

    # Выполнить вычисления
    calculator_page.calculate_sum()

    # Получить результат и проверить его
    result_text = calculator_page.get_result()
    print(f"Результат вычислений: {result_text}")

    # Проверка результата
    assert result_text == "15", f"Expected result to be '15', but got '{result_text}'."