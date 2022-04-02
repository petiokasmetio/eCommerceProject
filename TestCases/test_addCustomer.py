import random
import string
import time
import pytest
import unittest
import HtmlTestRunner
from selenium import webdriver
from pageObjects.LoginPage import Login
from pageObjects.CustomersPage import Customers
from pageObjects.AddCustomerPage import AddCustomer
from utilities.readProperties import ReadDataConfiguraton

class Test_AddCustomer:
    base_login_url = ReadDataConfiguraton.get_application_url()
    username_data = ReadDataConfiguraton.get_username_data()
    password_data = ReadDataConfiguraton.get_password_data()

    @pytest.mark.sanity
    def test_add_customer(self, setup):
        self.driver = setup
        self.driver.get(self.base_login_url)
        self.login_page_objects = Login(self.driver)
        self.login_page_objects.set_username(self.username_data)
        self.login_page_objects.set_password(self.password_data)
        self.login_page_objects.click_login()

        self.customers_page_objects = Customers(self.driver)
        self.customers_page_objects.click_customers_navmenu()
        self.customers_page_objects.click_customers_navmenu_option()
        self.customers_page_objects.click_addnew_custumer_button()

        self.add_customer_page_objects = AddCustomer(self.driver)
        self.email = random_generator() + "@gmail.com"
        self.add_customer_page_objects.set_email(self.email)
        self.add_customer_page_objects.set_password("test123")
        self.add_customer_page_objects.set_firstname("Petar")
        self.add_customer_page_objects.set_lastname("Nikolov")
        self.add_customer_page_objects.set_gender("Male")
        self.add_customer_page_objects.set_dateofbirth("03.03.1990")
        self.add_customer_page_objects.set_companyname("Automation QA")
        #self.add_customer_page_objects.set_customer_role("Guests")
        self.add_customer_page_objects.click_save_button()
        self.message = self.driver.find_element_by_tag_name("body").text
        if 'The new customer has been added successfully.' in self.message:
            assert True == True
            self.driver.close()
        else:
            assert True == False
            self.driver.close()

        #self.message = self.driver.find_element_by_css_selector('div[class="alert alert-success alert-dismissable"]')
        #assert(True, self.message.is_displayed())
        #self.driver.close()

        #self.message = self.driver.find_element_by_css_selector('div[class="alert alert-success alert-dismissable"]').text
        #print(self.message)
        #if 'The new customer has been added successfully.' in self.message:
            #assert True == True
            #self.driver.close()
        #else:
            #assert True == False

def random_generator(size = 8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range (size))