import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FormPage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открытие страницы формы по URL {url}')
    def open(self, url: str) -> None:
        self.driver.get(url)

    @allure.step('Заполнение формы данными: {first_name} {last_name}, {email}, {phone}, {zip_code}')
    def fill_form(
            self,
            first_name: str, last_name: str, address: str, email: str, phone: str,
            zip_code: str, city: str, country: str, job_position: str, company: str
    ) -> None:
        self.driver.find_element(By.CSS_SELECTOR, "input[name='first-name']").send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='last-name']").send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='address']").send_keys(address)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='e-mail']"))
        )
        self.driver.find_element(By.CSS_SELECTOR, "input[name='e-mail']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='phone']").send_keys(phone)
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='zip-code']"))
        )
        self.driver.find_element(By.CSS_SELECTOR, "input[name='zip-code']").send_keys(zip_code)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='city']").send_keys(city)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='country']").send_keys(country)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='job-position']").send_keys(job_position)
        self.driver.find_element(By.CSS_SELECTOR, "input[name='company']").send_keys(company)

    @allure.step('Отправка формы')
    def submit_form(self) -> None:
        submit_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
        )
        submit_button.click()

    @allure.step('Ожидание появления всех предупреждений на странице')
    def wait_for_alerts(self) -> None:
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".alert"))
        )

    @allure.step('Проверка всех предупреждений на странице')
    def check_alerts(self, alerts: list) -> None:
        for alert in alerts:
            if "alert-danger" in alert.get_attribute("class"):
                assert alert.is_displayed(), "Поле Zip code не подсвечено красным."
            elif "alert-success" in alert.get_attribute("class"):
                assert alert.is_displayed(), "Не все поля подсвечены зелёным."

    @allure.step('Получение всех предупреждений на странице')
    def get_alerts(self):
        return self.driver.find_elements(By.CSS_SELECTOR, ".alert")