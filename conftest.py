import pytest
from utils.driver_factory import get_driver

@pytest.fixture(params=["chrome", "firefox", "edge"])
def driver(request):
    driver = get_driver(request.param)
    driver.maximize_window()
    yield driver
    driver.quit()
