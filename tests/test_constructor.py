import pytest
from locators.locators import ConstructorLocators
from data import BASE_URL

@pytest.mark.usefixtures("driver")
class TestConstructor:

    def test_navigate_to_buns_section(self, driver):
        driver.get(BASE_URL + "constructor")
        driver.find_element(*ConstructorLocators.BUNS_SECTION).click()
        assert driver.find_element(*ConstructorLocators.SECTION_TITLE).text == "Булки"

    def test_navigate_to_sauces_section(self, driver):
        driver.get(BASE_URL + "constructor")
        driver.find_element(*ConstructorLocators.SAUCES_SECTION).click()
        assert driver.find_element(*ConstructorLocators.SECTION_TITLE).text == "Соусы"

    def test_navigate_to_fillings_section(self, driver):
        driver.get(BASE_URL + "constructor")
        driver.find_element(*ConstructorLocators.FILLINGS_SECTION).click()
        assert driver.find_element(*ConstructorLocators.SECTION_TITLE).text == "Начинки"

