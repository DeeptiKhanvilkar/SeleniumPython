import time

import pytest

from Pages.CarBase import CarBase
from Pages.HomePage import HomePage
from TestCases.BaseTest import BaseTest
from Utilities.ExcelReader import get_all_data
from Utilities.LogUtil import Logger

log = Logger()
class Test_CarWale(BaseTest):

    @pytest.mark.skip
    def test_gotoNewCar(self):
        log.get_logger().info("*********Go to New Car**********")
        home = HomePage(self.driver)
        home.gotoNewCars()
        time.sleep(3)
        assert home.gotoNewCars().get_title()

    @pytest.mark.parametrize("carBrand, carTitle", get_all_data("..//Excel/TestData.xlsx", "SelectCars"))
    def test_selectCars(self, carBrand, carTitle):
        log.get_logger().info("********* Inside Select Cars ************** ")
        home = HomePage(self.driver)
        carbase = CarBase(self.driver)
        if carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = carbase.get_title("carTitle_CSS")
            print(carTitle,  title)
            assert title == carTitle, "Title is not as expected"
            time.sleep(2)
            carbase.getCarNameandPrices("carName_XPATH", "carPrice_XPATH")
        elif carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = carbase.get_title("carTitle_CSS")
            assert title == carTitle, "Title is not as expected"
            time.sleep(2)
            carbase.getCarNameandPrices("carName_XPATH", "carPrice_XPATH")
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = carbase.get_title("carTitle_CSS")
            assert title == carTitle, "Title is not as expected"
            time.sleep(2)
            carbase.getCarNameandPrices("carName_XPATH", "carPrice_XPATH")
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = carbase.get_title("carTitle_CSS")
            assert title == carTitle, "Title is not as expected"
            time.sleep(2)
            carbase.getCarNameandPrices("carName_XPATH", "carPrice_XPATH")



    @pytest.mark.parametrize("carBrand, carTitle", get_all_data("..//Excel/TestData.xlsx", "SelectCars"))
    def test_printCarNamesandPrices(self, carBrand, carTitle):
        log.get_logger().info("********* Inside Select Cars ************** ")
        home = HomePage(self.driver)
        carbase = CarBase(self.driver)
        if carBrand == "Toyota":
            home.gotoNewCars().selectToyota()
            title = carbase.get_title("carTitle_CSS")
            print(carTitle,  title)
            assert title == carTitle, "Title is not as expected"
            time.sleep(2)
            carbase.getCarNameandPrices("carName_XPATH", "carPrice_XPATH")
        elif carBrand == "BMW":
            home.gotoNewCars().selectBMW()
            title = carbase.get_title("carTitle_CSS")
            assert title == carTitle, "Title is not as expected"
            time.sleep(2)
            carbase.getCarNameandPrices("carName_XPATH", "carPrice_XPATH")
        elif carBrand == "Honda":
            home.gotoNewCars().selectHonda()
            title = carbase.get_title("carTitle_CSS")
            assert title == carTitle, "Title is not as expected"
            time.sleep(2)
            carbase.getCarNameandPrices("carName_XPATH", "carPrice_XPATH")
        elif carBrand == "Hyundai":
            home.gotoNewCars().selectHyundai()
            title = carbase.get_title("carTitle_CSS")
            assert title == carTitle, "Title is not as expected"
            time.sleep(2)
            carbase.getCarNameandPrices("carName_XPATH", "carPrice_XPATH")






