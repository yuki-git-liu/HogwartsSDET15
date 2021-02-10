# coding = utf-8
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    def setup(self):
        desired_caps = {"platformName": "Android",
                        "platformVersion": "6.0",
                        "deviceName": "emulator-5554",
                        "appPackage": "com.tencent.wework",
                        "appActivity": ".login.controller.LoginWxAuthActivity",
                        "noReset": "true",
                        "dontStopAppOnReset": "true",
                        "skipDeviceInitialization": "ture",
                        "skipServerInstallation": "ture"
                        }
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.find_element_by_id("com.tencent.wework:id/a59").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id("com.tencent.wework:id/cjf").click()
        self.driver.implicitly_wait(5)

    def teardown(self):
        self.driver.quit()
