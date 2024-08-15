
import subprocess
import time
import os
import matplotlib.pyplot as plt
import pyautogui
from smarthome.Log import logger
cmd = 'adb devices'
def get_command_result(cmd):
    sbp = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = sbp.communicate()
    return stdout.decode('utf-8')


def get_adb_device():
    cmd = 'adb devices'
    device_result = get_command_result(cmd)
    devices_list = [line.split('\t')[0] for line in device_result.strip().split('\n')[1:] if 'device' in line]
    return devices_list

def get_dir() -> str:
    dir_path = os.path.dirname(__file__).split('public')[0]
    return dir_path













