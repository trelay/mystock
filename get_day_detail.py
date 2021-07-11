import requests
import pymongo
import json
import logging
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("/home/pi/mail/log.txt")
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)


now = datetime.now().strftime('%Y%m%d')
f = open('/home/pi/get_profit/list','r')
ts_code_list = f.readlines()
f.close()

#ts_code_list=["300588.SZ\n"]
client = pymongo.MongoClient("mongodb://localhost:27017/")
day_db = client["day_data"]
day_col = day_db["Data_min"]

for code in ts_code_list:
    codex= code.split(".")
    codey=str(codex[1].strip().lower())+str(codex[0])
    url = "https://web.ifzq.gtimg.cn/appstock/app/minute/query?code={0}".format(codey)
    r = requests.get(url)
    
    if r.status_code == 200:
        day_dict = json.loads(r.text)
        if len(day_dict['data'][codey]['data']['data']) == 1 or day_dict['data'][codey]['data']['date'] == "":
            logger.info("can not find data:{0}".format(codey))
        else:
            date_code = day_dict['data'][codey]['data']['date'] + "_" + codey
            if day_col.find({ "date_code":date_code}).count() ==0:
                insert_data = {"date_code":date_code,"data_min":day_dict['data'][codey]['data']['data']}
                day_col.insert_one(insert_data)
            
    else:
        logger.error("Network issue when fetch data:{0}".format(codey))
client.close()
logger.info("finished today_{0} data".format(now))
print("finished today_{0} data".format(now))
