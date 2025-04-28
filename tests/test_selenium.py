"""Модуль для автоматического решения квадратного уравнения"""
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
from logic import kv_ur

# Инициализация драйвера
driver = webdriver.Chrome()

try:
    # Открываем HTML файл
    html_path = "index.html"
    file_path = os.path.abspath(html_path)
    file_url = f"file:///{file_path}"
    driver.get(file_url)
    # Коэффициенты
    a = 1
    b = -5
    c = 6
    # Вычисляем результат с помощью функции
    result = kv_ur(a, b, c)
    # Заполняем поля
    driver.find_element(By.ID, "a").send_keys(str(a))
    driver.find_element(By.ID, "b").send_keys(str(b))
    driver.find_element(By.ID, "c").send_keys(str(c))
    # Нажимаем кнопку
    driver.find_element(By.TAG_NAME, "button").click()
    # Пауза для просмотра результата
    time.sleep(5)
finally:
    # Закрываем браузер
    driver.quit()
