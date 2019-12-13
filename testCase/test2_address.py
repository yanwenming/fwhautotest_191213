#!/usr/bin/env python
# -*-coding:utf-8-*-

# author:Yan Wenming
# create time:2019-12-06

import requests
import unittest
import json
from testCase import test1_login
from time import sleep
import random

''''''


class address(unittest.TestCase):
    '''用户添加地址'''
    def test2_addaddress ( self ) :
        token= test1_login.login().test2_getToken()
        # print(token)
        # print(len(token))
        url = "https://api-user-test.uyess.com/v2/user/add-address?qd_no=uyes_gzh&district_id=1997&access_token=" + token
        form_data = {'username' : '研发'+random.choice("深圳欢迎您南山宝安福田罗湖龙岗株洲长沙") , 'sex' : '' , 'phone' : 13510642540 , 'province_id' : 1895 , 'city_id' : 1987 ,
                 'district_id' : 1997 , 'address' : '南山地铁站D口' , 'house_num' : '2栋202' , 'sys_province_id' : 1895 ,
                 'sys_city_id' : 1987 , 'sys_district_id' : 1997 , 'sys_street_code' : 440305002 ,
                 'street_code' : 440305002 , 'qd_no' : 'uyes_gzh'}
        data = form_data
        # print(url)
        response = requests.post ( url , data )
        r = response.text
        address_id = json.loads ( r )["data"]["id"]
        with open('addressid.txt','w') as f:
            f.write(str(address_id))
        sleep(1)

    def test2_getAddressid ( self ) :
        with open("addressid.txt",'r') as f:
           addressid=f.read()
           return addressid