from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Locators.test_data import TestData


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator)))
        element.click()

    def do_send_keys(self, by_locator, text):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator)))
        element.send_keys(text)

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator)))
        print(element.text)

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, by_locator)))
        return bool(element)

    def get_title(self):
        try:
            title = TestData.title
            WebDriverWait(self.driver, 10).until(EC.title_is(title))
        except:
            print("Failed!")
        else:
            print("Title ", self.driver.title)