import os.path

import pytest
import allure
from common.ConnectDevice import ConnectDevice
import time
from smarthome.Log import logger

#用例失败后自动截图
@pytest.hookimpl(trylast=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    获取用例执行结果的钩子函数
    :param item: 测试用例对象
    :param call:测试用例的测试步骤
    :return:
    """
    outcome = yield
    report = outcome.get_result()
    if report.when == 'call' and report.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        with open("failures", mode) as f:
            if 'tmpir' in item.fixturenames:
                extra = " (%s)" % item.funcargs['tmpdir']
            else:
                extra = ''
                f.write(report.nodeid + extra + '\n')
            with allure.step('添加失败截图...'):
                pic_time = time.strftime('%Y%m%d_%H%M%S')
                pic_name = 'screenshot_{}.png'.format(pic_time)
                ConnectDevice().screenshot(pic_name)
                pic_path = os.getcwd() + os.sep + 'tmp' + os.sep + 'screenshot' + os.sep + pic_name
                # logger.info(pic_name)
                #file_path = r'C:\project\cheji\pythonProject1\script\online_device_inspection\tmp\screenshot\screenshot.png'
                allure.attach.file(pic_path, attachment_type=allure.attachment_type.PNG)


@pytest.fixture()
def get_test_method_name(request):
    _testMethodName = request.node.name
    yield _testMethodName
