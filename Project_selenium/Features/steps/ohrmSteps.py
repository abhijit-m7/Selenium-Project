from behave import *
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@given('launch chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome(ChromeDriverManager().install())


@when('open Orange Hrm Homepage')
def openHomepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the logo present on home page')
def verifyLogo(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then('close Browser')
def closeBrowser(context):
    context.driver.quit()
