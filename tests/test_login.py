from locators.locators import LoginPageLocators, NavigationLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_login_from_main(driver):
    driver.get(BASE_URL)
    driver.find_element(*NavigationLocators.ACCOUNT_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("test_user_1999@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("securepassword")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    assert "Личный кабинет" in driver.page_source

def test_login_from_account_button(driver):
    driver.get(BASE_URL)
    driver.find_element(*NavigationLocators.ACCOUNT_BUTTON).click()
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("test_user_1999@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("securepassword")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    assert "Личный кабинет" in driver.page_source

def test_login_from_registration_form(driver):
    driver.get(BASE_URL + "register")
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("test_user_1999@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("securepassword")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    assert "Личный кабинет" in driver.page_source

def test_login_from_password_recovery_form(driver):
    driver.get(BASE_URL + "forgot-password")
    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys("test_user_1999@yandex.ru")
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys("securepassword")
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    assert "Личный кабинет" in driver.page_source


