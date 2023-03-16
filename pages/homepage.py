from selenium.webdriver.common.by import By

from pages.PageBase import PageBase

class HomePage(PageBase):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    MENU_ITEMS = (By.XPATH, "//div/h5")
    HEADER_TITLE = (By.XPATH, "//div[@class='main-header']")
    
    def get_menu_items(self):
        return self.items_list(HomePage.MENU_ITEMS)
        
       
    
    def click_menu_item(self):
        self.wait_for_element_w(HomePage.MENU_ITEMS).click()
        
    def get_title(self):
        return self.wait_for_element_w(HomePage.HEADER_TITLE).text
        
    