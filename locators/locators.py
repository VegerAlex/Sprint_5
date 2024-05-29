from selenium.webdriver.common.by import By

class LoginPageLocators:
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.NAME, "submit")

class RegistrationPageLocators:
    USERNAME_INPUT = (By.NAME, "name")
    EMAIL_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SUBMIT_BUTTON = (By.NAME, "submit")

class NavigationLocators:
    ACCOUNT_BUTTON = (By.NAME, "account")
    LOGOUT_BUTTON = (By.NAME, "logout")
    LOGO_LINK = (By.CLASS_NAME, "logo")
    CONSTRUCTOR_LINK = (By.LINK_TEXT, "Конструктор")

class ConstructorLocators:
    BUNS_SECTION = (By.XPATH, "//span[text()='Булки']")
    SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']")
    FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']")
    SECTION_TITLE = (By.CLASS_NAME, "section-title")