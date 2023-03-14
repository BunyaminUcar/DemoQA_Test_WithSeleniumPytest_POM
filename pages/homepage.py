from selenium.webdriver.common.by import By

class HomePage():
    def __init__(self, driver):
        self.driver = driver

    def get_menu_items(self):
        items=self.driver.find_elements(By.XPATH,"//div/h5")
        menuler=[]
        for _ in items:
            menuler.append(_.text)
                
        return menuler