from Pages.BasePage import BasePage


class NewCarsPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def selectHyundai(self):
        self.click("hyundai_XPATH")

    def selectToyota(self):
        self.click("toyota_XPATH")

    def selectBMW(self):
        self.click("BMW_XPATH")


    def selectHonda(self):
        self.click("Honda_XPATH")

    def verifyTitle(self):
        self.get_title("allBrands_XPATH")
