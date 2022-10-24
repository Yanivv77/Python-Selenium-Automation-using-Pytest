import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

from conftest import get_browser


def get_data():
    return [
        ("trainer@way2automation.com", "kjsdfbksdf"),
        ("java@way2automation.com", "sdf")
        #("info@way2automation.com", "sdfsdf")
    ]

"""
def setup_function():
    global driver
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    driver.get("http://facebook.com")
    driver.maximize_window()


def teardown_function():
    driver.quit()
"""

@pytest.fixture()
def log_on_failure(request, get_browser):
    yield
    item = request.node
    driver = get_browser
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)

@pytest.mark.usefixtures("log_on_failure")
@pytest.mark.parametrize("username,password", get_data(), )
def test_dologin(username, password , get_browser):
    driver = get_browser
    driver.find_element(By.ID, "email").send_keys(username)
    driver.find_element(By.ID, "pass").send_keys(password)
    # assert 1 == 2
    # allure.attach(driver.get_screenshot_as_png(), name="dologin", attachment_type=AttachmentType.PNG)



