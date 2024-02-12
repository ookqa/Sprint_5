from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators
from locators import MainPageLocators
from locators import ProfilePageLocators
from data import Data


class TestLogout:
    def test_logout_logout_button_login_page(self, driver):
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE))
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(Data.TEST_USER_EMAIL)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(Data.TEST_USER_PASSWORD)
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(ProfilePageLocators.ABOUT))
        driver.find_element(*ProfilePageLocators.LOGOUT_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'
