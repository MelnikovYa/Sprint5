import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators as Main
from locators import LoginPageLocators as Login
from locators import RegistrationPageLocators as Reg
from utils.generators import generate_email, generate_password


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
    yield driver
    driver.quit()
@pytest.fixture
def registered_user(driver):
    email = generate_email()
    password = generate_password()

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

    return email, password

def create_user(driver, email, password):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    driver.find_element(*Reg.NAME_INPUT).send_keys("Тест")
    driver.find_element(*Reg.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Reg.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Reg.REGISTER_BUTTON).click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(Main.PERSONAL_ACCOUNT_BUTTON))

def login(driver, email, password):
    driver.find_element(*Login.EMAIL_INPUT).send_keys(email)
    driver.find_element(*Login.PASSWORD_INPUT).send_keys(password)
    driver.find_element(*Login.LOGIN_SUBMIT).click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located(Main.PERSONAL_ACCOUNT_BUTTON))