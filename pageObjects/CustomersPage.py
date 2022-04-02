from selenium import webdriver

class Customers:

    button_navlink_customers_css = 'i[class="nav-icon far fa-user"]'
    button_option_customers_xpath = '(//p[contains(.,"Customers")])[2]'
    button_addnew_customer_css = 'a[href="/Admin/Customer/Create"]'

    def __init__(self, driver):
        self.driver = driver

    def click_customers_navmenu(self):
        self.driver.find_element_by_css_selector(self.button_navlink_customers_css).click()

    def click_customers_navmenu_option(self):
        self.driver.find_element_by_xpath(self.button_option_customers_xpath).click()

    def click_addnew_custumer_button(self):
        self.driver.find_element_by_css_selector(self.button_addnew_customer_css).click()

