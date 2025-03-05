from selenium.webdriver.common.by import By

from Utilities import ConfigReader


class CarBase():

    def __init__(self, driver):
        self.driver = driver


    def get_title(self, locator):
        global title
        if str(locator).endswith("_XPATH"):
            title = self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_CSS"):
            title = self.driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_ID"):
            title = self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_TAG_NAME"):
            title = self.driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_NAME_"):
            title = self.driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_CLASS_NAME"):
            title = self.driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)).text
        elif str(locator).endswith("_LINK_TEXT"):
            title = self.driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)).text
        elif str(locator).endswith("PARTIAL_LINK_TEXT_"):
            title = self.driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator)).text

        return title

    def getCarNameandPrices(self, carName_locator, carPrices_locator):
        carNames = self.driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", carName_locator))
        carPrices = self.driver.find_elements(By.XPATH, ConfigReader.readConfig("locators", carPrices_locator))
        existing_carCount = len(carPrices)
        print(existing_carCount)
        for i in range(0, existing_carCount):
            print(carNames[i].text+ "-------Prices are-------" + carPrices[i].text)