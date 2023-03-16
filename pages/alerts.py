from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.PageBase import PageBase


class AlertsPage(PageBase):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    ALERT_BUTTON=(By.ID,"alertButton")
    CONFİRM_BUTTON=(By.XPATH,"//*[@id='confirmButton']")
    CONFİRM_RESULT=(By.XPATH,"//*[@id='confirmResult']")
    PROMPT_RESULTS=(By.XPATH,"//*[@id='promptResult']")
    PROMPT_BUTTON=(By.XPATH,"//*[@id='promtButton']")
    SMALL_MODAL_BUTTON=(By.XPATH,"//*[@id='showSmallModal']")
    SMALL_MODAL_BODY=(By.XPATH,"//*[@class='modal-content']")
    SMALL_MODAL_BODY_CONTENT=(By.XPATH,"//*[@class='modal-body']")
    
    def click_js_alert_button(self):
        self.wait_for_element_w(AlertsPage.ALERT_BUTTON).click()
    
    def catch_alert(self):  
        alert=self.driver.switch_to.alert
        return alert.text
        
    def click_js_confirm_button_to_running_alert(self):
        self.wait_for_element_w(AlertsPage.CONFİRM_BUTTON).click()
        
    def alert_accept(self):
        self.driver.switch_to.alert.accept()
        
    def alert_confirm_text(self):
        return self.driver.find_element(*AlertsPage.CONFİRM_RESULT).text
    
    def alert_not_confirm(self):
        self.driver.switch_to.alert.dismiss()
    
    def alert_send_key(self,key):
        self.driver.switch_to.alert.send_keys(key)

        
    def alert_send_prompt_and_accept_then_get_key(self,key):
        self.alert_send_key(key)
        AlertsPage.alert_accept(self)
        return self.driver.find_element(*AlertsPage.PROMPT_RESULTS).text
        
    def click_js_prompt_button(self):
        self.wait_for_element_w(AlertsPage.PROMPT_BUTTON).click()
        
    def alert_promt_visibility(self):
        wait = WebDriverWait(self.driver, 1)
        try:
            wait.until(EC.visibility_of_element_located((AlertsPage.PROMPT_RESULTS)))
            result = True
        except:
            result = False
        return result
    
    def click_small_modal_button(self):
        self.wait_for_element_w(AlertsPage.SMALL_MODAL_BUTTON).click()    
    
    def small_modal_visibility_and_content(self):
        wait = WebDriverWait(self.driver, 1)
        try:
            wait.until(EC.visibility_of_element_located((AlertsPage.SMALL_MODAL_BODY)))
            modal_content=self.driver.find_element(*AlertsPage.SMALL_MODAL_BODY_CONTENT).text
            result = True
        except:
            result = False
        return result,modal_content
    
    
    
