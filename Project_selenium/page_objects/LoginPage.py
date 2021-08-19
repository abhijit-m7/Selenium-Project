from selenium import webdriver

class LoginPage:
    u_textbox_id = "Email"
    p_textbox_id = "Password"
    button_login_xpath = "//button[normalize-space()='Log in']"
    button_logout_link_text = "Logout"

    def __init__(self,driver):
        self.driver = driver

    def username(self,username):
        self.driver.find_element_by_id(self.u_textbox_id).clear()
        self.driver.find_element_by_id(self.u_textbox_id).send_keys(username)

    def password(self,password):
        self.driver.find_element_by_id(self.p_textbox_id).clear()
        self.driver.find_element_by_id(self.p_textbox_id).send_keys(password)

    def Loginbutton(self):
        self.driver.find_element_by_xpath(self.button_login_xpath).click()

    def Logout(self):
        self.driver.find_element_by_link_text(self.button_logout_link_text).click()
