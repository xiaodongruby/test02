import time
import pytest
from appium import webdriver
class TestAddContact:
    def setup(self):
        # 创建一个字典，包装相应的启动参数
        desired_caps = dict()
        # 需要连接的手机的平台(不限制大小写)
        desired_caps['platformName'] = 'Android'
        # 需要连接的手机的版本号(比如 5.2.1 的版本可以填写 5.2.1 或 5.2 或 5 ，以此类推)
        desired_caps['platformVersion'] = '5.1'
        # 需要连接的手机的设备号(andoird平台下，可以随便写，但是不能不写)
        desired_caps['deviceName'] = 'huawei p30'
        # 需要启动的程序的包名
        desired_caps['appPackage'] = 'com.android.contacts'
        # 需要启动的程序的界面名
        desired_caps['appActivity'] = '.activities.PeopleActivity'
        # 让系统不再重置引用
        desired_caps['noReset'] = True

        # 连接appium服务器
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


    def teardown(self):
        time.sleep(3)
        self.driver.quit()

    @pytest.mark.parametrize(("name", "phone"), [("zhangsan", "188888888"), ("lisi", "199999999")])
    def test_add_contact(self, name, phone):
        self.driver.find_element_by_id("com.android.contacts:id/floating_action_button").click()
        self.driver.find_element_by_xpath("//*[@text='姓名']").send_keys(name)
        self.driver.find_element_by_xpath("//*[@text='电话']").send_keys(phone)
        self.driver.find_element_by_class_name("android.widget.ImageButton").click()

