from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_dynamic_loading():
    """Клик и проверка 'Hello World!'"""
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)

    try:
        driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

        start_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#start button"))
        )
        start_button.click()

        hello_element = wait.until(
            EC.visibility_of_element_located((By.ID, "finish"))
        )

        driver.save_screenshot("screenshot_task1.png")

        assert hello_element.text == "Hello World!", (
            "Ожидался текст 'Hello World!', "
            f"но получен: '{hello_element.text}'"
        )
    finally:
        driver.quit()
