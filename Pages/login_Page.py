from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.login_page_loca import Login_Page_Loca
from selenium.webdriver.common.by import By
from Pages.base_Page import BasePage
from Locators.test_data import TestData


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    #Lấy trực tiếp user và pass từ web
    def take_user(self):
        #user = self.driver.find_element(By.XPATH, self.user)
        find_user = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Login_Page_Loca.user)))
        x = find_user.text  # Áp dụng strip() để loại bỏ khoảng trắng
        x_list = [item.strip() for item in x.split(':')]
        x_dict = {'Username': x_list[1]}  # Tạo từ điển với khóa 'Username' và giá trị tương ứng
        return x_dict.get('Username')

    def take_passw(self):
        find_pass = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Login_Page_Loca.passw)))
        x = find_pass.text
        x_list = [item.strip() for item in x.split(':')]
        x_dict = {'Password': x_list[1]}
        return x_dict.get('Password')

    def enter_username(self):
        x = self.driver.find_element(By.XPATH, Login_Page_Loca.loca_username)
        x.send_keys(self.take_user())

    def enter_password(self):
        x = self.driver.find_element(By.XPATH, Login_Page_Loca.loca_password)
        x.send_keys(self.take_passw())

    def click_login(self):
        self.driver.find_element(By.XPATH, Login_Page_Loca.loca_login_button).click()

    def process_login(self):
        self.enter_username()
        self.enter_password()
        self.click_login()

        try:
            self.driver.find_element(By.XPATH, Login_Page_Loca.required_info)
        except:
            try:
                self.driver.find_element(By.XPATH, Login_Page_Loca.invalid_notice)
            except:
                print("Exactly!")
            else:
                print("Invalid!")
        else:
            print("Required usern and passw!")

    def do_get_title(self):
        self.get_title()