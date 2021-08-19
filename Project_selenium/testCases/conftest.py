import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("launching Chrome")

    elif browser == "firefox" :
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        print("launching Firefox")

    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("launching Chrome")
    return driver

#This will get value from  CLI/hooks

def pytest_addoption(parser):
    parser.addoption("--browser")

#This will return the value from browser to setup method
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########## PyTest HTML Reports #########
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Abhijit'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)

"""
to run crossBrowser

 pytest -v -s testCases/test_login.py --browser firefox

To run Parallelly
 pytest -v -s -n=2 testCases/test_login.py --browser firefox

TO Generate PyTest Html  Report

pytest -v -s -n=2  --html=Reports/reports.html testCases/test_login.py --browser firefox




"""
