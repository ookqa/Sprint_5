# UI-тесты для сервиса Stellar Burgers

Тесты реализованы с использованием **Selenium** и проверяют функциональность сервиса.
Тесты хранятся в директории `/tests`.

Тесты используют фикстуры из `conftest.py`

Локаторы описаны в файле `locators.py`

Креды тестового пользователя лежат в `data.py`

Для проверки кейсов с регистрацией в сервисе используется функция генерации адресов электронной почты, импортируется из `helpers.py`

### Как запустить тесты:

```
pytest -v tests.py
```

### Список тестов по функциональности:

- `test_register.py` - проверка регистрации в сервисе, в том числе отображение ошибки при некорректном пароле 
- `test_login.py` - проверки залогинивания в сервисе, в том числе переход к странице входа из разных мест внутри сервиса
- `test_navigation.py` - проверки навигации переходов в личный кабинет и к Конструктору
- `test_logout.py` - проверка выхода из аккаунта
- `test_constructor_section.py`- проверки перехода к разделам в Конструкторе 