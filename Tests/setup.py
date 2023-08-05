
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Pages.login_Page import TestData
from Pages import login_Page
from Locators.login_page_loca import Login_Page_Loca
from selenium.webdriver.common.by import By



class Setup:
    def __init__(self):
        #self.desired_caps = {'platform': "WINDOWS", 'browserName': "chrome"}
        #self.driver = webdriver.Remote('http://localhost:4444/wd/hub', self.desired_caps)
        self.driver = webdriver.Chrome()
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element(By.XPATH, login_Page.Login_Page_Loca.title_page_login)
        except:
            print("Load page failed!")
        else:
            print("Load page success!")

