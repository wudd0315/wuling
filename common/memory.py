import os
import subprocess
import matplotlib.pyplot as plt
import re
from common.Tools import get_command_result
class GetMemory:
    def __init__(self, package):
        self.package_name = package

    def get_mem_info(self):
        try:
            # 使用subprocess.check_output执行adb命令
            output = subprocess.check_output(
                ['adb', 'shell', 'dumpsys', 'meminfo', self.package_name],
                stderr=subprocess.STDOUT,  # 将标准错误重定向到标准输出
                text=True  # 设置编码方式为文本
            )
            total_line = re.search(r'TOTAL\s+(\d+)', output)
            if total_line:
                # 返回总内存值
                return int(total_line.group(1))
        except subprocess.CalledProcessError as e:
            print("错误：", e.output)
            return None

    def create_plot(self, total_memory_values, memory_num):
        project_name = None
        plt.plot(total_memory_values)
        plt.xlabel('Iteration')
        plt.ylabel('Total Memory (KB)')
        title_name = '{} Memory Curve over {} iterations'.format(self.package_name, memory_num)
        plt.title(title_name)
        current_path = os.getcwd()
        path_split = current_path.split(os.sep)
        if path_split[-1] in ['online_device_inspection'] and path_split[-2] == 'script':
            project_name = path_split[-3]
        else:
            project_name = path_split[-1]
        pic_name = '{}.png'.format(self.package_name)
        memory_leak_file = os.path.join(current_path[:current_path.rfind(project_name)], project_name, 'leak_pic', pic_name)
        plt.savefig(memory_leak_file)


if __name__ == '__main__':
    mem = GetMemory()
    meminfo_output = []
    for i in range(3):
        output = mem.get_mem_info()
        print(type(output))
        # meminfo_output.append(output)
    # print(meminfo_output)
    # mem.create_plot(meminfo_output)









