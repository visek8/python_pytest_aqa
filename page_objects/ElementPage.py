from page_objects import BasePage24


class ElementPage(BasePage24):
    def __init__(self, driver):
        super().__init__(driver)
        self.LOGO = '//*[@class="h-logo"]'
        self.GEO = '//*[@class="h-drop__head"]'
        self.NEW = '//*/div[3]/div/div[1]/div[1]/div[1]'
        self.KITCHEN = '//*[@id="swiper-wrapper-171f859bbeadc128"]'
        self.SEARCH = '//form[2]/input[2]'

    def click_on_element_new(self):
        self.click(self.NEW)

    def click_on_element_kitchen(self):
        self.click(self.KITCHEN)

    def assert_that_logo_visible(self):
        assert self.get_locator_by_xpath(self.LOGO)

    def assert_that_geo_visible(self):
        assert self.get_locator_by_xpath(self.GEO)
