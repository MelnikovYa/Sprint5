from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import RegistrationPageLocators as Reg
from utils.generators import generate_email, generate_password

def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    email = generate_email()
    password = generate_password()
    driver.find_element(*Reg.NAME_INPUT).send_keys("Тест")
    driver.find_element(*Reg.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Reg.PASSWORD_INPUT).send_keys(password)

    driver.find_element(*Reg.REGISTER_BUTTON).click()

    wait = WebDriverWait(driver, 10)
    login_header = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']")))
    assert login_header.is_displayed(), "Не открылась страница входа после регистрации"

def test_registration_with_short_password(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    email = generate_email()
    short_password = "123"

    driver.find_element(*Reg.NAME_INPUT).send_keys("Тест")
    driver.find_element(*Reg.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Reg.PASSWORD_INPUT).send_keys(short_password)
    driver.find_element(*Reg.REGISTER_BUTTON).click()

    wait = WebDriverWait(driver, 10)
    error_text = wait.until(EC.visibility_of_element_located(Reg.ERROR_TEXT)).text
    assert "Некорректный пароль" in error_text, "Ошибка не отобразилась или текст другой"