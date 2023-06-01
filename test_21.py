# import time
from selenium.webdriver import ActionChains

from selenium.webdriver.common.by import By


def test_submit(browser_chrome):
    browser_chrome.get('https://demoqa.com/text-box')

    submit_xpath = (By.XPATH, '//*[@id="userForm"]/div[5]/div')
    submit_locator = browser_chrome.find_element(*submit_xpath)

    browser_chrome.execute_script("arguments[0].scrollIntoView();", submit_locator)
    submit_locator.click()

    current_url = browser_chrome.current_url
    assert current_url == 'https://demoqa.com/text-box'


def test_check_box(browser_chrome):
    browser_chrome.get('https://demoqa.com/text-box')

    check_xpath = (By.XPATH, '//*[@id="item-1"]')
    check_locator = browser_chrome.find_element(*check_xpath)

    browser_chrome.execute_script("arguments[0].scrollIntoView();", check_locator)

    check_locator.click()

    box_xpath = (By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]')
    box_locator = browser_chrome.find_element(*box_xpath)

    browser_chrome.execute_script("arguments[0].scrollIntoView();", box_locator)

    if box_locator.is_selected() == False:
        print('Не отмечен')
    else:
        print('Отмечен')


def test_radio(browser_chrome):
    browser_chrome.get('https://demoqa.com/radio-button')

    radio_xpath = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/div[2]/label')
    radio_locator = browser_chrome.find_element(*radio_xpath)

    browser_chrome.execute_script("arguments[0].scrollIntoView();", radio_locator)

    radio_locator.click()

    text_xpath = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/p')
    text_locator = browser_chrome.find_element(*text_xpath)

    assert text_locator.is_displayed()


def test_double_click(browser_chrome):
    browser_chrome.get('https://demoqa.com/buttons')

    double_xpath = (By.XPATH, '//*[@id="doubleClickBtn"]')
    double_locator = browser_chrome.find_element(*double_xpath)

    browser_chrome.execute_script("arguments[0].scrollIntoView();", double_locator)

    action = ActionChains(browser_chrome)
    action.double_click(double_locator).perform()

    text_double_xpath = (By.XPATH, '//*[@id="doubleClickMessage"]')
    text_double_locator = browser_chrome.find_element(*text_double_xpath)

    assert text_double_locator.is_displayed()


def test_link(browser_chrome):
    browser_chrome.get('https://demoqa.com/broken')

    broke_xpath = (By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div[2]/a[2]')
    broke_locator = browser_chrome.find_element(*broke_xpath)

    browser_chrome.execute_script("arguments[0].scrollIntoView();", broke_locator)

    broke_locator.click()

    link_2_xpath = (By.XPATH, '//*[@id="content"]/div/p/a')
    link_2_locator = browser_chrome.find_element(*link_2_xpath)

    link_2_locator.click()

    link_404_xpath = (By.XPATH, '//*[@id="content"]/div/ul/li[3]/a')
    link_404_locator = browser_chrome.find_element(*link_404_xpath)

    link_404_locator.click()

    status_code_xpath = (By.XPATH, '//*[@id="content"]/div/p')
    status_code_locator = browser_chrome.find_element(*status_code_xpath)

    assert status_code_locator.is_displayed()
