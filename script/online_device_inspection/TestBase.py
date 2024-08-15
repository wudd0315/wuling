import time

import uitest

# from uitest import Device,Keycode,Element
from smarthome.Log import logger
from common.Checker import checker
from common.Element import Element
from common.ConnectDevice import ConnectDevice
from common.memory import GetMemory
class TestBase:
    connect_device = None
    element = None
    device_status = None
    instance = None


    @classmethod
    def setup_class(cls) -> None:
        pass
        # cls.connect_device = ConnectDevice()
        # cls.element = Element()
        # # cls.keycode = Keycode()
        # cls.device_connect_status = cls.connect_device.getUdid()
        # #创建类的实例
        # instance = cls()
        # #调用实例方法
        # instance.__check_device_connect_status()
        # cls.connect_device.home()




    # @checker
    # def __check_device_connect_status(self):
        # if self.device_connect_status == '' or self.device_connect_status is None:
        #     alert_data = {'message': f'Device Connect Fail!'}
        #     logger.error('Device Connect Fail!'"")
        #     return alert_data





    @classmethod
    def teardown_class(cls):
        pass
        # for i in range(5):
        #     cls.connect_device.back()
        #     time.sleep(0.3)
        # cls.connect_device.home()


    def setup_method(self):
        logger.info('======================= start setUp ')

    def teardown_method(self):
        pass












