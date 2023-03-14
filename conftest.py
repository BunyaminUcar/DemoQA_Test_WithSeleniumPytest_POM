from selenium import webdriver
from selenium.webdriver.common.keys import Keys


import pytest
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome("C:\chromewebdriver\chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
