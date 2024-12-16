import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from lesson10.pages.form_page_L10 import FormPage


@pytest.fixture(scope="module")
def driver():
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@allure.parent_suite("Тесты на сайте с формами")
@allure.suite("Тесты формы")
@allure.epic("Тестирование форм")
@allure.feature("Форма для отправки данных")
@allure.story("Проверка успешной отправки формы")
@allure.title("Проверка отправки формы с валидными данными")
@allure.description("""
Этот тест проверяет:
1. Корректное заполнение всех полей формы.
2. Успешную отправку формы.
3. Проверку отображения предупреждений или сообщений о подтверждении.
""")
@allure.severity(allure.severity_level.CRITICAL)
@allure.label("ID", "FORM-001")
def test_form_submission(driver):
    form_page = FormPage(driver)

    with allure.step("Открываем страницу с формой"):
        form_page.open("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    with allure.step("Заполняем форму валидными данными"):
        form_page.fill_form(
            first_name='Иван',
            last_name='Петров',
            address='Ленина, 55-3',
            email='test@skypro.com',
            phone='+7985899998787',
            zip_code='',
            city='Москва',
            country='Россия',
            job_position='QA',
            company='SkyPro'
        )

    with allure.step("Отправляем форму"):
        form_page.submit_form()

    with allure.step("Проверяем отображение предупреждений или подтверждения"):
        form_page.wait_for_alerts()
        alerts = form_page.get_alerts()
        form_page.check_alerts(alerts)