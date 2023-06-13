from page_objects.ElementPage import ElementPage


def test_logo(browser_chrome, open_page):
    element = ElementPage(browser_chrome)

    element.assert_that_geo_visible()
    element.assert_that_logo_visible()
