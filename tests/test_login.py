import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from locators import MainPageLocators as Main
from locators import LoginPageLocators as Login
from locators import RegistrationPageLocators as Reg
from utils.generators import generate_email, generate_password


def create_user(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Reg.NAME_INPUT).send_keys("Тест")
    driver.find_element(*Reg.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Reg.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Reg.REGISTER_BUTTON).click()
    time.sleep(2)


def login(driver, email, password):
    driver.find_element(*Login.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Login.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Login.LOGIN_SUBMIT).click()
    time.sleep(2)

def test_login_from_main_page():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        email = generate_email()
        password = generate_password()
        create_user(driver, email, password)

        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Main.LOGIN_BUTTON).click()

        login(driver, email, password)

        assert driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).is_displayed(), "Не удалось войти с главной страницы"

    finally:
        driver.quit()


def test_login_from_personal_account_button():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        email = generate_email()
        password = generate_password()
        create_user(driver, email, password)

        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).click()

        login(driver, email, password)

        assert driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).is_displayed(), "Не удалось войти через Личный кабинет"

    finally:
        driver.quit()


def test_login_from_registration_page():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        email = generate_email()
        password = generate_password()
        create_user(driver, email, password)

        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.LINK_TEXT, "Войти").click()

        login(driver, email, password)

        assert driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).is_displayed(), "Не удалось войти со страницы регистрации"

    finally:
        driver.quit()


def test_login_from_forgot_password_page():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        email = generate_email()
        password = generate_password()
        create_user(driver, email, password)

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.LINK_TEXT, "Войти").click()

        login(driver, email, password)

        assert driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).is_displayed(), "Не удалось войти со страницы восстановления пароля"

    finally:
        driver.quit()