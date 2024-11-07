from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
try:
    driver.get("http://uitestingplayground.com/classattr")
    blue_button = driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary")
    blue_button.click()
    time.sleep(2)
    print("Клик на синюю кнопку выполнен.")
finally:
    driver.quit()
