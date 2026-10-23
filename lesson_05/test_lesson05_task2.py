from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_form_submission():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    start_url = "https://httpbin.qa-territory.online/forms/post"

    try:
        driver.get(start_url)

        wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

        custname_field = wait.until(
            EC.visibility_of_element_located((By.NAME, "custname"))
        )
        custname_field.clear()
        custname_field.send_keys("Alice")

        submit_button = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, '//button[normalize-space()="Submit order"]')
            )
        )
        submit_button.click()

        wait.until(lambda d: d.current_url != start_url)

        assert driver.current_url != start_url, (
            f"Ожидалось изменение URL после отправки формы, "
            f"но остался тот же: {driver.current_url}"
        )
    finally:

        driver.quit()
