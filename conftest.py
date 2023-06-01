import pytest
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from webdriver_manager.core.utils import ChromeType

@pytest.fixture(autouse=False)
def browser_chrome():
    print("-------")
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()

    print("+++++++++")