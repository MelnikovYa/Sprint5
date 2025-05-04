import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators as Main
from locators import AccountPageLocators as Account


def test_go_to_personal_account(driver, registered_user):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(Account.LOGOUT_BUTTON))

    assert driver.find_element(*Account.LOGOUT_BUTTON).is_displayed(), "Не открылась страница личного кабинета"


def test_go_to_constructor_from_account_button(driver, registered_user):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Account.CONSTRUCTOR_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

    assert driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']").is_displayed(), "Не открылась страница конструктора"


def test_go_to_constructor_from_logo(driver, registered_user):
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main.PERSONAL_ACCOUNT_BUTTON)).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Main.STELLAR_LOGO)).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

    assert driver.find_element(By.XPATH, "//h1[text()='Соберите бургер']").is_displayed(), "Переход по логотипу не сработал"
