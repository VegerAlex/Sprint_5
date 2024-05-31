import pytest
from locators.locators import NavigationLocators
from data import BASE_URL

@pytest.mark.usefixtures("driver")
class TestNavigation:

    def test_personal_account_access(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*NavigationLocators.ACCOUNT_BUTTON).click()
        assert "Личный кабинет" in driver.page_source

    def test_navigate_to_constructor_from_account(self, driver):
        driver.get(BASE_URL + "account")
        driver.find_element(*NavigationLocators.CONSTRUCTOR_LINK).click()
        assert "Конструктор" in driver.page_source

    def test_navigate_to_constructor_from_logo(self, driver):
        driver.get(BASE_URL)
        driver.find_element(*NavigationLocators.LOGO_LINK).click()
        assert "Конструктор" in driver.page_source


