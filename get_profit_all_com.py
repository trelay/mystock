#!/bin/python3
import pandas as pd
import tushare as ts
from time import sleep
from pandas import DataFrame
from datetime import datetime
global all_data
all_data = DataFrame()

now = '20210618'
pro = ts.pro_api('418443b56e07ac5c235d232406b44db8f80484569f8240f4554c6d67')

#f = open('/home/trelay/list','r')
#ts_code_list = f.readlines()
#f.close()
#ts_code_list = ['000651.SZ', '600009.SH']
ts_code_list = pro.query('stock_basic', exchange='', list_status='L', fields='ts_code')['ts_code']

for ts_code in ts_code_list:
    ts_code = ts_code.strip()
    print("searching {0}".format(ts_code))

    new_data=pro.income(ts_code=ts_code, start_date='20190101', end_date='20200731',period="20191231", fields='ts_code,ann_date,report_type,revenue,operate_profit')

    try:
        all_data= pd.concat([all_data, new_data])
    except IndexError:
        print("Jump {0}".format(ts_code))
    sleep(1.1)


print(all_data)
file_path = os.path.join(os.getcwd(),"profit.xlsx")
all_data.to_excel(file_path)
