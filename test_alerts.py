import pytest


import time

from pages.alerts import AlertsPage


@pytest.mark.usefixtures("setup")
class TestAlerts():
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://demoqa.com/alerts")
        self.alert=AlertsPage(self.driver)
    
    def test_catch_alert(self):
                 
        self.alert.click_js_alert_button()      
        message=self.alert.catch_alert()
        time.sleep(1)#wait for alert to appear       
        self.alerts.alert_accept()
        assert message=="You clicked a button"
    
    def test_alert_box_confirm(self):
        
        self.alert.click_js_confirm_button_to_running_alert()
        alert_text=self.alert.catch_alert()
        time.sleep(1)#wait for alert to appear
        self.alert.alert_accept()
        confirm=self.alert.alert_confirm_text()
        assert confirm=="You selected Ok"
        assert alert_text=="Do you confirm action?"
    
    def test_alert_box_not_confirm(self):
        
        self.alert.click_js_confirm_button_to_running_alert()
        alert_text=self.alert.catch_alert()
        time.sleep(1)#wait for alert to appear
        self.alert.alert_not_confirm()
        confirm=self.alert.alert_confirm_text()
        assert confirm=="You selected Cancel"
        assert alert_text=="Do you confirm action?" 
   
    def test_alert_box_send_prompt(self):
        
        self.alert.click_js_prompt_button()
        key="Hello"
        time.sleep(1)#wait for alert to appear
        result=self.alert.alert_send_prompt_and_accept_then_get_key(key)
        assert result=="You entered "+key
       
    def test_alert_box_send_prompt_and_cancel(self):
        
        self.alert.click_js_prompt_button()
        key="Hello"
        self.alert.alert_send_key(key)
        time.sleep(1)#wait for alert to appear
        self.alert.alert_not_confirm()
        result=self.alert.alert_promt_visibility()    
        assert result==False
       
    def test_small_modal_content(self):
        
        self.driver.get("https://demoqa.com/modal-dialogs")
        modal=AlertsPage(self.driver)
        modal.click_small_modal_button()
        time.sleep(1)#wait for modal to appear
        result, model_content=modal.small_modal_visibility_and_content()
        assert result==True
        assert model_content=="This is a small modal. It has very less content"
        
        
    