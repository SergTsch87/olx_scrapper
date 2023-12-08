#!usr/bin/env

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv

# Завантажуємо значення констант з файлу ".env"
load_dotenv()
EMAIL = os.environ.get('EMAIL')
PASSWORD = os.environ.get('PASSWORD')


def login_to_olx(driver):
    # -------------------------------
    # Логінимось на Olx.ua

    base_url = "https://www.olx.ua/uk/"
    driver = webdriver.Chrome()
    driver.get(base_url)

    # Чекаємо на появу блоку "Розділи на сервісі OLX"
    link_your_profile = WebDriverWait(driver, 40).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div/div/h2"))
    )

    time.sleep(1)
    # Розгортаємо вікно браузера на повну
    driver.maximize_window()
    time.sleep(2)

    # Натискаємо на кнопку "Ваш профіль"
    link_your_profile = driver.find_element(By.CSS_SELECTOR, "a.css-12l1k7f")
    link_your_profile.click()

# =====================================
    # Чекаємо на появу поля email
    input_type_email = WebDriverWait(driver, 40).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div/div/div/div/main/div/div[3]/div/form/div[1]/div/div/input"))
    )

    # Вводимо email до поля input
    input_type_email.send_keys(EMAIL)

    # Вводимо password до поля input
    input_type_password = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/main/div/div[3]/div/form/div[2]/div/div/div/input")
    input_type_password.send_keys(PASSWORD)

    # Натискаємо на кнопку "Увійти":
    btn_next = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/main/div/div[3]/div/form/button[2]')
    btn_next.click()


def get_data_with_page(driver, base_url):
    driver.get(base_url)

    # Close pan cookies
    wait_cookies = WebDriverWait(driver, 40)
    wait_cookies.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.css-1lla6pe button'))
    ).click()

    time.sleep(5)
    driver.maximize_window()

    driver.execute_script("window.scrollBy({top: 400, left: 0, behavior: 'smooth'})")
    time.sleep(5)

    # # Очікуємо, доки кнопка, яка викликає номер телефону, стане видимою та клікабельною
    phone_button = WebDriverWait(driver, 30).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]/button[2]"))
    )

    time.sleep(5)
    # Натискаємо на цю кнопку
    phone_button.click()

    # Очікуємо, доки номер телефону стане видимим
    phone_element = WebDriverWait(driver, 30).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div[2]/div[3]/div[2]/div[1]/div[5]/div[1]/button[2]/span/a"))
    )

    data_from_page = {'phone_number': phone_element.text}
    return data_from_page


def main():
    driver = webdriver.Chrome()
    
    login_to_olx(driver)
    
    url = "https://www.olx.ua/d/uk/obyavlenie/gladilka-nerzhavyucha-gladka-z-plastikovoyu-ruchkoyu-dnipro-m-120h280-mm-IDSAHjw.html"
    data_from_page = get_data_with_page(driver, url)
    print(data_from_page)

    driver.quit()


if __name__ == '__main__':
    main()