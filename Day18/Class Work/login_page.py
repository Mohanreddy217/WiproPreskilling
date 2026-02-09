from selenium import webdriver
from selenium.webdriver.common.by import By

class login_page:
    
    def __init__(self,driver):
        self.driver=driver

    username=(By.NAME,"username")
    password=(By.NAME,"password")
    loginbutton=(By.XPATH,"//button[@type='submit']")


    def enter_username(self,user):
        self.driver.find_element(*self.username).send_keys(user)
        
    def enter_password(self,pwsd):
        self.driver.find_element(*self.password).send_keys(pwsd)
    
    def click_login(self):
        self.driver.find_element(*self.loginbutton).click()