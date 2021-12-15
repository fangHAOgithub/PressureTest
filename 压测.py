# -*- coding: utf-8 -*-

import requests
import threading
import time


class myThread(threading.Thread):
    def __init__(self, name, aim_url):
        threading.Thread.__init__(self)
        self.name = name
        self.aim_url = aim_url

    def run(self):
        this_str = "start :" + self.name
        print(this_str)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36 Edg/96.0.1054.53',
            }

        try:
            r = requests.get(self.aim_url, headers)
            if r.status_code == 200:
                print(self.name, '请求成功！')
        except Exception as e:
            print(e)
        this_str = "end :" + self.name
        print(this_str)


if __name__ == '__main__':
    url = 'http://fangxiaohao.top/'
    try:
        i = 0
        # 开启线程数目
        tasks_number = 20
        print('启动')
        time1 = time.clock()
        while i < tasks_number:
            t_name = i + 1
            t = myThread(str(t_name),aim_url=url)
            t.start()
            i += 1
        time2 = time.clock()
        times = time2 - time1
        print(times / tasks_number)
    except Exception as e:
        print(e)