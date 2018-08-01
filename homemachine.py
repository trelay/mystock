#!/usr/bin/env python
#coding=utf-8
import tushare as ts
ts.get_industry_classified()
data_all = ts.get_industry_classified()
data_home = data_all[data_all["c_name"]=="家电行业"]
print(data_home)
