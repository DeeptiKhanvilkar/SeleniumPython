from Pages.BasePage import BasePage
from Pages.NewCarsPage import NewCarsPage


class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    def gotoNewCars(self):
        # self.driver.find
        self.mouse_hover("newCars_XPATH")
        self.click("findNewCars_XPATH")
        return NewCarsPage(self.driver)

    def gotoCompareCars(self):
        pass

    def gotoUsedCars(self):
        pass

