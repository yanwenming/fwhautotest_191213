#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:Yan Wenming
# create time:2019-12-06

import requests
import unittest
import json
from testCase import test2_address
from testCase import test1_login
from time import sleep
import datetime
import time

''''''


class createorder(unittest.TestCase):
    '''用户提交订单'''
    def test3_createorder(self):
        token = test1_login.login().test2_getToken()
        addressid=test2_address.address.test2_getAddressid(self)
        now_time=datetime.datetime.now()
        book_day=(now_time+datetime.timedelta(days=+10)).strftime("%Y-%m-%d")#设置预约时间
        url = "https://api-user-test.uyess.com/v2/order/add-order?qd_no=uyes_gzh&district_id=1997&access_token=" + token
        form_data = {"address_id" : int(addressid) , "order_source" : 2 , "carts" : [] , "goods" : [
            {"goods_no" : "793511395600" , "activity_id" : 0 , "num" : 1 , "item_id" : "311" , "price" : "30.00" ,
             "goods_item_id" : "311" , "ref_no" : "sku05395949177948"}] , "redpacket_id" : "19968581" ,
                     "book_day" : book_day , "book_period" : "09:00-12:00" , "user_remark" : "test the process" ,
                     "mix_goods" : "" , "mix_book_day" : "" , "mix_book_period" : ""}
        data2 = json.dumps ( form_data )
        data = {'data': data2,'qd_no':'uyes_gzh', 'referee_no':''}
        respone = requests.post(url ,data)
        # global order_id
        r = respone.text  # new
        print(r)
        order_id = json.loads ( r )["data"]["order_id"]
        with open('orderid.txt','w') as f:
            f.write(order_id)
        sleep(1)
        message1 = json.loads ( r )["message"]
        self.assertEqual ( message1 , "SUCCESS" )

    def test3_getOrderid ( self ) :
        with open('orderid.txt','r') as f:
           orderid=f.read()
           return orderid
