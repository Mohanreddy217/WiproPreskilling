from Loginpage_factory import loginpage_PageFactory
from selenium import webdriver

driver=webdriver.Edge()
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.implicitly_wait(10)
login=loginpage_PageFactory(driver)
login.enterusername("Admin")
login.enterpassword("admin123")
login.clicklogin()