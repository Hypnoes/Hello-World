#!/usr/bin/python3
# -*- coding: utf-8 -*-

import time
import logging
import argparse

from logging import Logger
from base64 import b64encode

import requests

from requests.exceptions import Timeout, ConnectionError

class Login(object):
    def __init__(self, username=None, password=None):
        self.username_ = str(username)
        self.password_ = '{B}' + b64encode(password.encode()).decode()

        self.url = 'http://10.10.10.10/srun_portal_pc.php?ac_id=1&url='

        self.data = {
            'action':'login',
            'username': self.username_,
            'password': self.password_,
            'ac_id':'1',
            'user_ip':'',
            'nas_ip':'',
            'save_me':'0',
            'ajax':'1'
            }

        self.header = {
            'X-Requested-With':'XMLHttpRequest',
            'Cache-Control':'no-cache',
            'User-Agent':'Mozilla/5.0(Windows NT 10.0; Win64; x64)'
            }

        self.logger = None

    def setLogger(self, logger):
        self.logger = logger

    @Delay(sec=3)
    def connect(self):
        try:
            res = requests.post(self.url, data=self.data, headers=self.header)
            return res.ok
        
        except Timeout:
            self.logger.error("Login Failed :: Timeout")
            return False

        except ConnectionError:
            self.logger.error("Login Failed :: Connection Broken.")
            return False

        finally:
            pass

    @Delay(sec=7)
    def test(self):
        try:
            test_point = 'http://106.14.182.15/?'
            test_response = 'OK'
            test_res = requests.get(test_point, timeout=1)
            if test_res.content.decode('utf8') == test_response:
                self.logger.info('OK')
                yield test_res.ok
            else:
                raise Offline

        except Timeout:
            self.logger.error('Test Failed :: TimeOut')
            return False

        except Offline:
            self.logger.error('Test Failed :: OffLine')
            return False

        finally:
            pass

class LoginLog(Logger):
    def __init__(self, name, level='INFO'):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)

        self.console_handler = logging.StreamHandler()
        self.console_handler.setLevel(logging.INFO)

        self.formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        self.console_handler.setFormatter(self.formatter)

        self.logger.addHandler(self.console_handler)

    def info(self, msg):
        self.logger.info(msg)

    def warn(self, msg):
        self.logger.warn(msg)

    def error(self, msg):
        self.logger.error(msg)

class Offline(Exception):
    def __init__(self):
        Exception.__init__("OffLine")

class Delay(object):
    def __init__(self, sec=0):
        self.sec = sec

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            time.sleep(self.sec)
            func(*args, **kwargs)
        return wrapper

def main(ns):
    me = Login(username=ns.n, password=ns.p)
    me.setLogger(LoginLog('auto-login'))

    try:
        while True:
            if me.connect():
                while me.test():
                    pass
            else:
                me.connect()
    except KeyboardInterrupt:
        print('\r')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Auto Connect')
    parser.add_argument('-n', metavar='username', type=int, nargs='+', help='username')
    parser.add_argument('-p', metavar='password', type=str, nargs='+', help='password')
    args = parser.parse_args()

    main(args)
