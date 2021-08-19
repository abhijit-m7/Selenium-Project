import pytest
from selenium import webdriver
from page_objects.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from .conftest import *
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen

class Test_001_Login:
    baseUrl = ReadConfig.baseUrl()
    username = ReadConfig.username()
    password = ReadConfig.password()

    logger = logGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("*************Test_001_Login*************")
        self.logger.info("*************Verifying Title*************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        title = self.driver.title
        if title == "Your store. Login":
            assert True
            self.driver.quit()
            self.logger.info("*************Title Pass*************")
        else:
            assert False
            self.driver.quit()
            self.logger.error("*************Title Fail*************")

    def test_login(self,setup):
        self.logger.info("*************Test_001_Login*************")
        self.logger.info("*************Login*************")

        self.driver = setup
        self.driver.get(self.baseUrl)
        self.Login_obj = LoginPage(self.driver)
        self.Login_obj.username(self.username)
        self.Login_obj.password(self.password)
        self.Login_obj.Loginbutton()
        title = self.driver.title


        if title == "Dashboard / nopCommerce administration":
            assert True
            self.driver.quit()
            self.logger.info("*************Login Pass*************")
        else:
            self.driver.save_screenshot("/home/abhijit/Desktop/python/Project_selenium/Screenshots/"+"test_fail.png")
            self.driver.quit()
            self.logger.error("*************Login Fail*************")
            assert False
