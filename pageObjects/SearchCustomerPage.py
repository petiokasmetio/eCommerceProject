import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

class SearchCustomer:

    input_email_id = 'SearchEmail'
    input_firstname_id = 'SearchFirstName'
    input_lastname_id = 'SearchLastName'
    button_search_id = 'search-customers'

    table_search_result_xpath = '//table[@role="grid"]'
    table_customers_grid_xpath = '//table[@id="customers-grid"]'
    table_rows_xpath = '//table[@id="customers-grid"]//tbody/tr'
    table_columns_xpath = '//table[@id="customers-grid"]//tbody/tr/td'


    def __init__(self, driver):
        self.driver = driver

    def set_email(self, email):
        self.driver.find_element_by_id(self.input_email_id).clear()
        self.driver.find_element_by_id(self.input_email_id).send_keys(email)

    def set_firstname(self, firstname):
        self.driver.find_element_by_id(self.input_firstname_id).clear()
        self.driver.find_element_by_id(self.input_firstname_id).send_keys(firstname)

    def set_lastname(self, lastname):
        self.driver.find_element_by_id(self.input_lastname_id).clear()
        self.driver.find_element_by_id(self.input_lastname_id).send_keys(lastname)

    def click_search(self):
        self.driver.find_element_by_id(self.button_search_id).click()

    def get_number_of_rows(self):
        return len(self.driver.find_element_by_xpath(self.table_rows_xpath))

    def get_number_of_columns(self):
        return len(self.driver.find_element_by_xpath(self.table_columns_xpath))

    def search_customer_by_email(self, email):
        flag = False
        for r in range (1, self.get_number_of_rows()+1):
            table = self.driver.find_element_by_xpath(self.table_customers_grid_xpath)
            email_id = table.find_element_by_xpath("//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[2]").text
            if email_id == email:
                flag = True
                break
        return flag

    def search_customer_by_name(self, name):
        flag = False
        for r in range (1, self.get_number_of_rows()+1):
            table = self.driver.find_element_by_xpath(self.table_customers_grid_xpath)
            fullname = table.find_element_by_xpath('//table[@id="customers-grid"]/tbody/tr["+str(r)+"]/td[3]').text
            if fullname == name:
                flag = True
                break
        return flag
