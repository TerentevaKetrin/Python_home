from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def test_navigation():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    start_url = "https://httpbin.qa-territory.online"

    try:
        driver.get(start_url)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        # Ищем ссылку по точному тексту "HTML Form"
        html_form_link = wait.until(
            EC.element_to_be_clickable((By.LINK_TEXT, "HTML Form"))
        )
        html_form_link.click()

        wait.until(EC.url_contains("/forms/post"))
        assert driver.current_url.endswith(
            "/forms/post"
        ), f"Ожидался URL с /forms/post, но получен: {driver.current_url}"

        driver.back()
        time.sleep(2)

        wait.until(EC.url_contains("httpbin.qa-territory.online"))
        assert driver.current_url.startswith(start_url), (
            f"Ожидался URL, начинающийся с {start_url}, "
            f"но получен: {driver.current_url}"
        )
    finally:
        driver.quit()
