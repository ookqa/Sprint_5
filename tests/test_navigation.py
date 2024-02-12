from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators
from locators import MainPageLocators
from locators import ProfilePageLocators
from data import Data


class TestNavigation:

    def test_navigation_main_to_profile_page(self, driver):
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
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/account/profile'

    def test_navigation_from_profile_page_constructor_link_constructor(self, driver):
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
        driver.find_element(*MainPageLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'

    def test_navigation_from_profile_page_logo_link_constructor(self, driver):
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
        driver.find_element(*MainPageLocators.HEADER_LOGO_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
