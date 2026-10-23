from selenium import webdriver

GITFLIC_BASE_URL = "https://gitflic.ru"
LOGIN_PATH = "/auth/login"


def test_session_storage_auth():
    """Проверка редиректа при фейковых cookie"""
    driver = webdriver.Chrome()

    try:
        driver.get(GITFLIC_BASE_URL)
        driver.add_cookie(
            {"name": "sessionid", "value": "fake_session_user_1"}
        )
        driver.refresh()
        driver.get(f"{GITFLIC_BASE_URL}/profile/user1")
        url_user1 = driver.current_url

        driver.delete_all_cookies()

        driver.add_cookie(
            {"name": "sessionid", "value": "fake_session_user_2"}
        )
        driver.refresh()
        driver.get(f"{GITFLIC_BASE_URL}/profile/user2")
        url_user2 = driver.current_url

        assert LOGIN_PATH in url_user1, (
            "User1 не был перенаправлен на страницу входа. "
            f"Текущий URL: {url_user1}"
        )
        assert LOGIN_PATH in url_user2, (
            "User2 не был перенаправлен на страницу входа. "
            f"Текущий URL: {url_user2}"
        )
    finally:
        driver.quit()
