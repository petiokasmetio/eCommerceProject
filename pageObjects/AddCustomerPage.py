import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class AddCustomer:

    button_navlink_customers_css = 'i[class="nav-icon far fa-user"]'
    button_option_customers_xpath = '(//p[contains(.,"Customers")])[2]'
    button_addnew_customer_css = 'a[href="/Admin/Customer/Create"]'
    input_email_id = 'Email'
    input_password_id = 'Password'
    input_firstname_id = 'FirstName'
    input_lastname_id = 'LastName'
    radiobutton_male_id = 'Gender_Male'
    radiobutton_female_id = 'Gender_Female'
    input_dateofbirth_id = 'DateOfBirth'
    input_companyname_id = 'Company'
    check_tax_id = 'IsTaxExempt'
    listbox_newsletter_xpath = '(//div[contains(@unselectable,"on")])[2]'
    listbox_newsletter_optionyourstore_xpath = '//li[@tabindex="-1"][contains(.,"Your store name")]'
    listbox_custumerrole_xpath = '//input[contains(@aria-expanded,"true")]'
    listbox_custumerrole_guests_xpath = '//li[@tabindex="-1"][contains(.,"Guests")]'
    button_save_css = 'button[name="save"]'
    alert_successful_message_css = 'body[class="sidebar-mini layout-fixed control-sidebar-slide-open sidebar-closed sidebar-collapse"]'

    def __init__(self, driver):
        self.driver = driver

    def click_customers_navmenu(self):
        self.driver.find_element_by_css_selector(self.button_navlink_customers_css).click()

    def click_customers_navmenu_option(self):
        self.driver.find_element_by_xpath(self.button_option_customers_xpath).click()

    def click_addnew_custumer_button(self):
        self.driver.find_element_by_css_selector(self.button_addnew_customer_css).click()

    def set_email(self, email):
        self.driver.find_element_by_id(self.input_email_id).send_keys(email)

    def set_password(self, password):
        self.driver.find_element_by_id(self.input_password_id).send_keys(password)

    def set_firstname(self, firstname):
        self.driver.find_element_by_id(self.input_firstname_id).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element_by_id(self.input_lastname_id).send_keys(lastname)

    def set_gender(self, gender):
        if gender == 'Male':
            self.driver.find_element_by_id(self.radiobutton_male_id).click()
        elif gender == 'Female':
            self.driver.find_element_by_id(self.radiobutton_female_id).click()
        else:
            self.driver.find_element_by_id(self.radiobutton_male_id).click()

    def set_dateofbirth(self, dateofbirth):
        self.driver.find_element_by_id(self.input_dateofbirth_id).send_keys(dateofbirth)

    def set_companyname(self, companyname):
        self.driver.find_element_by_id(self.input_companyname_id).send_keys(companyname)

    def check_tax(self):
        self.driver.find_element_by_id(self.check_tax_id).click()

    def click_newsletter(self):
        self.driver.find_element_by_xpath(self.listbox_newsletter_xpath).click()

    def set_newsletter_option(self):
        self.driver.find_element_by_xpath(self.listbox_newsletter_optionyourstore_xpath).click()

    def set_customer_role(self):
        self.driver.find_element_by_xpath(self.listbox_custumerrole_xpath).click()
        time.sleep(1)
        if role == 'Guests':
            self.list_item = self.driver.find_element_by_xpath(self.listbox_custumerrole_guests_xpath)
        time.sleep(1)
        self.driver.execute_script("arguments[2].click();", self.list_item)
    #def set_customer_role(self, role):
        #self.driver.find_element_by_xpath(self.listbox_custumerrole_guests_xpath).click()

    def click_save_button(self):
        self.driver.find_element_by_css_selector(self.button_save_css).click()

    def get_successful_message(self):
        self.driver.find_element_by_css_selector(self.alert_successful_message_css).text