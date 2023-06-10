import time
import requests

from BasePage import BasePage


class TestDynamic:
    def test_dynamic(self, browser_chrome):
        base_page = BasePage(browser_chrome)

        base_page.driver.get('http://the-internet.herokuapp.com/dynamic_controls')

        checkbox = base_page.get_locator_by_css('input[type=checkbox]')
        checkbox.click()

        button = base_page.get_locator_by_xpath('//*[@id="checkbox-example"]/button')
        button.click()

        inscription_1 = base_page.get_locator_by_contains_text("It's gone!")
        browser_chrome.execute_script("arguments[0].scrollIntoView();", inscription_1)

        # тут проверка на то, что чек-бокс не отображается
        base_page.assert_element_is_not_displayed('input[type=checkbox]')

        in_put = base_page.get_locator_by_xpath('//*[@id="input-example"]/input')

        # здесь проверяем, что инпут дизаблед
        base_page.assert_disable_attribute('//*[@id="input-example"]/input')

        button_2 = base_page.get_locator_by_xpath('//*[@id="input-example"]/button')
        button_2.click()

        inscription_2 = base_page.get_locator_by_contains_text("It's enabled!")
        browser_chrome.execute_script("arguments[0].scrollIntoView();", inscription_2)

        # проверить что инпут енаблед
        assert not base_page.assert_disable_attribute('//*[@id="input-example"]/input')


def test_download(browser_chrome):
    response = requests.get('http://the-internet.herokuapp.com/download/download.png', stream=True)

    with open('download.png', 'wb') as image:
        for chunk in response.iter_content(chunk_size=1024):
            image.write(chunk)


def test_unloading(browser_chrome):
    base_page = BasePage(browser_chrome)
    base_page.driver.get('http://the-internet.herokuapp.com/upload')
    file_element = base_page.get_locator_by_css("input[type=file]")
    file_path = "C:/Users/vika8/OneDrive/Изображения/обои/itachi.jpg"
    file_element.send_keys(file_path)
    button = base_page.get_locator_by_xpath('//*[@id="file-submit"]')
    button.click()
    time.sleep(5)
    file_name = 'itachi.jpg'
    first_result = base_page.get_locator_by_xpath("//*[@id='uploaded-files']").get_attribute(
        "innerText")
    assert first_result == file_name
