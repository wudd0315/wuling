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




class Element():
    """
    设备操作接口
    """
    def __init__(self):
        self.element = uitest.Element()
        self.fail_reason = None
        self.fail_result = {}

    @checker
    def create_assert_message(self, *args, **kwargs):
        if len(args) > 0:
            self.fail_reason = args[0]
            self.fail_result.update({"message": self.fail_reason})

            return self.fail_result

    def click(self, attrib=None, name=None, **msg):
        """
        同属性单个元素，返回是否存在
        :args:
        - attrib - node节点中某个属性
        - name - node节点中某个属性对应的值
        用法：d(resourceId='com.android.calculator2:id/op_mul')
             d(text='8')
             d(content_desc='乘')
        """
        try:
            return self.element.click(attrib, name, **msg)
        except Exception as e:
            self.create_assert_message(repr(e))

    def d(self, attrib=None, name=None, **msg):
        """
         同属性单个元素，返回单个坐标元组，(x, y)
        用法：d(resourceId='com.android.calculator2:id/op_mul')
             d(text='8')
             d(content_desc='乘')
        :param attrib: node节点中某个属性
        :param name: node节点中某个属性对应的值
        :param msg:
        :return:
        """
        try:
            return self.element.d(attrib, name, **msg)
        except Exception as e:
            self.create_assert_message(repr(e))

    def swipe_find(self, **msg):
        """
        msg['resourceId'] != ''
        msg['text'] != ''
        msg['content_desc'] != ''
        msg['textContains'] != ''
        下滑屏幕,找到元素就点击
        :param msg: 字典类型
        :return:
        """
        try:
            return self.element.swipe_find(**msg)
        except Exception as e:
            self.create_assert_message(repr(e))

    def d_right_corner(self, attrib=None, name=None, **msg):
        """
        同属性单个元素，返回单个 右下角 坐标元组，(x, y)
        用法：d(resourceId='com.android.calculator2:id/op_mul')
             d(text='8')
             d(content_desc='乘')
        :param attrib: node节中某个属性点
        :param name: node节点中某个属性对应的值
        :param msg:
        :return:坐标元组（x,y)
        """
        try:
            return self.element.d_right_corner(attrib, name, **msg)
        except Exception as e:
            self.create_assert_message(repr(e))

    def info(self, attrib=None, name=None, **msg):
        """
        同属性单个元素，返回单个控件所有属性
        :param attrib: node节点中某个属性
        :param name: node节点中某个属性对应的值
        :param msg:
        :return:
        用法：d(resourceId='com.android.calculator2:id/op_mul')
             d(text='8')
             d(content_desc='乘')
        """
        try:
            return self.info(attrib, name, **msg)
        except Exception as e:
            self.create_assert_message(repr(e))

    def exists(self, attrib=None,name=None, **msg):
        """
        同属性单个元素，返回boolean
        :param attrib: node节点中某个属性
        :param name: node节点中某个属性对应的值
        :param msg:
        :return:
        用法：d(('resourceId,'com.android.calculator2:id/op_mul'))
        """
        try:
            return self.element.exists(attrib, name, **msg)
        except Exception as e:
            self.create_assert_message(repr(e))



    def findElementByName(self, name):
        """
        通过元素名称定位单个元素
        usage: findElementByName(u"设置")
        :param name:
        :return:
        """
        try:
            return self.element.findElementByName(name)
        except Exception as e:
            self.create_assert_message(repr(e))




    def findElementsByName(self, name):
        """
        通过元素名称定位多个相同text的元素
        :param name:
        :return:
        """
        try:
            return self.element.findElementByName(name)
        except Exception as e:
            self.create_assert_message(repr(e))

    def findElementByClass(self, className):
        """
        通过元素类名定位单个元素
        usage: findElementByClass("android.widget.TextView")
        :param className:
        :return:
        """
        try:
            return self.element.findElementByClass(className)
        except Exception as e:
            self.create_assert_message(repr(e))

    def findElementsByClass(self,className):
        """
        通过元素类名定位多个相同class的元素
        :param className:
        :return:
        """
        try:
            return self.element.findElementsByClass(className)
        except Exception as e:
            self.create_assert_message(repr(e))

    def findElementById(self, id):
        """
        通过元素的resource-id定位单个元素
        usage: findElementsById("com.android.deskclock:id/imageview")
        :param id:resource-id
        :return:
        """
        try:
            return self.element.findElementById(id)
        except Exception as e:
            self.create_assert_message(repr(e))

    def findElementsById(self, id):
        """
        通过元素的resource-id定位多个相同id的元素
        :param id:
        :return:
        """
        try:
            return self.element.findElementsById(id)
        except Exception as e:
            self.create_assert_message(repr(e))

    def findElementByContentDesc(self, contentDesc):
        """
        通过元素的content-desc定位单个元素
        :param contentDesc:
        :return:
        """
        try:
            return self.element.findElementByContentDesc(contentDesc)
        except Exception as e:
            self.create_assert_message(repr(e))

    def findElementsByContentDesc(self, contentDesc):
        """
        通过元素的content-desc定位多个相同的元素
        :param contentDesc:
        :return:
        """
        try:
            return self.element.findElementsByContentDesc(contentDesc)
        except Exception as e:
            self.create_assert_message(repr(e))

    def getElementBoundByName(self, name):
        """
        通过元素名称获取单个元素的区域
        :param name:
        :return:
        """
        try:
            return self.element.getElementBoundByName(name)
        except Exception as e:
            self.create_assert_message(repr(e))

    def getElementBoundsByName(self, name):
        """
        通过元素名称获取多个相同text元素的区域
        :param name:
        :return:
        """
        try:
            return self.element.getElementBoundsByName(name)
        except Exception as e:
            self.create_assert_message(repr(e))

    def getElementBoundByClass(self, className):
        """
        通过元素类名获取单个元素的区域
        :param className:
        :return:
        """
        try:
            return self.element.getElementBoundByClass(className)
        except Exception as e:
            self.create_assert_message(repr(e))

    def getElementBoundsByClass(self,className):
        """
        通过元素类名获取多个相同class元素的区域
        :param className:
        :return:
        """
        try:
            return self.element.getElementBoundsByClass(className)
        except Exception as e:
            self.create_assert_message(repr(e))

    def getElementBoundByContentDesc(self, contentDesc):
        """
        通过元素content-desc获取单个元素的区域
        :param contentDesc:
        :return:
        """
        try:
            return self.element.getElementBoundByContentDesc(contentDesc)
        except Exception as e:
            self.create_assert_message(repr(e))

    def getElementBoundsByContentDesc(self, contentDesc):
        """
        通过元素content-desc获取多个相同元素的区域
        :param contentDesc:
        :return:
        """
        try:
            return self.element.getElementBoundsByContentDesc(contentDesc)
        except Exception as e:
            self.create_assert_message(repr(e))

    def getElementBoundById(self, id):
        """
        通过元素id获取单个元素的区域
        :param id:
        :return:
        """
        try:
            return self.element.getElementBoundById(id)
        except Exception as e:
            self.create_assert_message(repr(e))

    def getElementBoundsById(self, id):
        """
        通过元素id获取多个相同resource-id元素的区域
        :param id:
        :return:
        """
        try:
            return self.element.getElementBoundsById(id)
        except Exception as e:
            self.create_assert_message(repr(e))

    def isElementsCheckedByName(self, name):
        """
        通过元素名称判断checked的布尔值，返回布尔值列表
        :param name:
        :return:
        """
        try:
            return self.element.isElementsCheckedByName(name)
        except Exception as e:
            self.create_assert_message(repr(e))

    def isElementsCheckedById(self, id):
        """
        通过元素id判断checked的布尔值，返回布尔值列表
        :param id:
        :return:
        """
        try:
            return self.element.isElementsCheckedById(id)
        except Exception as e:
            self.create_assert_message(repr(e))

    def isElementsCheckedByClass(self, className):
        """
        通过元素类名判断checked的布尔值，返回布尔值列表
        :param className:
        :return:
        """
        try:
            return self.element.isElementsCheckedByClass(className)
        except Exception as e:
            self.create_assert_message(repr(e))









