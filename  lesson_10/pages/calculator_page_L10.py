import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы калькулятора по URL {url}')
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step('Установка задержки на {delay} секунд')
    def set_delay(self, delay: int) -> None:
        delay_input = self.driver.find_element(By.CSS_SELECTOR, "input[value='5']")
        delay_input.clear()
        delay_input.send_keys(str(delay))

    @allure.step('Выполнение вычислений: 7 + 8')
    def calculate_sum(self) -> None:
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(1)").click()  # Кнопка 7
        self.driver.find_element(By.CSS_SELECTOR, ".operator.btn.btn-outline-success").click()  # Кнопка +
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-primary:nth-child(2)").click()  # Кнопка 8
        self.driver.find_element(By.CSS_SELECTOR, ".btn.btn-outline-warning").click()  # Кнопка =

    @allure.step('Получение результата вычислений')
    def get_result(self) -> str:
        WebDriverWait(self.driver, 60).until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
        )
        return self.driver.find_element(By.CSS_SELECTOR, ".screen").text