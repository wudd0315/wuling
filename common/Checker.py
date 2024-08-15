from smarthome.Log import logger
class TestFailException(Exception):
    """
    自定义异常，便于区分报错类型,能人为自造异常，退出测试结果
    """

def checker(func):
    def wrapper(*args, **kwargs):
        #len(args)表示该对象的属性是存在的
        if len(args) > 0:
            className = args[0].__class__.__name__
            funcName = func.__name__
            argsObj = args[0]
            #并不是所有的aw，都以类方法的方式存在的
            if className == 'str':
                argsValue = args
                className = ''
            else:
                argsValue = args[1:]
        else:
            className = ''
            funcName = ''
            argsValue = ''
            argsObj = ''
        logger.info("Begin to run %s.%s" % (className, funcName))
        #防止aw考虑不完善，导致代码报错
        try:
            ret = func(*args, **kwargs)
        except Exception as e:
            print(e)
            import traceback,re
            logger.info("错误提醒=======================错误提醒")
            logger.info(traceback.format_exc())
            logger.info("错误提醒==========================错误提醒")
            ret = False
        result = my_assert(argsObj, ret, funcName, argsValue)
        logger.info("%s.%s:%s" % (className, funcName, result))
        return result

    return wrapper

def my_assert(obj, expr, funcName, argsValue):
    """
    失败上报assert,中断脚本执行
    :param obj:
    :param expr:
    :param funcName:
    :param argsValue:
    :return:
    """
    if expr != None:
        msg = "方法:%s%s执行结果为%s，请滚动到上方日志中检查[error]标签日志" % (funcName, argsValue, expr)
        raise TestFailException(msg)
    return expr






