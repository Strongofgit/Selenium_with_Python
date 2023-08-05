import random

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.pim_loca import Add_Loca
from Locators.login_page_loca import Login_Page_Loca
from Locators.pim_loca import Search_Loca
from Locators.pim_loca import Delete_Loca
from Locators.pim_loca import Details_Loca
from Locators.pim_loca import Sort_Loca
from Locators.test_data import TestData_Pim
from Locators.test_data import TestData
from Pages.base_Page import BasePage
from time import sleep


class PimPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self):
        self.do_send_keys(Login_Page_Loca.loca_username, TestData.username)
        self.do_send_keys(Login_Page_Loca.loca_password, TestData.password)
        self.do_click(Login_Page_Loca.loca_login_button)

    def send(self, _id):
        self.do_send_keys(Add_Loca.first_name, TestData_Pim.first_name)
        self.do_send_keys(Add_Loca.last_name, TestData_Pim.last_name)
        txt = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, Add_Loca.employee_id)))
        txt.send_keys(Keys.BACKSPACE * len(txt.get_attribute("value")))
        self.do_send_keys(Add_Loca.employee_id, _id)
        # self.do_send_keys(Add_Loca.profile_picture, TestData_Pim.profile_picture)

    def add_delete(self, _id):
        self.do_click(Add_Loca.add_button)
        self.do_send_keys(Add_Loca.first_name, TestData_Pim.first_name)
        self.do_send_keys(Add_Loca.last_name, TestData_Pim.last_name)
        txt = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, Add_Loca.employee_id)))
        txt.send_keys(Keys.BACKSPACE * len(txt.get_attribute("value")))
        self.do_send_keys(Add_Loca.employee_id, _id)
        self.do_click(Add_Loca.save_button)
        self.do_click(Add_Loca.employee_lis)

    def find_id(self, _id):
        try:
            self.driver.find_element(By.XPATH, f"//div[text()='{_id}']")
        except:
            print("Id has not been added to the list")
        else:
            print("Added id to the list")
    def add_employee(self): #Ktra nếu tồn tại trong lisst thì xóa trc
        self.login()
        self.do_click(Add_Loca.pim)
        self.do_click(Add_Loca.add_button)
        _id = random.randint(1000, 9999) # random 1 id
        #_id = "0038"
        self.send(_id)
        #Check ID tồn tại chưa
        try:
            self.driver.find_element(By.XPATH, Add_Loca.check_id)
        except:
            print("ID")
        else:
            self.do_click(Add_Loca.employee_lis)
            element = self.driver.find_element(By.XPATH, f"//div[text()='{_id}']/../preceding-sibling::div//input")
            self.driver.execute_script("arguments[0].click();", element)
            self.do_click(Delete_Loca.delete)
            self.do_click(Delete_Loca.excep_del)
            self.do_click(Add_Loca.add_button)
            self.send(_id)
        before_id = self.get_element_text(Add_Loca.employee_id)
        self.do_click(Add_Loca.save_button)
        # Check thông báo success khi save. Kieemr tra list xh nó
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Add_Loca.notice_save_success)))
        except:
            print("Save Failed!")
        else:
            print("Save successed!")
            self.do_click(Add_Loca.employee_lis)
            try:
                path = self.driver.find_elements(By.XPATH, Add_Loca.page_num) # ktra số trang hiển thị
                page_number = len(path)
            except:
                self.find_id(_id)
            else:
                try:
                    self.driver.find_element(By.XPATH, f"//div[text()='{_id}']")
                except:
                    for x in range(0, page_number):
                        if x + 2 < page_number:
                            self.driver.find_element(By.XPATH, f"//button[text()='{x+2}']").click()
                            try:
                                self.driver.find_element(By.XPATH, f"//div[text()='{_id}']")
                            except:
                                continue
                            else:
                                print("Added id to the list")
                                break
                    else:
                        print("Id has not been added to the list")
                else:
                    print("Added id to the list")

        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Add_Loca.required)))
        except:
            print("Enough fullname!")
        else:
            print("Required Firstname and Lastname!")

        '''
        # Ktra load page sau khi save
        try:
           after_id = self.get_element_text(Add_Loca.employee_id)
        except:
            print("No load")
        else:
            if before_id == after_id:
                print("Load page correct!")
            else:
                print("Load page wrong!")
        '''

        '''
        #Check file image hợp lệ không
        try:
            self.driver.find_element(By.XPATH, Add_Loca.check_image)
        except:
            print("Image")
        else:
            print("File image not allowed")
        '''

    def search(self):
        self.login()
        self.do_click(Add_Loca.pim)
        self.do_send_keys(Search_Loca.txtbox_employee_name, TestData_Pim.name_enter)
        sleep(3)
        try:
            self.driver.find_element(By.XPATH, Search_Loca.no_resutl)
        except:
            lis = self.driver.find_elements(By.XPATH, Search_Loca.list_result)
            for i in range(0, len(lis)):
                if lis[i].text == TestData_Pim.name_search:
                    lis[i].click()
                    self.do_click(Search_Loca.search_button)
                    sleep(5)
                    print(self.get_element_text(Search_Loca.result))
        else:
            self.do_click(Search_Loca.search_button)
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Search_Loca.notice_no_result)))
            except:
                print("NO Display notice 'No record found'")
            else:
                print("Displayed notice 'No record found'")

    def delete(self): # Tạo dữ liệu text cho bất kỳ cái nào muốn del
        self.login()
        self.do_click(Add_Loca.pim)
        try:
            lis_loca_id = self.driver.find_elements(By.XPATH, Sort_Loca.sort_id)
            lis_id = []
            for i in lis_loca_id:
                _id = i.text
                lis_id.append(_id)
            ran_id = random.randint(1000, 9999)
            while ran_id in lis_id:
                ran_id = random.randint(1000, 9999)
            else:
                self.add_delete(ran_id)
        except:
            print("")
        else:
            element = self.driver.find_element(By.XPATH, f"//div[text()='{ran_id}']/../preceding-sibling::div//input")
            path= f"//div[text()='{ran_id}']"
            self.driver.execute_script("arguments[0].click();", element)
            self.do_click(Delete_Loca.delete)
            self.do_click(Delete_Loca.excep_del)
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Delete_Loca.notice_del_success)))
            except:
                print("Notice not be display")
            else:
                print("Displayed notice!")

            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, path)))
            except:
                print("Element not in list id")
            else:
                print("Element in list")

        '''
        # Xóa 1 employee bằng button del               
        try:
            lis_loca_id = self.driver.find_elements(By.XPATH, Sort_Loca.sort_id)
            lis_id = []
            for i in lis_loca_id:
                _id = i.text
                lis_id.append(_id)
            ran_id = random.randint(1000, 9999)
            while ran_id in lis_id:
                ran_id = random.randint(1000, 9999)
            else:
                self.add_delete(ran_id)
        except:
            print("")
        else:
            element = self.driver.find_element(By.XPATH, f"//div[text()='{ran_id}']/../..//button/i[@class='oxd-icon bi-trash']")
            path= f"//div[text()='{ran_id}']"
            self.driver.execute_script("arguments[0].click();", element)
            self.do_click(Delete_Loca.button_acxept)
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Delete_Loca.notice_del_success)))
            except:
                print("Notice not be display")
            else:
                print("Displayed notice!")

            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, path)))
            except:
                print("Element not in list id")
            else:
                print("Element in list")
        '''

        '''
        #Delete all
        try:
           option = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Delete_Loca.chose_all)))
           self.do_click(option)
           self.do_click(Delete_Loca.delete)
           self.do_click(Delete_Loca.excep_del)
        except:
            print("Deleted fail!")
        else:
            try:
                self.driver.find_element(By.XPATH, "//p[normalize-space()='Successfully Deleted']")
            except:
                print("Notice is not Displayed!")
            else:
                print("Deleted success!")
        '''

    def sort(self):
        """ Kiểm tra danh sách đc sort theo id sau khi click chưa """
        self.login()
        self.do_click(Add_Loca.pim)
        try:
            lis_nosort = self.driver.find_elements(By.XPATH, Sort_Loca.sort_id)
            lis_id_befo = []
            for i in range(0, len(lis_nosort)):
                lis_id_befo.append(lis_nosort[i].text)

            self.do_click(Sort_Loca.button_sort)
            self.do_click(Sort_Loca.ascending)
            sleep(3)
            lis_id = self.driver.find_elements(By.XPATH, Sort_Loca.sort_id)
            lis_id_sorted = []
            for i in range(0, len(lis_id)):
                lis_id_sorted.append(lis_id[i].text)
        except:
            print("...")
        else:
            lis_id_befo_sorted = sorted(lis_id_befo, key=int)
            if lis_id_sorted == lis_id_befo_sorted:
                print("Sorted Id!")
            else:
                print("Id is not sorted!")


    def details(self):
        self.login()
        self.do_click(Add_Loca.pim)
        try:
            lis_loca_id = self.driver.find_elements(By.XPATH, Sort_Loca.sort_id)
            lis_id = []

            for i in lis_loca_id:
                _id = i.text
                lis_id.append(_id)
            print(lis_id)
            ran_id = random.randint(1000, 9999) # tạo 1 id có 4 chữ số ngẫu nhiên để detail
            while ran_id in lis_id:
                ran_id = random.randint(1000, 9999)
            else:
                self.do_click(Add_Loca.add_button)
                self.do_send_keys(Add_Loca.first_name, TestData_Pim.first_name)
                self.do_send_keys(Add_Loca.last_name, TestData_Pim.last_name)
                txt = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH, Add_Loca.employee_id)))
                txt.send_keys(Keys.BACKSPACE * len(txt.get_attribute("value"))) #xóa
                self.do_send_keys(Add_Loca.employee_id, ran_id)
                self.do_click(Add_Loca.save_button)
                self.do_click(Add_Loca.employee_lis)
        except:
            print("")
        else:
            element = self.driver.find_element(By.XPATH, f"//div[text()='{ran_id}']/../preceding-sibling::div//input")
            self.driver.execute_script("arguments[0].click();", element)
            self.do_click(Details_Loca.button_detail)
            #self.do_click(Delete_Loca.excep_del)
            try:
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, Details_Loca.check_id)))
            except:
                print("Nope!")
            else:
                print("Loaded")

    #############################