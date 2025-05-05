from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import ConstructorPageLocators as Constructor

def test_constructor_sauces_tab(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

    driver.find_element(*Constructor.SAUCES_TAB).click()
    active_tab = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span"))
    )
    assert active_tab.text == "Соусы", "Не сработал переход на вкладку 'Соусы'"


def test_constructor_fillings_tab(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']")))

    driver.find_element(*Constructor.FILLINGS_TAB).click()
    active_tab = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span"))
    )
    assert active_tab.text == "Начинки", "Не сработал переход на вкладку 'Начинки'"


def test_constructor_buns_tab(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
    )

    buns_tab = driver.find_element(*Constructor.BUNS_TAB)
    driver.execute_script("arguments[0].scrollIntoView(true);", buns_tab)
    driver.execute_script("arguments[0].click();", buns_tab)

    active_tab = WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span"))
    )
    assert active_tab.text == "Булки", "Не сработал переход на вкладку 'Булки'"