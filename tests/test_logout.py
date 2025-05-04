from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import MainPageLocators as Main
from locators import AccountPageLocators as Account

def test_logout_from_account(driver, registered_user):
    driver.find_element(*Main.PERSONAL_ACCOUNT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(Account.LOGOUT_BUTTON))

    driver.find_element(*Account.LOGOUT_BUTTON).click()
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h2[text()='Вход']"))
    )

    assert driver.find_element(By.XPATH, "//h2[text()='Вход']").is_displayed(), "Не произошло выхода из аккаунта"