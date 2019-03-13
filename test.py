# -*- coding: utf-8 -*-
import json

### citys info
#from dianping import DianPing
#dp = DianPing()
#cities = dp.active_cities
#print(cities)

### city locations
#from city import City
#shenzhen= City('深圳')
#shenzhen.get()
#locations = shenzhen.locations
#print(locations)
#with open('shenzhen_location.txt', 'w') as f:
#    json.dump(locations, f, indent=4, ensure_ascii=False)

### city shop category
#from city import City
#shenzhen= City('深圳')
#shenzhen.get()
#category = shenzhen.category
#print(category)
#f = open('/data/data/dianping/shenzhen_category.json', 'w')
#json.dump(category, f, indent=4, ensure_ascii=False)
#f.close()

### relative result of keyword in city
#from city import City
#shenzhen= City('深圳')
#shenzhen.get()
#relative = shenzhen.get_relative('水吧')
#print(relative)

### search and download shop infos
from city import City
from dbhelper import Database
from config import MongoDB
db = Database(MongoDB)
shenzhen= City('深圳', searchDB=db)
shenzhen.get()
results = shenzhen.search('',category='饮品店',location='全部地区',sort='按人气排序',save=True,details=True,comments=False)
#print(results)
#f = open('/data/data/dianping/shenzhen_nanshan_yinpin_cha.json', 'w')
#json.dump(results, f, indent=4, ensure_ascii=False)
#f.close()
