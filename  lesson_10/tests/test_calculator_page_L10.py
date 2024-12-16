import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lesson10.pages.calculator_page_L10 import CalculatorPage


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.parent_suite("Тесты на сайте калькулятора")
@allure.suite("Тесты калькулятора")
@allure.epic("Тестирование калькулятора")
@allure.feature("Функциональность медленного калькулятора")
@allure.story("Проверка вычислений")
@allure.title("Проверка сложения 7 + 8 с задержкой 45 секунд")
@allure.description("""
Этот тест проверяет:
1. Установку задержки выполнения.
2. Выполнение операции сложения чисел 7 и 8.
3. Проверку корректности результата (15).
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("ID", "CALC-001")
def test_calculator(driver):
    calculator_page = CalculatorPage(driver)

    with allure.step("Открыть страницу калькулятора"):
        calculator_page.open("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    with allure.step("Установить задержку"):
        calculator_page.set_delay(45)

    with allure.step("Выполнить вычисления"):
        calculator_page.calculate_sum()

    with allure.step("Получить результат вычислений"):
        result_text = calculator_page.get_result()

    with allure.step("Проверить результат вычислений"):
        assert result_text == "15", f"Expected result to be '15', but got '{result_text}'."