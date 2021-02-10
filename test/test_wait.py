# coding = utf-8
import shelve
from time import sleep
from test.base import Base
from selenium.webdriver.common.by import By
import os


class Test(Base):

    def test_cookie(self):
        # get_cookies() 可以获取当前打开的页面的cookies 信息
        # add_cookie() 可以把cookie 添加到当前的页面中去
        cookies = self.driver.get_cookies()
        print(cookies)

        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            if 'expiry' in cookie.keys():
                cookie.pop('expiry')
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        sleep(3)

    def test_shelve(self):
        # shelve python 内置模块，专门用来对数据进行持久化存储的库，相当于小型的数据库
        # 可以通过 key，value 来把数据保存到shelve中
        # 读取cookie
        db = shelve.open("cookies")
        cookies = db['cookie']
        db.close()
        # 利用读取的cookie 完成登录操作
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        for cookie in cookies:
            self.driver.add_cookie(cookie)

        self.driver.refresh()
        # 找到"导入联系人"按钮
        self.driver.find_element(By.CSS_SELECTOR, ".index_service_cnt_itemWrap:nth-child(2)").click()
        # 上传
        self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_uploadInputMask").send_keys(
            "/Users/juanxu/Downloads/mydata.xlsx")
        # 验证 上传文件名
        filename = self.driver.find_element(By.CSS_SELECTOR, ".ww_fileImporter_fileContainer_fileNames").text
        assert "mydata.xlsx" == filename
        sleep(3)
