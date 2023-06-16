import pytest
# from selenium.webdriver.chrome.webdriver import WebDriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver


# from webdriver_manager.core.utils import ChromeType


@pytest.fixture
def browser_chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture
def open_page(browser_chrome):
    browser_chrome.get("https://5element.by/")
