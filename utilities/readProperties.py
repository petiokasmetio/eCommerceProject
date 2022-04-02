import configparser

data_configuration = configparser.RawConfigParser()
data_configuration.read("C:\\Users\\Elitebook\\PycharmProjects\\eCommerce\\configurations\\config.ini")

class ReadDataConfiguraton:
    @staticmethod
    def get_application_url():
        base_login_url = data_configuration.get('common info', 'base_login_url')
        return base_login_url

    @staticmethod
    def get_username_data():
        username_data = data_configuration.get('common info', 'username_data')
        return username_data

    @staticmethod
    def get_password_data():
        password_data = data_configuration.get('common info', 'password_data')
        return password_data