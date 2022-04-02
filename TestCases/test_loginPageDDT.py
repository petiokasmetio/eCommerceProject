import time

import pytest
import unittest
import HtmlTestRunner
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadDataConfiguraton
from utilities import excelDataUtils

#(unittest.TestCase)
class Test_login_DDT:

    base_login_url = ReadDataConfiguraton.get_application_url()
    path_excel_file = "C:\\Users\\Elitebook\\PycharmProjects\\eCommerce\\testData\\username_password.xlsx"

    def test_login_ddt(self, setup):
        self.driver = setup
        self.driver.get(self.base_login_url)
        self.login_page_objects = Login(self.driver)
        self.rows = excelDataUtils.getRowCount(self.path_excel_file, 'Лист1')
        print("number of rows in excel", self.rows)
        list_status = []
        for row in range(2, self.rows+1):
            self.username = excelDataUtils.readData(self.path_excel_file, 'Лист1', row, 1) #column number is 1
            self.password = excelDataUtils.readData(self.path_excel_file, 'Лист1', row, 2) #column number is 2
            self.expect_result = excelDataUtils.readData(self.path_excel_file, 'Лист1', row, 3) #column number 3
            self.login_page_objects.set_username(self.username)
            self.login_page_objects.set_password(self.password)
            self.login_page_objects.click_login()
            time.sleep(5)
            actual_title = self.driver.title
            expect_title = 'Dashboard / nopCommerce administration'
            if actual_title == expect_title:
                if self.expect_result == 'Pass':
                    print("TEST PASSED")
                    self.login_page_objects.click_logout()
                    list_status.append("Pass")
                elif self.expect_result == 'Fail':
                    self.login_page_objects.click_logout()
                    list_status.append("Fail")
                    print("TEST FAILED")
            elif actual_title != expect_title:
                if self.expect_result == 'Pass':
                    list_status.append('Fail')
                    print("TEST FAILED")
                elif self.expect_result == 'Fail':
                    list_status.append('Pass')
                    print("TEST PASSED")

        if 'Fail' not in list_status:
            print("LOGIN TEST PASSED")
            self.driver.close()
            assert True
        else:
            print("LOGIN TEST FAILED")
            self.driver.close()
            assert False



