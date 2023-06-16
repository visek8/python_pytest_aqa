from hw_24.page_objects.ElementPage import ElementPage


def test_logo(browser_chrome, open_page):
    element = ElementPage(browser_chrome)

    element.assert_that_geo_visible()
    element.assert_that_logo_visible()


def test_click_new(browser_chrome, open_page):
    element = ElementPage(browser_chrome)

    element.click_on_element_new()


def test_click_kitchen(browser_chrome, open_page):
    element = ElementPage(browser_chrome)

    element.click_on_element_kitchen()
