import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from locators import MainPageLocators as Main
from locators import AccountPageLocators as Account
from locators import LoginPageLocators as Login
from locators import RegistrationPageLocators as Reg
from utils.generators import generate_email, generate_password


def create_and_login(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Reg.NAME_INPUT).send_keys("Тест")
    driver.find_element(*Reg.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Reg.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Reg.REGISTER_BUTTON).click()
    time.sleep(2)

    driver.find_element(*Login.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Login.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Login.LOGIN_SUBMIT).click()
    time.sleep(2)


def test_logout_from_account():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        email = generate_email()
        password = generate_password()
        create_and_login(driver, email, password)

        driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).click()
        time.sleep(1)

        driver.find_element(*Account.LOGOUT_BUTTON).click()
        time.sleep(2)

        assert driver.find_element(By.XPATH, "//h2[text()='Вход']").is_displayed(), "Не произошло выхода из аккаунта"

    finally:
        driver.quit()