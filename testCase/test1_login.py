#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:Yan Wenming
# create time:2019-12-06

import requests
import unittest
from time import sleep


class login ( unittest.TestCase):
    '''用户登录'''
    def test1_tologin( self ):
        url = "https://api-user-test.uyess.com/v2/user/login"
        param = {"mobile": "13510642540", "code": "1234", "qd_no": "uyes_gzh"}
        r = requests.get(url , param)
        response1 = r.json()
        # print('我是：',response1['data']['user_access_token'])
        with open('tokenvalue.txt','w') as f:
            f.write(response1['data']['user_access_token'])
        sleep(1)

    def test2_getToken(self):
       with open("tokenvalue.txt",'r') as f:
           token=f.read()
           return token










# if __name__ == '__main__':
#     unittest.main(verbosity = 2)






