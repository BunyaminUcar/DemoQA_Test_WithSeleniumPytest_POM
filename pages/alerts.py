from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class AlertsPage():
    def __init__(self, driver):
        self.driver = driver
    
    ALERT_BUTTON=(By.ID,"alertButton")
    CONFİRM_BUTTON=(By.XPATH,"//*[@id='confirmButton']")
    CONFİRM_RESULT=(By.XPATH,"//*[@id='confirmResult']")
    PROMPT_RESULTS=(By.XPATH,"//*[@id='promptResult']")
    PROMPT_BUTTON=(By.XPATH,"//*[@id='promtButton']")
    def click_js_alert_button(self):
        self.driver.find_element(*AlertsPage.ALERT_BUTTON).click()
    
    def catch_alert(self):  
        alert=self.driver.switch_to.alert
        return alert.text
    
    def accept_alert(self):
        alert=self.driver.switch_to.alert
        alert.accept()
        
    def click_js_confirm_button_to_running_alert(self):
        self.driver.find_element(*AlertsPage.CONFİRM_BUTTON).click()
        
    def alert_accept(self):
        self.driver.switch_to.alert.accept()
        
    def alert_confirm_text(self):
        return self.driver.find_element(*AlertsPage.CONFİRM_RESULT).text
    
    def alert_not_confirm(self):
        self.driver.switch_to.alert.dismiss()
    
    def alert_send_key(self,key):
        self.driver.switch_to.alert.send_keys(key)
        
    def alert_send_prompt_and_accept_then_get_key(self,key):
        self.driver.switch_to.alert.send_keys(key)
        self.driver.switch_to.alert.accept()
        return self.driver.find_element(*AlertsPage.PROMPT_RESULTS).text
        
    def click_js_prompt_button(self):
        self.driver.find_element(*AlertsPage.PROMPT_BUTTON).click()
        
    def alert_promt_visibility(self):
        wait = WebDriverWait(self.driver, 1)
        try:
            wait.until(EC.visibility_of_element_located((AlertsPage.PROMPT_RESULTS)))
            result = True
        except:
            result = False
        return result
         
    
    
