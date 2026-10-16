import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="function")
def driver():
    options = Options()
    # Если хочешь видеть браузер во время теста — закомментируй строку ниже:
    options.add_argument("--headless=new")
    options.add_argument("--window-size=1920,1080")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()
