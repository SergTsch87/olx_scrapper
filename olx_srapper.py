#!usr/bin/env

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from dotenv import load_dotenv


def main():
    driver = webdriver.Chrome()
    
    login_to_olx(driver)
    
    url = "https://www.olx.ua/d/uk/obyavlenie/gladilka-nerzhavyucha-gladka-z-plastikovoyu-ruchkoyu-dnipro-m-120h280-mm-IDSAHjw.html"
    data_from_page = get_data_with_page(driver, url)
    print(data_from_page)

    driver.quit()


if __name__ == '__main__':
    main()