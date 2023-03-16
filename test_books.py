import pytest
from selenium.webdriver.support import expected_conditions as EC

import time

from pages.books import BookPage



@pytest.mark.usefixtures("setup")
class TestBooks():
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.driver.get("https://demoqa.com/books")
        self.book=BookPage(self.driver)
    
    def test_input_key_value(self):
      
      
      key="hi"
      self.book.search_book(key)
      input_value=self.book.get_input_value()
      assert input_value==key
    
    def test_search_book(self):
       
      
      self.book.search_book("Git")
      time.sleep(1)
      assert self.book.get_title()=="Git Pocket Guide"
       
    