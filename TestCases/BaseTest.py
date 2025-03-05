import pytest


@pytest.mark.usefixtures("get_browser", "log_on_failure")
class BaseTest():
    pass