from locators.locators import NavigationLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_personal_account_access(driver):
    driver.get(BASE_URL)
    driver.find_element(*NavigationLocators.ACCOUNT_BUTTON).click()
    assert "Личный кабинет" in driver.page_source

def test_navigate_to_constructor_from_account(driver):
    driver.get(BASE_URL + "account")
    driver.find_element(*NavigationLocators.CONSTRUCTOR_LINK).click()
    assert "Конструктор" in driver.page_source

def test_navigate_to_constructor_from_logo(driver):
    driver.get(BASE_URL)
    driver.find_element(*NavigationLocators.LOGO_LINK).click()
    assert "Конструктор" in driver.page_source

