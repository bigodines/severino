from pyccuracy.page import Page

class YahooPage(Page):
    url = 'http://www.yahoo.com'

    def register(self):
        self.register_element("search field", "//input[@name='p']")
        self.register_element("search button", "//button[@id='search-submit']")
        
        