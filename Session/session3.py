#! python3
# -*- coding:utf-8 -*-
__author__ = 'Hypnoes'

import requests
import re

url = 'http://www.heibanke.com/lesson/crawler_ex02/'
r = requests.get(url)
_cookies = r.cookies

