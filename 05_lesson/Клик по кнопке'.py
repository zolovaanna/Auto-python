from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Путь к chromedriver
service = Service(executable_path=r'/Users/anna/Desktop/хромдрайвер/chromedriver')

# Запуск веб-драйвера без дополнительных опций
driver = webdriver.Chrome(service=service)

# Открытие страницы
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

# Клик по кнопке "Add Element" 5 раз
add_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Add Element']"))
)

for _ in range(5):
    add_button.click()

# Явное ожидание, пока не появятся кнопки "Delete"
WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CLASS_NAME, "added-manually"))
)

# Сбор списка кнопок "Delete"
delete_buttons = driver.find_elements(By.CLASS_NAME, "added-manually")

# Вывод размера списка
print(f"Количество кнопок 'Delete': {len(delete_buttons)}")

# Закрытие браузера
driver.quit()