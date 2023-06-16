import time

from BasePage import BasePage


class TestBBC:
    def test_1_css(self, browser_chrome):
        # ищем картинку с новостью
        base_page = BasePage(browser_chrome)
        base_page.driver.get('https://www.bbc.com/')
        first_picture = base_page.get_locator_by_css('.media.media--hero')
        browser_chrome.execute_script("arguments[0].scrollIntoView();", first_picture)

        time.sleep(5)

        browser_chrome.save_screenshot("test_1_css.png")

        assert first_picture

    def test_1_xpath(self, browser_chrome):
        # ищем картинку с новостью
        base_page = BasePage(browser_chrome)
        base_page.driver.get('https://www.bbc.com/')
        first_picture = base_page.get_locator_by_xpath(
            '//div[@class="media media--hero media--primary media--overlay block-link"]')
        browser_chrome.execute_script("arguments[0].scrollIntoView();", first_picture)

        time.sleep(5)

        browser_chrome.save_screenshot("test_1_xpath.png")

        assert first_picture

    def test_2_css(self, browser_chrome):
        # ищем кнопку BBC
        base_page = BasePage(browser_chrome)
        base_page.driver.get('https://www.bbc.com/')
        second_picture = base_page.get_locator_by_css('.orb-nav-section')
        browser_chrome.execute_script("arguments[0].scrollIntoView();", second_picture)

        time.sleep(5)

        browser_chrome.save_screenshot('test_2_css.png')

        assert second_picture

    def test_2_xpath(self, browser_chrome):
        # ищем кнопку BBC
        base_page = BasePage(browser_chrome)
        base_page.driver.get('https://www.bbc.com/')
        second_picture = base_page.get_locator_by_xpath(
            '//*[@class="orb-nav-section orb-nav-blocks"]')
        browser_chrome.execute_script("arguments[0].scrollIntoView();", second_picture)

        time.sleep(5)

        browser_chrome.save_screenshot("test_2_xpath.png")

        assert second_picture

    def test_3_css(self, browser_chrome):
        # ищем кнопку sport
        base_page = BasePage(browser_chrome)
        base_page.driver.get('https://www.bbc.com/')
        third_picture = base_page.get_locator_by_css('.orb-nav-sport')
        browser_chrome.execute_script("arguments[0].scrollIntoView();", third_picture)

        time.sleep(5)

        browser_chrome.save_screenshot('test_3_css.png')

        assert third_picture

    def test_3_xpath(self, browser_chrome):
        # ищем кнопку sport
        base_page = BasePage(browser_chrome)
        base_page.driver.get('https://www.bbc.com/')
        third_picture = base_page.get_locator_by_xpath(
            '//*[@class="orb-nav-sport"]')
        browser_chrome.execute_script("arguments[0].scrollIntoView();", third_picture)

        time.sleep(5)

        browser_chrome.save_screenshot("test_3_xpath.png")

        assert third_picture


class TestTwoMethod:
    def test_checkbox(self, browser_chrome):
        # нажимаем на I have a bike
        base_page = BasePage(browser_chrome)

        base_page.driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')

        checkbox = base_page.get_locator_by_css('input[value=Bike]')
        checkbox.click()
        browser_chrome.save_screenshot("test_checkbox.png")
        assert checkbox.is_selected()

    def test_scroll(self, browser_chrome):
        base_page = BasePage(browser_chrome)
        browser_chrome.maximize_window()

        base_page.driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')
        button = base_page.get_locator_by_contains_text("© NextLevel Solutions USA, LLC")
        browser_chrome.execute_script("arguments[0].scrollIntoView();", button)
        time.sleep(5)

        scroll = base_page.get_locator_by_css('.et-visible')
        browser_chrome.execute_script("arguments[0].scrollIntoView();", scroll)
        scroll.click()

        browser_chrome.save_screenshot("test_scroll.png")
        assert scroll  # при запуске теста видно, что кнопка scroll не появляется

    def test_radio_button(self, browser_chrome):
        # кликаем на Female
        base_page = BasePage(browser_chrome)

        base_page.driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')

        radio_button = base_page.get_locator_by_css('input[value=female]')
        radio_button.click()
        browser_chrome.save_screenshot("test_radio_button.png")
        assert radio_button.is_selected()

    def test_dropdown(self, browser_chrome):
        base_page = BasePage(browser_chrome)

        base_page.driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')

        dropdown = base_page.get_locator_by_css('.et_pb_blurb_description select')
        dropdown.click()

        audi = base_page.get_locator_by_xpath('//select/option[4]')
        audi.click()

        browser_chrome.save_screenshot("dropdown.png")
        assert dropdown

    def test_input_text(self, browser_chrome):
        base_page = BasePage(browser_chrome)
        base_page.driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')

        name = base_page.get_locator_by_id('et_pb_contact_name_0')
        name.send_keys("Vika")

        email = base_page.get_locator_by_id('et_pb_contact_email_0')
        email.send_keys("vika8nask@gmail.com")

        email_me = base_page.get_locator_by_css('.et_contact_bottom_container')
        time.sleep(5)
        email_me.click()

        message = base_page.get_locator_by_contains_text('Thanks for contacting us')
        browser_chrome.execute_script("arguments[0].scrollIntoView();", message)

        browser_chrome.save_screenshot("input_text.png")
        assert email_me

    def test_attribute(self, browser_chrome):
        base_page = BasePage(browser_chrome)
        base_page.driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')

        name = base_page.get_locator_by_xpath('//*[8]/div/div/div/form/input[1]')
        name.get_attribute("attribute name")

        assert name


class TestDifference:

    def test_enabled(self, browser_chrome):
        base_page = BasePage(browser_chrome)

        base_page.driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')

        radio_button = base_page.get_locator_by_css('input[value=female]')
        radio_button.click()
        assert radio_button.is_enabled()

    def test_displayed(self, browser_chrome):
        base_page = BasePage(browser_chrome)

        base_page.driver.get('https://ultimateqa.com/simple-html-elements-for-automation/')

        radio_button = base_page.get_locator_by_css('input[value=female]')
        radio_button.click()
        assert radio_button.is_displayed()
