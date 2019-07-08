from selenium import webdriver
import requests
import ssl
import re
import json 
requests.packages.urllib3.disable_warnings()

def stationDic():	
	res = requests.get("https://kyfw.12306.cn/otn/resources/js/framework/station_name.js",verify=False)
	stationdata = res.text
	list1 = stationdata.split("@")
	list2 = []
	for i in list1:
		list2.append(i.split("|"))
	del list2[0]
	dic = {}
	for i in list2:
		dic[i[1]] = i[2]
	return dic

def search(city):
	stationdic = stationDic()
	cityname = city
	try:
		telecode = stationdic[cityname]
		res = requests.get("https://kyfw.12306.cn/otn/czxx/query?train_start_date=2019-07-04&train_station_name=&train_station_code="+telecode+"&randCode=",verify=False)
		train_list = json.loads(res.text)["data"]["data"]
		for t in train_list:
			print (t['station_train_code'],t['start_station_name'],t['start_start_time'],t['end_station_name'],t['end_arrive_time'])
	except Exception as e:
		print("NO",e)
	

while True:
	import os
	cityname = input("city:")
	os.system('cls')
	if cityname == "q":
		break
	else:
		search(cityname)	