import time, os
'''#循环执行demo'''


def re_exe(cmd, inc=60):
    while True:
        os.system(cmd)
        time.sleep(inc)
        print('我正在获取数据，请不要关闭',time.localtime())

# 如果系统变量里有python3和python2，需要使用此条命令
# re_exe('python3 get_coinfarm_data.py', 60)
re_exe('python get_coinfarm_data.py', 1780)