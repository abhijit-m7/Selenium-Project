from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given('launch the chrome browser')
def Browser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())

@when('open  Homepage')
def Homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('Enter username "admin" and password "admin123"')
def usrAndpass(context):
    username = "txtUsername"
    password =  "txtPassword"
    context.driver.find_element_by_id(username).send_keys("admin")
    context.driver.implicitly_wait(10)
    context.driver.find_element_by_id(password).send_keys("admin123")

@then('click on login button')
def loginButton(context):
    Login = "//input[@id='btnLogin']"
    context.driver.find_element_by_xpath(Login).click()

@then('user must successfully login to the Dashboard')
def succesfulLogin(context):
    text = context.driver.find_element_by_xpath("//h1[normalize-space()='Dashboard']").text
    assert text == "Dashboard"
    context.driver.quit()
