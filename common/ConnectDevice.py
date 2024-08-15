import uitest
from common.Checker import checker
#from common.Base import Base
from smarthome.Log import logger


class UiAutomatorException(Exception):
    '''
    测试无法执行
    '''
    def __init__(self, messages):
        self.messages = messages
class ConnectDevice:

    def __init__(self, device_id=""):
        self.device = uitest.Device()
        if "?" in device_id:
            device_id = ""
        if device_id == "":
            self.device_id = ""
        else:
            self.device_id = "-s %s" % device_id

    @checker
    def create_assert_message(self, *args):
        if len(args) > 0:
            fail_reason = args[0]

            # attribute_value = getattr(args, 'attribute', 'Default Value')

            # print(attribute_value)  # 输出: This is an attribute
            # logger.error('fail reason {}'.format(str(e)))
            fail_result = {"message":fail_reason}

            return fail_result


    def getUdid(self):
        """
        # 获取udid ，判断设备是否连接
        :return:
        """
        try:
            return self.device.getUdid()
        except Exception as e:
            self.create_assert_message(e)

    def getDeviceState(self):
        """
        获取设备状态： offline | bootloader | device
        :return:
        """
        try:
            return self.device.getDeviceState()
        except Exception as e:
            self.create_assert_message(repr(e))

    def shell(self, args):
        """
        注意：用完需要关闭 close()
        :return:
        """
        try:
            return self.device.shell(args)
        except Exception as e:
            self.create_assert_message(repr(e))

    def force_stop(self, packageName):
        """
        退出app，类似于kill掉进程
        usage: quitApp("com.android.settings")
        :param packageName:
        :return:
        """
        try:
            self.device.force_stop(packageName)
        except Exception as e:
            self.create_assert_message(repr(e))

    def getMemTotal(self):
        """
        获取内存总值
        :return:
        """
        try:
            return self.device.getMemTotal()
        except Exception as e:
            self.create_assert_message(repr(e))

    def screenshot(self, fileName=None):
        """
        截图，保存到脚本"tmp\screenshot"目录里
        usage: adb.screenchot('screenshot.png')
        win 7不自动创建文件夹，所有要先判断然后创建
        :param fileName:
        :return:
        """
        try:
            self.device.screenshot(fileName)
        except Exception as e:
            self.create_assert_message(repr(e))

    def reboot(self):
        """
        重启设备
        :return:
        """
        try:
            self.device.reboot()
        except Exception as e:
            self.create_assert_message(repr(e))

    def getAppStartTotalTime(self, component):
        """
        获取启动应用所花时间
        usage: getAppStartTotalTime("com.android.settings/.Settings")
        :param component:
        :return:
        """
        try:
            return self.device.getAppStartTotalTime(component)
        except Exception as e:
            self.create_assert_message(repr(e))


    @checker
    def start_app(self, packageName):
        """
        启动一个应用
        usage: start_app("com.android.settings")
        :param packageName:
        :return:
        """
        try:
            self.device.start_app(packageName)
        except Exception as e:
            self.create_assert_message(e)


    def sendKeyEvent(self, keycode):
        """
        发送一个按键事件
        args:
        - keycode -:
        http://developer.android.com/reference/android/view/KeyEvent.html
        usage: sendKeyEvent(keycode.HOME)
        :param keycode:
        :return:
        """
        try:
            self.device.sendKeyEvent(keycode)
        except Exception as e:
            self.create_assert_message(repr(e))

    def longPressKey(self, keycode):
        """
        发送一个按键长按事件，Android 4.4以上
        usage: longPressKey(keycode.HOME)
        :param keycode:
        :return:
        """
        try:
            self.device.longPressKey(keycode)
        except Exception as e:
            self.create_assert_message(repr(e))

    def click_element(self, element):
        """
        点击元素
        usage: click_element(Element().findElementByName(u"计算器"))
        :param element:
        :return:
        """
        try:
            self.device.click_element(element)
        except Exception as e:
            self.create_assert_message(repr(e))

    def click(self, x, y=None):
        """
        发送触摸点击事件
        usage: click(0.5, 0.5) 点击屏幕中心位置
        """
        try:
            self.device.click(x, y)
        except Exception as e:
            self.create_assert_message(repr(e))


    def swipe(self, start_ratioWidth, start_ratioHigh, end_ratioWidth, end_ratioHigh, duration=" "):
        """
        发送滑动事件，Android 4.4以上可选duration(ms)
        usage: swipe(0.9, 0.5, 0.1, 0.5) 左滑
        :param start_ratioWidth:
        :param start_ratioHigh:
        :param end_ratioWidth:
        :param end_ratioHigh:
        :param duration:
        :return:
        """
        try:
            self.device.swipe(start_ratioWidth, start_ratioHigh, end_ratioWidth, end_ratioHigh, duration)
        except Exception as e:
            self.create_assert_message(repr(e))

    def swipeToLeft(self):
        """
        左滑屏幕
        :return:
        """
        try:
            self.device.swipeToLeft()
        except Exception as e:
            self.create_assert_message(repr(e))

    def swipeToRight(self):
        """
        右滑屏幕
        :return:
        """
        try:
            self.device.swipeToRight()
        except Exception as e:
            self.create_assert_message(repr(e))

    def swipeToUp(self):
        """
        上滑屏幕
        :return:
        """
        try:
            self.device.swipeToUp()
        except Exception as e:
            self.create_assert_message(repr(e))

    def swipeToDown(self):
        """
        下滑屏幕
        :return:
        """
        try:
            self.device.swipeToDown()
        except Exception as e:
            self.create_assert_message(repr(e))

    def click_long(self, x, y,duration=None):
        """
        长按屏幕的某个坐标位置, Android 4.4及以上
        usage: click_long(500, 600)
               click_long(0.5, 0.5)
        :param x:
        :param y:
        :param duration:
        :return:
        """
        try:
            self.device.click_long(x, y,duration)
        except Exception as e:
            self.create_assert_message(repr(e))

    def clear_text(self, number):
        """
        删除文本框内容，入参：删除次数
        :param number:
        :return:
        """
        try:
            self.device.clear_text(number)
        except Exception as e:
            self.create_assert_message(repr(e))

    def setText(self, string):
        """
        发送一段文本，只能包含英文字符和空格
        usage: setText("i am unique")
        :param string:
        :return:
        """
        try:
            self.device.setText(string)
        except Exception as e:
            self.create_assert_message(repr(e))

    def get_meminfo_heap(self, packageName):
        """
        获取内存,并写入到txt中记录
        :param packageName:
        :return:
        """
        try:
            self.device.get_meminfo_heap(packageName)
        except Exception as e:
            self.create_assert_message(repr(e))

    def logcat_pull(self, **msg):
        """
        取日志,入参：str1，str2
        :param msg:
        :return:
        """
        try:
            self.device.logcat_pull(**msg)
        except Exception as e:
            self.create_assert_message(repr(e))

    def screenshot_err_no_open(self, **msg):
        """
        可疑情况截图不打开，入参：str1，str2自定义错误信息，截图后缀名
        :param msg:
        :return:
        """
        try:
            self.device.screenshot_err_no_open(**msg)
        except Exception as e:
            self.create_assert_message(repr(e))

    def push(self, local, remote, override=True):
        """
        push电脑本地文件到手机
        :param local:
        :param remote:
        :param override:
        :return:
        """
        try:
            self.device.push(local, remote, override=True)
        except Exception as e:
            self.create_assert_message(repr(e))

    def pull(self, remote, local=''):
        """
        pull手机里的文件到电脑本地
        :param remote:
        :param local:
        :return:
        """
        try:
            self.device.pull(remote, local)
        except Exception as e:
            self.create_assert_message(repr(e))

    def screen_on(self):
        """
        点亮解锁屏幕
        :return:
        """
        try:
            self.device.screen_on()
        except Exception as e:
            self.create_assert_message(repr(e))

    def screen_off(self):
        """
        熄灭屏幕
        :return:
        """
        try:
            self.device.screen_off()
        except Exception as e:
            self.create_assert_message(repr(e))

    def is_screen_on(self):
        """
        判断屏幕是否点亮
        :return:
        """
        try:
            return self.device.is_screen_on()
        except Exception as e:
            self.create_assert_message(repr(e))

    def is_wifi_on(self):
        """
        判断WiFi是否打开
        :return:
        """
        try:
            return self.device.is_wifi_on()
        except Exception as e:
            self.create_assert_message(repr(e))

    def find_icon(self, icon_name, confidence=None):
        """
        根据图片名判断当前页面
        usage:  find_icon('icon/print_cancel.720x1280.jpg', '')
                find_icon('icon/print_cancel.720x1280.jpg', 0.9)

        :param icon_name: 本地图片路径，待查找的图
        :param confidence: 相似度
        :return: 位置坐标
        """
        try:
            return self.device.find_icon(icon_name, confidence)
        except Exception as e:
            self.create_assert_message(repr(e))

    def find_icon_click(self, icon_name, confidence=None):
        """
        点击找到的图片
        usage:  find_icon_click('icon/print_cancel.720x1280.jpg', '')
                find_icon_click('icon/print_cancel.720x1280.jpg', 0.9)
        :param icon_name: 本地图片路径，待查找的图
        :param confidence: 相似度
        :return: True 或者 False
        """
        try:
            return self.device.find_icon_click(icon_name, confidence)
        except Exception as e:
            self.create_assert_message(repr(e))

    def back(self):
        """
        返回
        :return:
        """
        try:
            self.device.back()
        except Exception as e:
            self.create_assert_message(repr(e))

    def home(self):
        """
        HOME键
        :return:
        """
        try:
            self.device.home()
        except Exception as e:
            self.create_assert_message(e)

    def get_allnet(self, packageName):
        """
        获取指定包名的应用的wifi流量消耗, 目前只针对部分机型
        :param packageName:
        :return: 使用流量：单位m：get_allnet('com.lzz.test')[4]
        :usage: allnet = get_allnet('com.lzz.test')
        # print('网络数据：', allnet[2]+allnet[3], 'kb','≈', allnet[4],'m')
        """
        try:
            return self.device.get_allnet(packageName)
        except Exception as e:
            self.create_assert_message(repr(e))

    def is_root(self):
        """
        判断设备是否root
        :return:
        """
        try:
            return self.device.is_root()
        except Exception as e:
            self.create_assert_message(repr(e))

    def get_boot_time(self):
        """
        获取设备开机时间
        :return:设备开机时间
        """
        try:
            return self.device.get_boot_time()
        except Exception as e:
            self.create_assert_message(repr(e))

    def get_has_boot_time(self, show='s'):
        """
        获取设备已开机时间
        :return:
        """
        try:
            return self.get_has_boot_time(show)
        except Exception as e:
            self.create_assert_message(repr(e))
































