from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from locators import ConstructorLocators


class TestConstructorSection:

    def test_constructor_section_tab_select(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*ConstructorLocators.TOPPINGS_TAB).click()
        WebDriverWait(driver, 3)
        assert driver.find_element(By.XPATH, "//span/parent::div[contains(@class, 'current')]").text == 'Начинки'
        driver.find_element(*ConstructorLocators.SAUCE_TAB).click()
        WebDriverWait(driver, 3)
        assert driver.find_element(By.XPATH, "//span/parent::div[contains(@class, 'current')]").text == 'Соусы'
        driver.find_element(*ConstructorLocators.BUN_TAB).click()
        WebDriverWait(driver, 3)
        assert driver.find_element(By.XPATH, "//span/parent::div[contains(@class, 'current')]").text == 'Булки'
        driver.quit()
