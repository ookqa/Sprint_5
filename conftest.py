import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def driver():
    chrome_options = Options()
    chrome_options.add_argument("--window-size=1366,768")
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()
