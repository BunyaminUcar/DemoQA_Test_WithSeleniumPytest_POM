from selenium.webdriver.common.by import By

class BookPage():
    def __init__(self, driver):
        self.driver = driver
    
    
    
    SEARCH_BOX=(By.ID,"searchBox")
    SEARCH_BUTTON=(By.ID,"basic-addon2")
    RESULT=(By.XPATH,"//*[@id='see-book-Git Pocket Guide']/a")
    
    def search_book(self,key):
        self.driver.find_element(*BookPage.SEARCH_BOX).send_keys(key)
        self.driver.find_element(*BookPage.SEARCH_BUTTON).click()
    
    def get_title(self):
        return self.driver.find_element(*BookPage.RESULT).text
    
    def get_input_value(self):
        return self.driver.find_element(*BookPage.SEARCH_BOX).get_attribute("value")
    
    