import pytest
from pages.homepage import HomePage

@pytest.mark.usefixtures("setup")
class TestHome():
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://demoqa.com/")
        self.homepage=HomePage(self.driver)
    
    def test_check_item_bar(self):
        
        menu_items=self.homepage.get_menu_items() 
        expected_menu_items=["Elements","Forms","Alerts, Frame & Windows","Widgets","Interactions","Book Store Application"]  
        assert menu_items==expected_menu_items
        
        
    def test_click_forms_item(self):
        
        self.homepage.click_menu_item() 
        title=self.homepage.get_title()
        assert title=="Elements"
        
        
        
   
