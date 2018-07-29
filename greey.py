#!/usr/bin/env python
import requests
url = "http://finance.sina.com.cn/realstock/company/sz000651/qianfuquan.js?d=2014-06-16"
r = requests.get(url)
text = r.text.split("/*")[0].strip()
import demjson
data =demjson.decode(text)
from pandas import Series
obj =Series(data[0]['data'])
print obj.index

