import requests
import json

def call_weather_api():
    url = "https://opendata.cwa.gov.tw/api/v1/rest/datastore/F-C0032-001?Authorization=CWA-2DBA06BF-8B31-481D-B1D0-7A3D76502B2A"
    response = requests.get(url)
    json_api = json.loads(response.text)
    location = json_api["records"]["location"]
    element_dict = {}
    for i in location:
        city = i['locationName']    # 縣市名稱
        wx = {}
        pop = {}
        mint = {}
        ci = {}
        maxt = {}
        for counter in range(0, 3):
            wx[i['weatherElement'][0]['time'][counter]['startTime']] = i['weatherElement'][0]['time'][counter]['parameter']['parameterName']    # 天氣現象
            pop[i['weatherElement'][1]['time'][counter]['startTime']] = i['weatherElement'][1]['time'][counter]['parameter']['parameterName']    # 降雨機率
            mint[i['weatherElement'][2]['time'][counter]['startTime']] = i['weatherElement'][2]['time'][counter]['parameter']['parameterName']    # 最低溫
            ci[i['weatherElement'][3]['time'][counter]['startTime']] = i['weatherElement'][3]['time'][counter]['parameter']['parameterName']    # 舒適度
            maxt[i['weatherElement'][4]['time'][counter]['startTime']] = i['weatherElement'][4]['time'][counter]['parameter']['parameterName']    # 最高溫
        element_dict[city] = {"天氣現象":wx, "降雨機率":pop, "最低溫":mint, "舒適度":ci, "最高溫":maxt}
    return element_dict
