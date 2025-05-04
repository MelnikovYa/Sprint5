import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from locators import ConstructorPageLocators as Constructor


def test_constructor_tabs_navigation():
    options = Options()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get("https://stellarburgers.nomoreparties.site/")
        time.sleep(2)

        driver.find_element(*Constructor.SAUCES_TAB).click()
        time.sleep(1)
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span")
        assert active_tab.text == "Соусы", "Не сработал переход на вкладку 'Соусы'"

        driver.find_element(*Constructor.FILLINGS_TAB).click()
        time.sleep(1)
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span")
        assert active_tab.text == "Начинки", "Не сработал переход на вкладку 'Начинки'"

        driver.find_element(*Constructor.BUNS_TAB).click()
        time.sleep(1)
        active_tab = driver.find_element(By.XPATH, "//div[contains(@class,'tab_tab_type_current')]/span")
        assert active_tab.text == "Булки", "Не сработал переход на вкладку 'Булки'"

    finally:
        driver.quit()