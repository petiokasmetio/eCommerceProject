from selenium import webdriver

class Login:

    textbox_username_id = 'Email'
    textbox_password_id = 'Password'
    button_login_css = 'button[type="submit"]'
    button_logout_css = 'a[href="/logout"]'
    url_loginpage = 'https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F'

    def __init__(self, driver):
        self.driver = driver

    def get_login_url(self):
        self.driver.get_url('https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F')

    def set_username(self, username):
        self.driver.find_element_by_id(self.textbox_username_id).clear()
        self.driver.find_element_by_id(self.textbox_username_id).send_keys(username)

    def set_password(self, password):
        self.driver.find_element_by_id(self.textbox_password_id).clear()
        self.driver.find_element_by_id(self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element_by_css_selector(self.button_login_css).click()

    def click_logout(self):
        self.driver.find_element_by_css_selector(self.button_logout_css).click()