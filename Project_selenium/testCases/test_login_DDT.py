import pytest
from selenium import webdriver
from page_objects.LoginPage import LoginPage
from webdriver_manager.chrome import ChromeDriverManager
from .conftest import *
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
from utilities import ExcelUtilities
import time

class Test_002_Login_DDT:
    baseUrl = ReadConfig.baseUrl()
    path = "TestData/LoginData.xlsx" #path of excel sheet
    logger = logGen.loggen()

    def test_login_DDT(self,setup):
        self.logger.info("*************Test_002_Login_DDT*************")
        self.logger.info("*************Login*************")
        self.driver = setup
        self.driver.get(self.baseUrl)

        #Creating self Object of Class LoginPage
        self.Login_obj = LoginPage(self.driver)

        #Getting row count from  Excel sheet
        self.rows = ExcelUtilities.getRowCount(self.path,'Sheet1')
        print("Number of rows:",self.rows)

        #list of pass/Fail status
        list_status = []

        for i in range (2,self.rows+1):
            self.user = ExcelUtilities.readData(self.path,'Sheet1',i,1)
            self.paswd = ExcelUtilities.readData(self.path,'Sheet1',i,2)
            self.exp = ExcelUtilities.readData(self.path,'Sheet1',i,3)

            self.Login_obj.username(self.user)
            self.Login_obj.password(self.paswd)
            self.Login_obj.Loginbutton()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("***********Login Passed***********")
                    self.Login_obj.Logout()
                    list_status.append("Pass")

                elif self.exp == "Fail":
                    self.logger.info("***********Login Failed***********")
                    self.Login_obj.Logout()
                    list_status.append("Fail")

            if act_title != exp_title:
                    if self.exp == "Pass":
                        self.logger.info("***********Failed***********")
                        list_status.append("Fail")

                    elif self.exp == "Fail":
                        self.logger.info("***********Passed***********")
                        list_status.append("Pass")
        if "Fail" not in list_status:
            self.logger.info("***********Login DDT Passed***********")
            self.driver.quit()
            assert True
        else:
            self.logger.info("***********Login DDT Failed***********")
            self.driver.quit()
            assert False

        self.logger.info("***********Login DDT Completed***********")
