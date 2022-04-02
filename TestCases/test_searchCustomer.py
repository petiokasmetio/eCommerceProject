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
from pageObjects.SearchCustomerPage import  SearchCustomer

class Test_SearchCustomer:
    base_login_url = ReadDataConfiguraton.get_application_url()
    username_data = ReadDataConfiguraton.get_username_data()
    password_data = ReadDataConfiguraton.get_password_data()

    def test_search_customer_by_email(self, setup):
        self.driver = setup
        self.driver.get(self.base_login_url)
        self.login_page_objects = Login(self.driver)
        self.login_page_objects.set_username(self.username_data)
        self.login_page_objects.set_password(self.password_data)
        self.login_page_objects.click_login()

        self.customers_page_objects = Customers(self.driver)
        self.customers_page_objects.click_customers_navmenu()
        self.customers_page_objects.click_customers_navmenu_option()

        self.search_customer_page_objects = SearchCustomer(self.driver)
        self.search_customer_page_objects.set_email('brenda_lindgren@nopCommerce.com')
        self.search_customer_page_objects.click_search()
        time.sleep(2)
        status = self.search_customer_page_objects.search_customer_by_email('brenda_lindgren@nopCommerce.com')
        assert True == status
        self.driver.close()


