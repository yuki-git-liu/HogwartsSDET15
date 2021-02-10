# coding = utf-8
from selenium.webdriver import ActionChains
from test.base import Base
from time import sleep


class Test(Base):
    def test_alert(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame("iframeResult")

        drag = self.driver.find_element_by_id('draggable')
        drop = self.driver.find_element_by_id('droppable')
        action = ActionChains(self.driver)
        action.drag_and_drop(drag, drop).perform()
        sleep(2)
        print("点击 alert 确认")
        self.driver.switch_to.alert.accept()

        self.driver.switch_to.default_content()

        self.driver.find_element_by_id("submitBTN").click()
        sleep(3)
