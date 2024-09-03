import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

capabilities_options = UiAutomator2Options().set_capability('platformName', 'Android')
capabilities_options.set_capability('automationName', 'uiautomator2')
capabilities_options.set_capability('deviceName', 'Android')
capabilities_options.set_capability('appPackage', 'com.android.settings')
capabilities_options.set_capability('appActivity', '.Settings')
capabilities_options.set_capability('language', 'en')
capabilities_options.set_capability('locale', 'US')

#appium_server_url = 'http://localhost:4723/wd/hub'
appium_server_url = 'http://127.0.0.1:4723'


@pytest.fixture()
def driver():
    app_driver = webdriver.Remote(appium_server_url, options = capabilities_options)
    yield app_driver
    if app_driver:
        app_driver.quit()

def test_find_battery(driver) -> None:
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
    sleep(5)
