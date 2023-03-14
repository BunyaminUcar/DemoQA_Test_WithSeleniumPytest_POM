from selenium.webdriver.common.by import By

class AlertsPage():
    def __init__(self, driver):
        self.driver = driver
    
    def click_js_alert_button(self):
        self.driver.find_element(By.ID,"alertButton").click()
    
    def catch_alert(self):
         
        alert=self.driver.switch_to.alert
        return alert.text
    
    def accept_alert(self):
        alert=self.driver.switch_to.alert
        alert.accept()