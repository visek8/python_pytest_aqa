from selenium import webdriver
from selenium.webdriver.common.by import By


def test_delivery():
    driver = webdriver.Chrome(executable_path='C:/Users/vika8/python_pytest_aqa/chromedriver')
    driver.fullscreen_window()

    driver.get('https://www.21vek.by/')

    footer_xpath = (By.XPATH, '//*[@id="footer-inner"]/div/div/div[1]/div[1]/div[2]/a')
    footer_locator = driver.find_element(*footer_xpath)

    driver.execute_script("arguments[0].scrollIntoView();", footer_locator)

    footer_locator.click()

    current_url = driver.current_url
    assert current_url != 'https://www.21vek.by/services/delivery.html'
