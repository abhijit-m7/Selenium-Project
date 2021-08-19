import configparser

config = configparser.RawConfigParser()
config.read("Configurations/config.ini")

class ReadConfig:

    @staticmethod #it is used to use class methods without creating object
    def baseUrl():
        url = config.get('common info', 'baseUrl')
        return url

    @staticmethod #it is used to use class methods without creating object
    def username():
        username = config.get('common info', 'username')
        return username

    @staticmethod #it is used to use class methods without creating object
    def password():
        password = config.get('common info', 'password')
        return password
