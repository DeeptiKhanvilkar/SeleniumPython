from Pages.BasePage import BasePage


class HondaPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def numberOfCars(self):
        self.driver.find_element(By.CLASS, "o-brXWGL o-fznVqX o-fznVsN o-fznVmz o-fznVCp o-cpnuEd")