import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import RegisterPageLocators
from locators import LoginPageLocators
from helpers import generate_email
from data import Data


class TestRegister:

    def test_register_valid_data_register(self, driver):
        email = generate_email()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(Data.TEST_USER_NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(Data.TEST_USER_PASSWORD)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(LoginPageLocators.LOGIN_TITLE))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'

    @pytest.mark.parametrize("password", ["1", "12", "123", "1234", "12345"])
    def test_register_invalid_pass_len_error_msg(self, driver, password):
        email = generate_email()
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*RegisterPageLocators.NAME_INPUT).send_keys(Data.TEST_USER_NAME)
        driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(RegisterPageLocators.BAD_PASSWORD_MSG))
