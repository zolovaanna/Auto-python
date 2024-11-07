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
    driver.get("http://the-internet.herokuapp.com/inputs")

    # Шаг 2: Явное ожидание, чтобы элемент стал доступен для взаимодействия
    input_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "input"))
    )

    # Ввод текста "1000"
    input_field.send_keys("1000")

    # Очистка поля ввода
    input_field.clear()

    # Ввод текста "999"
    input_field.send_keys("999")

    print("Скрипт выполнен успешно.")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()