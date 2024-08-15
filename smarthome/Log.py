import logging
from logging import handlers


fmt = '[%(asctime)s] %(levelname)s %(message)s'
formatter = logging.Formatter(fmt)
logger = logging.getLogger('smarthome')
logger.setLevel(logging.INFO)
#创建一个输出日志到控制台的StreamHandler
hdr = logging.StreamHandler()
hdr.setFormatter(formatter)
#输出到文件
th = handlers.RotatingFileHandler(filename='smarthome.log', mode='w', encoding='utf-8') #往文件里写入
th.setFormatter(formatter)
logger.addHandler(th)
