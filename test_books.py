import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

from pages.books import BookPage


@pytest.mark.usefixtures("setup")
class TestBooks():
    
    def test_input_key_value(self):
       self.driver.implicitly_wait(10)
       self.driver.get("https://demoqa.com/books")
       book=BookPage(self.driver)
       key="hi"
       book.search_book(key)
       input_value=book.get_input_value()
       assert input_value==key
    
    def test_search_book(self):
       self.driver.implicitly_wait(10)
       self.driver.get("https://demoqa.com/books")
       book=BookPage(self.driver)
       book.search_book("Git")
       time.sleep(1)
       assert book.get_title()=="Git Pocket Guide"
       
    