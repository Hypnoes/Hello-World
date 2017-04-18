#! python3
# -*- coding:utf-8 -*-
__author__ = 'Hypnoes'

import requests
import re

root = 'http://www.heibanke.com/lesson/crawler_ex01/'
rex = re.compile('下一关')

for i in range(30):
    r = requests.post(root, data={
        'username' : 'root',
        'password' : '{0}'.format(i)
    })
    s = r.content.decode()
    try:
        rex.search(s).group(0)
        print(i)
        break
    except:
        pass


    