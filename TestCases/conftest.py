import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from Utilities import ConfigReader


# @pytest.fixture(params=["chrome", "firefox"], scope= "function")
@pytest.fixture(params=["chrome"], scope= "function")
def get_browser(request):
    if "chrome" in request.param:
        driver = webdriver.Chrome()
    elif "firefox" in request.param:
        driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.get(ConfigReader.readConfig("base info", "baseURL"))
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst= True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_"+ rep.when, rep)
    return rep

@pytest.fixture()
def log_on_failure(request, get_browser):
    driver = get_browser
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), attachment_type=AttachmentType.PNG, name="Registration")