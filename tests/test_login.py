from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import LoginPageLocators
from locators import MainPageLocators
from locators import RegisterPageLocators


class TestLogin:

    def test_login_header_button_valid_date_login(self, driver):
        email = 'ookqatest10@gmail.com'
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*MainPageLocators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 3)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('s121212')
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        order_button = driver.find_element(*MainPageLocators.ORDER_BUTTON)
        assert order_button.is_displayed()
        driver.quit()

    def test_login_login_button_valid_date_login(self, driver):
        email = 'ookqatest10@gmail.com'
        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(*MainPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('s121212')
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        order_button = driver.find_element(*MainPageLocators.ORDER_BUTTON)
        assert order_button.is_displayed()
        driver.quit()

    def test_login_reg_page_login_link_valid_date_login(self, driver):
        email = 'ookqatest10@gmail.com'
        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(*RegisterPageLocators.LOGIN_LINK).click()
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('s121212')
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        order_button = driver.find_element(*MainPageLocators.ORDER_BUTTON)
        assert order_button.is_displayed()
        driver.quit()

    def test_login_passreset_page_login_link_valid_date_login(self, driver):
        email = 'ookqatest10@gmail.com'
        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.XPATH, "//a[@href='/login']").click()
        WebDriverWait(driver, 3)
        driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(email)
        driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys('s121212')
        driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(MainPageLocators.CONSTRUCTOR_TITLE))
        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/'
        order_button = driver.find_element(*MainPageLocators.ORDER_BUTTON)
        assert order_button.is_displayed()
        driver.quit()
