from selenium import webdriver



import pytest
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome("C:\chromewebdriver\chromedriver.exe")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
