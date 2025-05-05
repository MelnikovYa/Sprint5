from selenium.webdriver.common.by import By

class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка входа на главной
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # кнопка личного кабинета
    STELLAR_LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # логотип в шапке

class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//input[@name='name']")  # поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # поле пароля
    LOGIN_SUBMIT = (By.XPATH, "//button[text()='Войти']")  # кнопка "Войти"

class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")  # поле имя
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")  # поле email
    PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")  # поле пароль
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")  # кнопка регистрации
    ERROR_TEXT = (By.CLASS_NAME, "input__error")  # текст ошибки

class AccountPageLocators:
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка выхода
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # кнопка "Конструктор"

class ConstructorPageLocators:
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']")  # вкладка Булки
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']")  # вкладка Соусы
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']")  # вкладка Начинки