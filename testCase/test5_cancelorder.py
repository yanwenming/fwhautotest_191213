#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:Yan Wenming
# create time:2019-12-09

import requests
import unittest
import json
from testCase import test3_createorder
from testCase import test1_login
from time import sleep


class cancel(unittest.TestCase):
    '''用户取消订单'''
    @unittest.skip ( "忽略取消订单" )
    def test5_cancelorder( self ):
        token=test1_login.login.test2_getToken(self)
        orderid=test3_createorder.createorder.test3_getOrderid(self)
        url='https://api-user-test.uyess.com/v2/order/cancel?qd_no=uyes_gzh&district_id=1997&access_token='+token
        param = {"order_id" : orderid , "option_id" : 323 , "refund_type" : "" , 'qd_no' : 'uyes_gzh'}
        response=requests.post(url,param)
        r=response.text
        message=json.loads ( r )["message"]
        self.assertEqual(message,"取消订单成功")
        print(r)