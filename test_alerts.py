import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

from pages.alerts import AlertsPage


@pytest.mark.usefixtures("setup")
class TestAlerts():
    
    def test_catch_alert(self):
        self.driver.get("https://demoqa.com/alerts")
        alerts=AlertsPage(self.driver)        
        alerts.click_js_alert_button()      
        message=alerts.catch_alert()
        time.sleep(1)#wait for alert to appear       
        alerts.accept_alert()
        assert message=="You clicked a button"

        
        
        