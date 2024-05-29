from locators.locators import RegistrationPageLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_successful_registration(driver):
    driver.get(BASE_URL + "register")
    driver.find_element(*RegistrationPageLocators.USERNAME_INPUT).send_keys("Test User")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("test_user_1999@yandex.ru")
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("securepassword")
    driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()
    assert "Личный кабинет" in driver.page_source

def test_invalid_password_registration(driver):
    driver.get(BASE_URL + "register")
    driver.find_element(*RegistrationPageLocators.USERNAME_INPUT).send_keys("Test User")
    driver.find_element(*RegistrationPageLocators.EMAIL_INPUT).send_keys("test_user_1999@yandex.ru")
    driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT).send_keys("short")
    driver.find_element(*RegistrationPageLocators.SUBMIT_BUTTON).click()
    assert "Некорректный пароль" in driver.page_source
