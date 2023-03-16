
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC 


class PageBase:
    
    def __init__(self, driver):
        self.driver = driver
        
    def wait_for_element_w(self, locator):
        element=WebDriverWait(self.driver, 2).until(EC.visibility_of_element_located(locator))
        return element
    
    def alert_send_key(self,key):
        self.driver.switch_to.alert.send_keys(key)
    
    def items_list(self,locator):
        items=self.driver.find_elements(*locator)
        liste=[]
        for _ in items:
            liste.append(_.text)      
        return liste