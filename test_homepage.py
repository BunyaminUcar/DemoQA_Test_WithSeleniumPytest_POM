import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from pages.homepage import HomePage

@pytest.mark.usefixtures("setup")
class TestHome():
    
    def test_check_item_bar(self):
        self.driver.get("https://demoqa.com/")
        homepage=HomePage(self.driver)
        menu_items=homepage.get_menu_items() 
        expected_menu_items=["Elements","Forms","Alerts, Frame & Windows","Widgets","Interactions","Book Store Application"]  
        assert menu_items==expected_menu_items
        
        
    def test_click_forms_item(self):
        self.driver.get("https://demoqa.com/")
        homepage=HomePage(self.driver)
        homepage.click_menu_item() 
        title=homepage.get_title()
        assert title=="Elements"
        
        
        
   
