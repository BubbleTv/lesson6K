import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def test_shop_checkout():
    # Настройка Firefox
    firefox_options = Options()
    firefox_options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=firefox_options)
    wait = WebDriverWait(driver, 10)

    try:
        # 1. Открыть сайт магазина
        driver.get("https://www.saucedemo.com/")

        # 2. Авторизоваться как standard_user
        username = driver.find_element(By.ID, "user-name")
        username.send_keys("standard_user")
        password = driver.find_element(By.ID, "password")
        password.send_keys("secret_sauce")
        login_btn = driver.find_element(By.ID, "login-button")
        login_btn.click()

        # 3. Добавить товары в корзину
        products = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
        }
        for product_name, btn_id in products.items():
            add_btn = wait.until(EC.element_to_be_clickable((By.ID, btn_id)))
            add_btn.click()

        # 4. Перейти в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()

        # 5. Нажать Checkout
        checkout_btn = driver.find_element(By.ID, "checkout")
        checkout_btn.click()

        # 6. Заполнить форму своими данными
        first_name = driver.find_element(By.ID, "first-name")
        first_name.send_keys("Иван")
        last_name = driver.find_element(By.ID, "last-name")
        last_name.send_keys("Петров")
        postal_code = driver.find_element(By.ID, "postal-code")
        postal_code.send_keys("123456")

        # 7. Нажать Continue
        continue_btn = driver.find_element(By.ID, "continue")
        continue_btn.click()

        # 8. Прочитать итоговую стоимость
        total_element = wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
        )
        total_text = total_element.text
        # total_text выглядит как "Total: $58.29"
        total_amount = total_text.split("$")[1]

        # 9. Проверить, что итоговая сумма равна $58.29
        assert total_amount == "58.29", f"Expected total $58.29, but got ${total_amount}"

    finally:
        driver.quit()