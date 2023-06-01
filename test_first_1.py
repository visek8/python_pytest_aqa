import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType


def test_deleviry(browser_chrome):
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver.get('https://www.21vek.by/')
    driver.fullscreen_window()

    footer_xpath = (By.XPATH, '//*[@id="footer-inner"]/div/div/div[1]/div[1]/div[2]/a')
    footer_locator = driver.find_element(*footer_xpath)

    driver.execute_script("arguments[0].scrollIntoView();", footer_locator)
    footer_locator.click()

    current_url = driver.current_url
    assert current_url == 'https://www.21vek.by/services/delivery.html'

    driver.close()
    driver.quit()

    # browser_chrome.execute_script("document.getElementById('modal-cookie').style.display = 'none'")
    # footer_xpath = (By.XPATH, '//*[@id="footer-inner"]/div/div/div[1]/div[1]/div[2]/a')
    # footer_locator = browser_chrome.find_element(*footer_xpath)
    # browser_chrome.execute_script("arguments[0].scrollIntoView();", footer_locator)
    # footer_locator.click()
    #
    # current_url = browser_chrome.current_url
    # assert current_url == 'https://www.21vek.by/services/delivery.html'


def test_check_find_elements():
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    driver.implicitly_wait(5)
    driver.get(
        'https://teachmeskills.by/kursy-programmirovaniya/qa-avtomatizirovannoe-testirovanie-na-python-online')

    driver.maximize_window()

    time.sleep(5)
    selector = driver.find_element(By.XPATH, '//*[@id="nav131755476"]/div/div[4]/div/div[2]/div/div[3]')
    driver.execute_script("arguments[0].scrollIntoView();", selector)

    assert selector.is_displayed()

    driver.close()
    driver.quit()

