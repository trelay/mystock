#!/usr/bin/env python
import requests
url = "http://finance.sina.com.cn/realstock/company/sz000651/qianfuquan.js?d=2014-06-16"
r = requests.get(url)
text = r.text.split("/*")[0].strip()
import demjson
data =demjson.decode(text)
from pandas import Series
import pandas as pd
from pandas import DataFrame
obj =Series(data[0]['data'])
obj1=pd.to_numeric(obj)
obj1.index=pd.to_datetime(obj1.index,format="_%Y_%m_%d")
#from pandas import DataFrame
#data1=DataFrame(obj1)
#data1.columns=["Price",]
#print(data1)
#data1.Price[data1.index.min()]
#data1.Price[data1.index.max()]

print(obj1)
rate = obj1[obj1.index.max()]/obj1[obj1.index.min()]
print(rate)
