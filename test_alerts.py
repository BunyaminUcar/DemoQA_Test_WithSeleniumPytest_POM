import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from pages.alerts import AlertsPage


@pytest.mark.usefixtures("setup")
class TestAlerts():
    
    def test_catch_alert(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://demoqa.com/alerts")
        alerts=AlertsPage(self.driver)        
        alerts.click_js_alert_button()      
        message=alerts.catch_alert()
        time.sleep(1)#wait for alert to appear       
        alerts.accept_alert()
        assert message=="You clicked a button"

    def test_alert_box_confirm(self):
        self.driver.implicitly_wait(10)
        self.driver.get("https://demoqa.com/alerts")
        alert=AlertsPage(self.driver)
        alert.click_js_confirm_button_to_running_alert()
        alert_text=alert.catch_alert()
        time.sleep(1)#wait for alert to appear
        alert.alert_accept()
        confirm=alert.alert_confirm_text()
        
        assert confirm=="You selected Ok"
        assert alert_text=="Do you confirm action?"