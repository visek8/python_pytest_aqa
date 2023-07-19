import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver

from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture(autouse=False)
def browser_chrome():
    print("-------")
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()

    print("+++++++++")


@pytest.fixture(autouse=False)
def browser_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()