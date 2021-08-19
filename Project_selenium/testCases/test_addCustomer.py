import pytest
import time
from page_objects.LoginPage import LoginPage
from page_objects.AddCustomerPage import AddCustomer
from .conftest import *
from utilities.readProperties import ReadConfig
from utilities.customLogger import logGen
import string
import random

class Test_003_AddCustomer:
    baseUrl = ReadConfig.baseUrl()
    username = ReadConfig.username()
    password = ReadConfig.password()
    logger = logGen.loggen()

    def test_AddCustomers(self,setup):
        self.logger.info("*********Test_003_AddCustomer*************")
        self.driver = setup

        self.driver.get(self.baseUrl)
        self.driver.maximize_window()

        self.Login_obj = LoginPage(self.driver)
        self.Login_obj.username(self.username)
        self.Login_obj.password(self.password)
        self.Login_obj.Loginbutton()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Add Customer Test **********")

        self.AddCust_obj = AddCustomer(self.driver)
        self.AddCust_obj.clickOnCustomersMenu()
        self.AddCust_obj.clickOnCustomersMenuItem()
        self.AddCust_obj.clickOnAddnew()

        self.logger.info("************* Providing customer info **********")

        self.email = random_generator() + "@gmail.com"
        self.AddCust_obj.setEmail(self.email)
        self.AddCust_obj.setPassword("test123")
        self.AddCust_obj.setCustomerRoles("Guests")
        self.AddCust_obj.setManagerOfVendor("Vendor 2")
        self.AddCust_obj.setGender("Male")
        self.AddCust_obj.setFirstName("Abhijit")
        self.AddCust_obj.setLastName("Menon")
        self.AddCust_obj.setDob("7/10/1996")  # Format: D / MM / YYY
        self.AddCust_obj.setCompanyName("NO")
        self.AddCust_obj.setAdminContent("This is for testing.........")
        self.AddCust_obj.clickOnSave()

        self.logger.info("************* Saving customer info **********")

        self.logger.info("********* Add customer validation started *****************")

        self.msg = self.driver.find_element_by_tag_name("body").text

        print(self.msg)
        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("********* Add customer Test Passed *********")
        else:
            self.driver.save_screenshot("Screenshots/" + "test_addCustomer_scr.png")  # Screenshot
            self.logger.error("********* Add customer Test Failed ************")
            assert False

        self.driver.quit()
        self.logger.info("******* Ending Add customer test **********")


        def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
            return ''.join(random.choice(chars) for x in range(size))
