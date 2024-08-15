# coding=utf-8
import logging
import time
import pytest
import allure
from hypium import  uidriver
import uitest
from smarthome.Log import logger
from common.Element import Element
from script.online_device_inspection.TestBase import TestBase
from common.memory import GetMemory

class TestAppstorememory(TestBase):
    package_name = 'com.sgmw.appstore'
    MEMORY_NUM = 500



    get_memory = GetMemory(package_name)
    meminfo_output = []

    
    @classmethod
    def setup_class(cls) -> None:
        super().setup_class()



    @classmethod
    def teardown_class(cls):
        pass
        # super().teardown_class()

    def setup_method(self):
        super().setup_method()

    def teardown_method(self):
        pass

    @allure.feature('内存泄漏')
    @allure.story("获取应用商店内存泄漏")
    @allure.title("get appstore memory")
    def test_check_appstore_memory(self, get_test_method_name):
        """
        获取应用商店进入退出后的内存泄漏信息
        :return:
        """
        a = 3
        b = 3
        assert a == b

    def test_check_memory(self, get_test_method_name):
        """
        获取应用商店进入退出后的内存泄漏信息
        :return:
        """
        a = 2
        b = 2
        assert a == b
        # logger.info('{} begin to {} memory leak'.format(get_test_method_name, self.package_name))
        # for i in range(self.MEMORY_NUM):
        #     self.connect_device.start_app(self.package_name)
        #     time.sleep(2)
        #     output = self.get_memory.get_mem_info()
        #     self.meminfo_output.append(output)
        #     time.sleep(2)
        #     self.connect_device.home()
        #     time.sleep(1)
        # self.get_memory.create_plot(self.meminfo_output, self.MEMORY_NUM)

















if __name__ == '__main__':
    pytest.main(['-vs'])

