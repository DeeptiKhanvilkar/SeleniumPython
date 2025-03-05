from argparse import Action
from itertools import dropwhile

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import ConfigReader
from Utilities.LogUtil import Logger
log = Logger()
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click(self, locator):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_TAG_NAME"):
            self.driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_NAME_"):
            self.driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("_LINK_TEXT"):
            self.driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)).click()
        elif str(locator).endswith("PARTIAL_LINK_TEXT_"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator)).click()
        log.get_logger().info("Clicked on the element: " + str(locator))

    def send_text(self, locator, text):
        if str(locator).endswith("_XPATH"):
            self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator)).send_keys(text)
        elif str(locator).endswith("_CSS"):
            self.driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator)).send_keys(text)
        elif str(locator).endswith("_ID"):
            self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator)).send_keys(text)
        elif str(locator).endswith("_TAG_NAME"):
            self.driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator)).send_keys(text)
        elif str(locator).endswith("_NAME_"):
            self.driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator)).send_keys(text)
        elif str(locator).endswith("_CLASS_NAME"):
            self.driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator)).send_keys(text)
        elif str(locator).endswith("_LINK_TEXT"):
            self.driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator)).send_keys(text)
        elif str(locator).endswith("PARTIAL_LINK_TEXT_"):
            self.driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator)).send_keys(text)
        log.get_logger().info("Sent text to the element: " + str(locator))

    def select_dropdown(self, locator, value):
        global dropdown
        if str(locator).endswith("_XPATH"):
            dropdown = self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            dropdown = self.driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            dropdown = self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_TAG_NAME"):
            dropdown = self.driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_NAME_"):
            dropdown = self.driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CLASS_NAME"):
            dropdown = self.driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_LINK_TEXT"):
            dropdown = self.driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("PARTIAL_LINK_TEXT_"):
            dropdown = self.driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator))
        select = Select(dropdown)
        select.select_by_visible_text(value)
        log.get_logger().info("Selected the element: " + str(locator))


    def mouse_hover(self, locator):
        global element
        if str(locator).endswith("_XPATH"):
            element = self.driver.find_element(By.XPATH, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CSS"):
            element = self.driver.find_element(By.CSS_SELECTOR, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_ID"):
            element = self.driver.find_element(By.ID, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_TAG_NAME"):
            element = self.driver.find_element(By.TAG_NAME, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_NAME_"):
            element = self.driver.find_element(By.NAME, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_CLASS_NAME"):
            element = self.driver.find_element(By.CLASS_NAME, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("_LINK_TEXT"):
            element = self.driver.find_element(By.LINK_TEXT, ConfigReader.readConfig("locators", locator))
        elif str(locator).endswith("PARTIAL_LINK_TEXT_"):
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, ConfigReader.readConfig("locators", locator))
        action = ActionChains(self.driver)
        action.move_to_element(element).perform()


