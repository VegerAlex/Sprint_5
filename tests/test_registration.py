import pytest
from locators.locators import RegistrationPageLocators
from data import BASE_URL, INVALID_PASSWORD, NEW_USER_NAME
import random
import string

def generate_random_email():
    return ''.join(random.choices(string.ascii_lowercase, k=10)) + "@yandex.ru"

@pytest.mark.usefixtures("driver")
class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*RegistrationPageLocators.USERNAME_INPUT).send_keys(NEW_USER_NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_random_email())
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("securepassword")
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()
        assert "Личный кабинет" in driver.page_source

    def test_invalid_password_registration(self, driver):
        driver.get(BASE_URL + "register")
        driver.find_element(*RegistrationPageLocators.USERNAME_INPUT).send_keys(NEW_USER_NAME)
        driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys(generate_random_email())
        driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys(INVALID_PASSWORD)
        driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()
        assert "Некорректный пароль" in driver.page_source
