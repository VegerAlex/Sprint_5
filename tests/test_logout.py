from locators.locators import NavigationLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_logout(driver):
    driver.get(BASE_URL + "account")
    driver.find_element(*NavigationLocators.LOGOUT_BUTTON).click()
    assert "Войти" in driver.page_source

