from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import ConstructorLocators


class TestConstructorSection:

    def test_constructor_section_bun_tab_select_tab_selected(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*ConstructorLocators.TOPPINGS_TAB).click()
        driver.find_element(*ConstructorLocators.BUN_TAB).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.BUN_SECTION_TITLE))
        assert driver.find_element(*ConstructorLocators.CURRENT_TAB).text == 'Булки'

    def test_constructor_section_sauce_tab_select_tab_selected(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*ConstructorLocators.SAUCE_TAB).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.SAUCE_SECTION_TITLE))
        assert driver.find_element(*ConstructorLocators.CURRENT_TAB).text == 'Соусы'

    def test_constructor_section_toppings_tab_select_tab_selected(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*ConstructorLocators.TOPPINGS_TAB).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ConstructorLocators.TOPPINGS_SECTION_TITLE))
        assert driver.find_element(*ConstructorLocators.CURRENT_TAB).text == 'Начинки'
