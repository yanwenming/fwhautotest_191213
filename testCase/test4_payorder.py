#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:Yan Wenming
# create time:2019-12-06

import requests
import unittest
import json
from testCase import test3_createorder
from testCase import test1_login
from time import sleep

''''''


class payorder(unittest.TestCase):
    '''用户支付订单'''
    # @unittest.skip ( "忽略支付" )
    def test4_topayorder( self ):
        token= test1_login.login().test2_getToken()
        order_id=test3_createorder.createorder.test3_getOrderid(self)
        sleep (2)
        url = 'https://api-user-test.uyess.com/payment/unified-pay/pay'
        param = {"pay_type" : "wallet" , "trade_type" : "order" , "qd_no" : "uyes_gzh" , 'district_id' : 1997 ,
                 'access_token' : token , 'trade_id' : order_id}
        response = requests.get ( url , param )
        print (response)
        r = response.text
        status = json.loads ( r )["status"]
        self.assertEqual ( status , 200 )
