import configparser


def readConfig(section, key):

    config = configparser.ConfigParser()
    config.read("..//ConfigurationData//conf.ini")
    return config.get(section, key)