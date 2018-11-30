import time, os
'''#循环执行demo'''


def re_exe(cmd, inc=60):
    while True:
        os.system(cmd)
        time.sleep(inc)


re_exe('python3 get_coinfarm_data.py', 20)