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

result = pd.read_csv("log.csv",dtype='str')
result.index=result.total
del result["total"]
data_all.index =data_all.code.values
del data_all["code"]

cb_df = result.join(data_all)
cb_df.to_csv('new.csv')

