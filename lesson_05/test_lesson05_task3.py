from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_multiple_elements():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    url = "https://httpbin.qa-territory.online/links/10"

    try:
        driver.get(url)
        wait.until(EC.presence_of_element_located((By.TAG_NAME, "a")))

        all_links = driver.find_elements(By.TAG_NAME, "a")

        msg_count = (
            f"Ожидалось 9 ссылок, но найдено: {len(all_links)}"
        )
        assert len(all_links) == 9, msg_count

        for i, link in enumerate(all_links):
            msg_displayed = (
                f"Ссылка №{i + 1} не отображается на странице"
            )
            assert link.is_displayed(), msg_displayed

        first_link = all_links[0]
        msg_first_text = (
            f"Текст первой ссылки должен содержать '1', "
            f"но получен: '{first_link.text}'"
        )
        assert "1" in first_link.text, msg_first_text
    finally:
        driver.quit()
