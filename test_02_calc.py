import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def test_calculator():
  
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 50) 

    try:
        
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

        
        delay_input = driver.find_element(By.ID, "delay")
        delay_input.clear()
        delay_input.send_keys("45")

        
        buttons = ["7", "+", "8", "="]
        for btn_text in buttons:
            btn = driver.find_element(By.XPATH, f"//span[text()='{btn_text}']")
            btn.click()

        
        result_element = wait.until(
            EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
        )
        result = driver.find_element(By.CLASS_NAME, "screen").text
        assert result == "15", f"Expected result 15, but got {result}"

    finally:
        driver.quit()