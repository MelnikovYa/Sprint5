import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from locators import RegistrationPageLocators as Reg
from utils.generators import generate_email, generate_password

def test_successful_registration():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )
    driver.maximize_window()

    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")

        email = generate_email()
        password = generate_password()
        driver.find_element(*Reg.NAME_INPUT).send_keys("Тест")
        driver.find_element(*Reg.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Reg.PASSWORD_INPUT).send_keys(password)

        driver.find_element(*Reg.REGISTER_BUTTON).click()

        time.sleep(2)

        login_header = driver.find_element(By.XPATH, "//h2[text()='Вход']")
        assert login_header.is_displayed(), "Не открылась страница входа после регистрации"

    finally:
        driver.quit()

def test_registration_with_short_password():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    try:
        driver.get("https://stellarburgers.nomoreparties.site/register")

        email = generate_email()
        short_password = "123"

        driver.find_element(*Reg.NAME_INPUT).send_keys("Тест")
        driver.find_element(*Reg.EMAIL_INPUT).send_keys(email)
        driver.find_element(*Reg.PASSWORD_INPUT).send_keys(short_password)
        driver.find_element(*Reg.REGISTER_BUTTON).click()

        time.sleep(1)

        error_text = driver.find_element(*Reg.ERROR_TEXT).text
        assert "Некорректный пароль" in error_text, "Ошибка не отобразилась или текст другой"

    finally:
        driver.quit()