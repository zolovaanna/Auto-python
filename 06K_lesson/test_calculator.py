import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # Подключаем менеджер драйвера


@pytest.fixture(scope="module")
def driver():
    # Запуск Chrome-драйвера с использованием ChromeDriverManager
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


def test_calculator(driver):
    # Открыть страницу
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    # Найти и очистить поле ввода, затем установить значение задержки в 45 секунд
    delay_input = driver.find_element(By.CSS_SELECTOR, "input[value='5']")
    delay_input.clear()
    delay_input.send_keys("45")

    # Нажать на кнопки 7, +, 8 и =
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(1)").click()  # Кнопка 7
    driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()  # Кнопка +
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(2)").click()  # Кнопка 8
    driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()  # Кнопка =

    # Ожидание появления результата "15" в течение 60 секунд
    try:
        # Ожидаем, пока в элементе с классом .screen не появится текст "15"
        WebDriverWait(driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )

        # Получаем текст из элемента
        result_text = driver.find_element(By.CSS_SELECTOR, ".screen").text
        print(f"Результат вычислений: {result_text}")  # Вывод результата на экран

        # Проверка результата
        assert result_text == "15", f"Expected result to be '15', but got '{result_text}'."
        print("Тест прошел успешно!")
    except Exception as e:
        print("Ошибка при ожидании результата:", str(e))
        assert False  # Помечаем тест как неуспешный в случае ошибки