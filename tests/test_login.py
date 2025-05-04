from selenium.webdriver.common.by import By

from locators import MainPageLocators as Main
from utils.generators import generate_email, generate_password
from conftest import create_user, login
def test_login_from_main_page(driver):
    email = generate_email()
    password = generate_password()
    create_user(driver, email, password)

    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*Main.LOGIN_BUTTON).click()

    login(driver, email, password)

    assert driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).is_displayed(), "Не удалось войти с главной страницы"

def test_login_from_personal_account_button(driver):
    email = generate_email()
    password = generate_password()
    create_user(driver, email, password)

    driver.get("https://stellarburgers.nomoreparties.site/")
    driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).click()

    login(driver, email, password)

    assert driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).is_displayed(), "Не удалось войти через Личный кабинет"

def test_login_from_registration_page(driver):
    email = generate_email()
    password = generate_password()
    create_user(driver, email, password)

    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(By.LINK_TEXT, "Войти").click()

    login(driver, email, password)

    assert driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).is_displayed(), "Не удалось войти со страницы регистрации"

def test_login_from_forgot_password_page(driver):
    email = generate_email()
    password = generate_password()
    create_user(driver, email, password)

    driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
    driver.find_element(By.LINK_TEXT, "Войти").click()

    login(driver, email, password)

    assert driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).is_displayed(), "Не удалось войти со страницы восстановления пароля"