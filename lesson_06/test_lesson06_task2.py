from selenium import webdriver


URL = "https://gitflic.ru"
LOGIN = f"{URL}/auth/login"


def test_session_storage_auth():
    driver = webdriver.Chrome()
    try:
        driver.get(URL)

        driver.add_cookie({"name": "sessionid", "value": "fake1"})
        driver.refresh()
        driver.get(f"{URL}/profile/user1")
        assert driver.current_url == LOGIN

        driver.delete_all_cookies()

        driver.add_cookie({"name": "sessionid", "value": "fake2"})
        driver.refresh()
        driver.get(f"{URL}/profile/user2")
        assert driver.current_url == LOGIN
    finally:
        driver.quit()
