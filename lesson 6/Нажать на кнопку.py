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
driver.get("http://uitestingplayground.com/ajax")

# Нажать на синюю кнопку
button = WebDriverWait(driver, 25).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '#ajaxButton'))
)
button.click()
print("Кнопка нажата, ожидаем появление зелёной плашки.")

# Увеличиваем тайм-аут до 30 секунд для надежности
try:
    # Ожидаем, пока элемент не станет присутствовать в DOM
    WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'p.bg-success'))
    )

    # Теперь проверяем, что элемент видим
    green_text_element = driver.find_element(By.CSS_SELECTOR, 'p.bg-success')
    if green_text_element.is_displayed():
        green_text = green_text_element.text
        print("Зелёная плашка найдена:", green_text)
    else:
        print("Зелёная плашка присутствует в DOM, но она не видна.")

except TimeoutException:
    print("Не удалось найти зелёную плашку в течение времени ожидания.")

# Закрыть браузер
driver.quit()