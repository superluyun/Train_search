from django.shortcuts import render
from django.http.response import HttpResponse
# from selenium import webdriver
import requests
import ssl
import re
import json

requests.packages.urllib3.disable_warnings()

# Create your views here.
def stations(request):
    stations = stationsList()
    jsonstr = json.dumps(stations)
    return HttpResponse(jsonstr)

def search_train(request):
    city = request.GET.get("city")
    train_list = search(city)
    if train_list == None:
        return HttpResponse("Null")
    else:
        train_list["code"]=0
        train_list["msg"]=""
        train_list["count"]=1000
        jsonstr = json.dumps(train_list)
        return HttpResponse(jsonstr)

def stationsList():
    res = requests.get("https://kyfw.12306.cn/otn/resources/js/framework/station_name.js", verify=False)
    stationdata = res.text
    list1 = stationdata.split("@")
    list2 = []
    for i in list1:
        list2.append(i.split("|"))
    del list2[0]
    list3=[]
    for i in list2:
        list3.append(i[1])
    return list3

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
        res = requests.get("https://kyfw.12306.cn/otn/czxx/query?train_start_date=2019-07-09&train_station_name=&train_station_code="+telecode+"&randCode=",verify=False)
        train_list = json.loads(res.text)["data"]
        # for t in train_list:
        #     print (t['station_train_code'],t['start_station_name'],t['start_start_time'],t['end_station_name'],t['end_arrive_time'])
        return train_list
    except Exception as e:
        return None