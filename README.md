DemoQA_Test_WithSeleniumPytest_POM

# pytest + selenium: demo tests

## Setup instructions (this assumes that you already have Python and pip installed)

- If you use this repository, you need 2 libraries


### 1-pytest

- Install [pytest](http://doc.pytest.org/en/latest/getting-started.html) via pip or easy_install:
```
pip install -U pytest or easy_install -U pytest
```
- After installation, you can check the installed version by running:
```
pytest --version
```

### 2-selenium webdriver

- Install [selenium](http://selenium-python.readthedocs.io/installation.html) via pip:
```
pip install -U selenium
```


## How to run the tests

- To run all tests inside the test directory, simply run this command:
```
pytest

or for a more detailed report

python -v pytest
```
Tests are specially tuned to generate reports in a sequential manner.

- To run a test module, simply do
```
pytest <module name>
e.g. pytest test_alerts.py
```
- To run a specific test, do
```
pytest <module name> <class name> <test name>
e.g. pytest test_alerts.py::TestAlerts::test_alert_box_send_prompt_and_cancel
```
- It is recommended to run the tests with verbosity by invoking `-v` during the test run.
- If there are `print` statements you wish to see on the console when the tests run, add `-s` to disable stdout
capturing.
 
