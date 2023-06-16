# from selenium.webdriver.chrome import webdriver
from time import sleep

from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

WAIT_TIME = 10


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_locator_by_css(self, selector):
        # .class_name
        css = (By.CSS_SELECTOR, selector)
        return self.driver.find_element(*css)

    def get_locator_by_xpath(self, selector):
        # div[@class="et_pb_button_wrapper"]
        xpath = (By.XPATH, selector)
        return self.driver.find_element(*xpath)

    def get_locator_by_id(self, selector):
        by_id = (By.ID, selector)
        return self.driver.find_element(*by_id)

    def get_locator_by_class_name(self, selector):
        # class_name
        class_name = (By.CLASS_NAME, selector)
        return self.driver.find_element(*class_name)

    def get_locator_by_contains(self, selector):
        # //div[contains(@class, "et_pb_module")]
        xpath = (By.XPATH, f'//div[contains(@class, "{selector}")]')
        return self.driver.find_element(*xpath)

    def get_locator_by_contains_text(self, text):
        xpath = (By.XPATH, f'//*[contains(text(), "{text}")]')
        return self.driver.find_element(*xpath)

    def get_element(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def assert_that_element_is_selected(self, selector):
        return self.get_locator_by_css(selector).is_selected()

    def wait_for_element(self, selector):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))

    def assert_that_element_is_enabled(self, selector):
        return self.get_locator_by_css(selector).is_enabled()

    def assert_that_element_is_displayed(self, selector):
        return self.get_locator_by_css(selector).is_displayed()

    def assert_element_is_not_displayed(self, xpath):
        try:
            displayed = self.get_locator_by_xpath(xpath).is_displayed()
            assert not displayed, f"Text {xpath} displayed"
        except NoSuchElementException:
            print(f'Failed to find element. XPATH {xpath}')

    def wait_for_visible_by_hard(self, xpath, retry=5):
        # Time consuming method to detect visible element
        element = None
        for _ in range(retry):
            try:
                element = self.get_locator_by_xpath(xpath)
                break
            except WebDriverException:
                print(f'Failed to find element, will try again. XPATH {xpath}')
                sleep(1)  # Is there any way to avoid sleep()?

        assert element, f'Did not find element. XPATH {xpath}'  # Is assert needed here?
        return element

    def assert_that_attribute_present(self, xpath, attribute):
        element = self.wait_for_visible_by_hard(xpath)
        value = element.get_attribute(attribute)
        if value is not None:
            return True
        return False

    def assert_disable_attribute(self, xpath):
        """Check that element is blocked for editing"""
        assert self.assert_that_attribute_present(xpath, 'disabled'), f"Element '{xpath}' doesn't have attr disabled"

    def click(self, locator):
        return self.get_locator_by_xpath(locator).click()
