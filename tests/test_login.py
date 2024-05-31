import pytest
from locators.locators import LoginPageLocators, NavigationLocators
from data import BASE_URL, TEST_USER_EMAIL, TEST_USER_PASSWORD

@pytest.mark.usefixtures("driver")
class TestLogin:

    def test_login_from_main(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*NavigationLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert "Личный кабинет" in driver.page_source

    def test_login_from_account_button(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*NavigationLocators.ACCOUNT_BUTTON).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert "Личный кабинет" in driver.page_source

    def test_login_from_registration_form(self, driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert "Личный кабинет" in driver.page_source

    def test_login_from_password_recovery_form(self, driver):
        driver.get(BASE_URL + "forgot-password")
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(TEST_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(TEST_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        assert "Личный кабинет" in driver.page_source

