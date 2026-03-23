import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

def test_form_submission():
   
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    driver = webdriver.Edge(options=edge_options)
    wait = WebDriverWait(driver, 10)

    try:
       
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

        
        fields = {
            "first-name": "Иван",
            "last-name": "Петров",
            "address": "Ленина, 55-3",
            "e-mail": "test@skypro.com",
            "phone": "+7985899998787",
            "zip-code": "",  
            "city": "Москва",
            "country": "Россия",
            "job-position": "QA",
            "company": "SkyPro"
        }

        for field_id, value in fields.items():
            input_element = wait.until(EC.presence_of_element_located((By.ID, field_id)))
            input_element.clear()
            if value:
                input_element.send_keys(value)

        
        submit_btn = driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_btn.click()

        
        zip_field = driver.find_element(By.ID, "zip-code")
        zip_class = zip_field.get_attribute("class")
        assert "alert-danger" in zip_class or "is-invalid" in zip_class.lower(), \
            "Zip code field is not highlighted in red"

        
        other_fields = [
            "first-name", "last-name", "address", "e-mail",
            "phone", "city", "country", "job-position", "company"
        ]
        for field_id in other_fields:
            field = driver.find_element(By.ID, field_id)
            field_class = field.get_attribute("class")
            assert "alert-success" in field_class or "is-valid" in field_class.lower(), \
                f"Field {field_id} is not highlighted in green"

    finally:
        driver.quit()