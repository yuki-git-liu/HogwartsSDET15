# coding = utf-8

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

desired_caps = {"platformName": "Android",
                "platformVersion": "6.0",
                "deviceName": "emulator-5554",
                "appPackage": "com.tencent.wework",
                "appActivity": ".login.controller.LoginWxAuthActivity",
                "noReset": "true",
                # "dontStopAPPOnReset": "true",
                # "skipDeviceInitialization": "ture"
                }
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.find_element_by_id("com.tencent.wework:id/a59").click()
driver.implicitly_wait(5)
# driver.find_element_by_id("com.tencent.wework:id/cjf").click()
# driver.find_element_by_id("com.tencent.wework:id/igk").click()
# driver.find_element_by_id("com.tencent.wework:id/gy9").send_keys("测试")
# driver.quit()

window_rect = driver.get_window_rect()
width = window_rect['width']
height = window_rect['height']
x1 = int(width / 2)
y_start = int(height * 4 / 5)
y_end = int(height * 1 / 5)
TouchAction(driver).press(x=x1, y=y_start).wait(200).move_to(x=x1, y=y_end).release().perform()
