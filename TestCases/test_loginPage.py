import pytest
import unittest
import HtmlTestRunner
from selenium import webdriver
from pageObjects.LoginPage import Login
from utilities.readProperties import ReadDataConfiguraton
from utilities.customLogger import LogGeneration

class Test_login:

    base_login_url = ReadDataConfiguraton.get_application_url()
    username_data = ReadDataConfiguraton.get_username_data()
    password_data = ReadDataConfiguraton.get_password_data()
    logger = LogGeneration.loggen()

    @pytest.mark.petiokasmetio
    def test_loginpage_title(self, setup):
        self.logger.info("*** test login page title ***")
        self.driver = setup
        self.driver.get(self.base_login_url)
        actual_title = self.driver.title
        if actual_title == 'Your store. Login':
            assert True
            self.driver.close()
            self.logger.info("*** test login page title PASSED ***")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Elitebook\\PycharmProjects\\eCommerce\\Screenshots\\test_loginpage_title.png")
            self.driver.close()
            self.logger.error("*** test login page title FAILED ***")
            assert False

    @pytest.mark.petiokasmetio
    def test_login(self, setup):
        self.logger.info("*** test login the system ***")
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
            self.logger.info("*** test login the system PASSED ***")
        else:
            self.driver.save_screenshot(
                "C:\\Users\\Elitebook\\PycharmProjects\\eCommerce\\Screenshots\\test_login.png")
            self.driver.close()
            assert False
            self.logger.error("*** test login the system FAILED ***")





