from locators.locators import ConstructorLocators

BASE_URL = "https://stellarburgers.nomoreparties.site/"

def test_navigate_to_buns_section(driver):
    driver.get(BASE_URL + "constructor")
    driver.find_element(*ConstructorLocators.BUNS_SECTION).click()
    assert driver.find_element(*ConstructorLocators.SECTION_TITLE).text == "Булки"

def test_navigate_to_sauces_section(driver):
    driver.get(BASE_URL + "constructor")
    driver.find_element(*ConstructorLocators.SAUCES_SECTION).click()
    assert driver.find_element(*ConstructorLocators.SECTION_TITLE).text == "Соусы"

def test_navigate_to_fillings_section(driver):
    driver.get(BASE_URL + "constructor")
    driver.find_element(*ConstructorLocators.FILLINGS_SECTION).click()
    assert driver.find_element(*ConstructorLocators.SECTION_TITLE).text == "Начинки"
