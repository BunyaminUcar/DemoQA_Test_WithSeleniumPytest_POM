from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self, driver):
        self.driver = driver
    MENU_ITEMS = (By.XPATH, "//div/h5")
    HEADER_TITLE = (By.XPATH, "//div[@class='main-header']")
    
    def get_menu_items(self):
        items=self.driver.find_elements(*HomePage.MENU_ITEMS)
        menuler=[]
        for _ in items:
            menuler.append(_.text)      
        return menuler
    
    def click_menu_item(self):
        self.driver.find_element(*HomePage.MENU_ITEMS).click()
        
    def get_title(self):
        return self.driver.find_element(*HomePage.HEADER_TITLE).text
        
    