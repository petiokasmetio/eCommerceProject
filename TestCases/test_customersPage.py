import time
import pytest
import unittest
import HtmlTestRunner
from selenium import webdriver
from pageObjects.LoginPage import Login
from pageObjects.CustomersPage import Customers
from utilities.readProperties import ReadDataConfiguraton

class Test_customers:

    base_login_url = ReadDataConfiguraton.get_application_url()
    username_data = ReadDataConfiguraton.get_username_data()
    password_data = ReadDataConfiguraton.get_password_data()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login_thesystem(self, setup):
        self.driver = setup
        self.driver.get(self.base_login_url)
        self.login_page_objects = Login(self.driver)
        self.login_page_objects.set_username(self.username_data)
        self.login_page_objects.set_password(self.password_data)
        self.login_page_objects.click_login()
        actual_title = self.driver.title
        if actual_title == 'Dashboard / nopCommerce administration':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Elitebook\\PycharmProjects\\eCommerce\\Screenshots\\test_login_thesystem.png")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_customers_pagetitle(self, setup):
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
        actual_title = self.driver.title
        if actual_title == 'Add a new customer / nopCommerce administration':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Elitebook\\PycharmProjects\\eCommerce\\Screenshots\\test_customers_pagetitle.png")
            self.driver.close()
            assert False
