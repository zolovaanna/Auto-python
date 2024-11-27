from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager  # Подключаем менеджер драйвера

# Запуск Chrome-драйвера с использованием Service и ChromeDriverManager
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Открыть сайт
driver.get("http://uitestingplayground.com/textinput")

# Написать в поисковую строку текст SkyPro
input_field = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, '#newButtonName')))
input_field.send_keys("SkyPro")

# Нажать на кнопку
search_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#updatingButton')))
search_button.click()

# Проверяем, что кнопка переименовалась
try:
    # Увеличиваем время ожидания до 15 секунд
    WebDriverWait(driver, 15).until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#updatingButton'), "SkyPro"))
    print("Кнопка была переименована успешно.")
except TimeoutException:
    print("Кнопка не была переименована.")

# Закрыть веб-драйвер
driver.quit()
