
from Pages.login_Page import LoginPage
from Pages import login_Page
from Tests.setup import Setup
from Pages.pim_page import PimPage
from time import sleep


class Login_Test(Setup):
    def __init__(self):
        super().__init__()

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        login.process_login()
        login.get_title()
        sleep(3)

class Pim_Test(Setup):

    def __init__(self):
        super().__init__()
    def test_add(self):
        driver = self.driver
        add = PimPage(driver)
        add.add_employee()

    def test_search(self):
        driver = self.driver
        search = PimPage(driver)
        search.search()

    def test_delete(self):
        driver = self.driver
        delete = PimPage(driver)
        delete.delete()

    def test_sort(self):
        driver = self.driver
        sort = PimPage(driver)
        sort.sort()

    def test_details(self):
        driver = self.driver
        detail = PimPage(driver)
        detail.details()


# l = Login_Test()
# l.test_login()

p = Pim_Test()
p.test_add()
#p.test_search()
#p.test_delete()
#p.test_sort()
#p.test_details()