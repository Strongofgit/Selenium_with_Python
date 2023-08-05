class Add_Loca:
    pim = "//span[normalize-space()='PIM']"
    add_button = "//button[normalize-space()='Add']"
    first_name = "//input[@name='firstName']"
    middle_name = "//input[@name='middleName']"
    last_name = "//input[@name='lastName']"
    employee_id = "//label[text()='Employee Id']/../following-sibling::div/input"
    profile_picture = "//div[@class='employee-image-wrapper']/img"
    save_button = "//button[normalize-space()='Save']"
    required = "//span[text()='Required']"
    notice_save_success = "//p[normalize-space()='Successfully Saved']"
    check_id = "//span[normalize-space()='Employee Id already exists']"
    check_image = "//span[normalize-space()='File type not allowed']"
    employee_lis = "//a[normalize-space()='Employee List']"
    lis_id = "//div[@class='oxd-table-body']//div[contains(@class,'oxd-table-row')]/div[2]"
    page_num = "//ul[@class='oxd-pagination__ul']/li"

class Search_Loca:
    search_button = "//button[normalize-space()='Search']"
    no_resutl = "//div[text()='No Records Found']"
    txtbox_employee_name = "//label[text()='Employee Name']/../following-sibling::div//input"
    list_result = "//div[@role='listbox']//span"
    notice_no_result = "//p[normalize-space()='No Records Found']"
    result = "//div[@class='orangehrm-horizontal-padding orangehrm-vertical-padding']//span"
    
class Delete_Loca:
    delete = "//button[normalize-space()='Delete Selected']"
    excep_del = "//button[normalize-space()='Yes, Delete']"
    options = "//div[@class='oxd-table-body']//input"
    notice_del_success = "//p[normalize-space()='Successfully Deleted']"
    button_del = "//div[text()='0066']/../..//button/i[@class='oxd-icon bi-trash']"
    chose_all = "//div[@class='oxd-table-header']//label/input"
    button_acxept = "//button[normalize-space()='Yes, Delete']"

class Sort_Loca:
    button_sort = "//div[text()='Id']//i"
    ascending = "//div[text()='Id']//span[text()='Ascending']"
    decending = "//div[text()='Id']//span[text()='Decending']"
    sort_id = "//div[@class='oxd-table-body']//div[contains(@class,'oxd-table-row')]/div[2]"

class Details_Loca:
    button_detail = "//div[text()='0070']/../..//button/i[@class='oxd-icon bi-pencil-fill']"
    title_page = "//h6[text()='Personal Details']"
    check_id = "//label[text()='Employee Id']/..//following-sibling::div"
    notice_update_success = "//p[text()='Successfully Updated']"
    notice_saved_success = "//p[text()='Successfully Saved']"
    id_check = "//div[text()='0070']"
    employee_id = "//label[text()='Employee Id']/../following-sibling::div"