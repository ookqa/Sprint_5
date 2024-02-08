from selenium.webdriver.common.by import By


class MainPageLocators:
    ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']/parent::a")  # кнопка перехода в личный кабинет в хэдере
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//li/a[@href='/']")  # ссылка на Конструктор в хэдере
    CONSTRUCTOR_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")  # заголовок секции Конструктора бургеров
    HEADER_LOGO_BUTTON = (By.XPATH, "//nav/div/a")  # ссылка на главную страницу в лого в хэдере
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # кнопка входа в аккаунт
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка оформления заказа


class ConstructorLocators:
    BUN_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")  # вкладка булок в конструкторе
    SAUCE_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")  # вкладка соуcов в конструкторе
    TOPPINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")  # вкладка начинок в конструкторе


class RegisterPageLocators:
    NAME_INPUT = (By.XPATH, ".//label[text()='Имя']/following-sibling::input")  # поле для ввода имени
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # поле для ввода адреса email
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # поле для ввода пароля
    REGISTER_BUTTON = (By.XPATH, ".//button[text()='Зарегистрироваться']")  # кнопка "Зарегистрироваться"
    LOGIN_LINK = (By.XPATH, "//a[@href='/login']")  # ссылка для входя для уже зарегистрированных пользователей
    BAD_PASSWORD_MSG = (By.XPATH, "//p[text()='Некорректный пароль']")  # сообщение о некорректном пароле


class LoginPageLocators:
    LOGIN_TITLE = (By.XPATH, "//h2[text()='Вход']")  # заголовок формы входа
    REGISTER_LINK = (By.XPATH, "//a[@href='/register']")  # ссылка для перехода к странице регистрации
    EMAIL_INPUT = (By.XPATH, ".//label[text()='Email']/following-sibling::input")  # поле для ввода адреса email
    PASSWORD_INPUT = (By.XPATH, ".//label[text()='Пароль']/following-sibling::input")  # поле для ввода пароля
    LOGIN_BUTTON = (By.XPATH, ".//button[text()='Войти']")  # кнопка "Войти"


class ProfilePageLocators:
    ABOUT = (By.XPATH, "//p[text()='В этом разделе вы можете изменить свои персональные данные']")  # сообщение с описанием раздела
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")  # кнопка "Выход"
