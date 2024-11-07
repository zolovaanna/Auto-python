from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager  # Подключаем менеджер драйвера

# Настройка опций Firefox (без указания пути к Firefox)
options = Options()

# Запуск Firefox-драйвера с использованием Service и GeckoDriverManager
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

try:
    # Шаг 1: Открытие страницы
    driver.get("http://the-internet.herokuapp.com/login")

    # Шаг 2: Ввод значения в поле username
    username_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_field.send_keys("tomsmith")

    # Шаг 3: Ввод значения в поле password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "password"))
    )
    password_field.send_keys("SuperSecretPassword!")

    # Шаг 4: Нажатие на кнопку Login
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']"))
    )
    login_button.click()

    print("Авторизация выполнена успешно.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()