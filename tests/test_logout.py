import pytest
from locators.locators import NavigationLocators, LoginPageLocators
from data import BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD

@pytest.mark.usefixtures("driver")
class TestLogout:

    def test_logout(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*NavigationLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        driver.find_element(*NavigationLocators.LOGOUT_BUTTON).click()
        assert "Войти" in driver.page_source


