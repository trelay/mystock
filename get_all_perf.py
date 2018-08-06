#!/usr/bin/env python2
#coding=utf-8
import requests
import demjson
from pandas import Series
import pandas as pd
from pandas import DataFrame
import tushare as ts
import numpy

data_all = ts.get_industry_classified()
data_all.index=data_all.code
del data_all['code']
data_all['rate']="NAN"

def get_rate(code):
    url = "http://finance.sina.com.cn/realstock/company/sz{0}/qianfuquan.js?d=2014-06-16".format(code)
    r = requests.get(url)
    if r.status_code!=200:
        url = "http://finance.sina.com.cn/realstock/company/sh{0}/qianfuquan.js?d=2014-06-16".format(code)
        r = requests.get(url)
    if r.status_code!=200:
       print("can not find this share")
       return "NAA"
    text = r.text.split("/*")[0].strip()
    data =demjson.decode(text)
    obj =Series(data[0]['data'])
    obj1=pd.to_numeric(obj)
    try: 
        obj1.index=pd.to_datetime(obj1.index,format="_%Y_%m_%d")
        rate = obj1[obj1.index.max()]/obj1[obj1.index.min()]
    except:
        rate = "NAN"
    print "{}:{}".format(code,rate)
    return rate
for com in numpy.array(data_all.index):
    rate = get_rate(com)
    data_all['rate'][com]=rate
    data_all.to_csv('result.log')
