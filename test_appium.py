import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options
from time import sleep

capabilities = dict(
    platformName='Android',
    automationName='uiautomator2',
    deviceName='Android',
    appPackage='com.android.settings',
    appActivity='.Settings',
    language='en',
    locale='US'
)
options =  UiAutomator2Options()
capabilities_options = options.load_capabilities(capabilities)

appium_server_url = 'http://localhost:4723'

@pytest.fixture()
def driver():
    app_driver = webdriver.Remote(appium_server_url, capabilities_options)
    yield app_driver
    if driver:
        driver.quit()

def test_find_battery(driver) -> None:
    el = driver.find_element(by=AppiumBy.XPATH, value='//*[@text="Battery"]')
    el.click()
    sleep(5)
