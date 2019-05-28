#!/usr/bin/env python
# *-* coding:utf8 *-*
import re
import requests


def today_weather(text='天气'):
    city = text.replace('天气', '')
    if city:
        return city_weather(city)
    return city_weather()


def city_weather(city='深圳'):
    api_url = 'http://wthrcdn.etouch.cn/weather_mini?city='
    try:
        r = requests.get(api_url+city)
        res = r.json()
        if res['desc'] != 'OK':
            return
        _city = res['data']['city']
        today = res['data']['forecast'][0]
        date = today['date']
        high = today['high']
        low = today['low']
        _high = re.search(r'\d+', high).group(0)
        _low = re.search(r'\d+', low).group(0)
        _type = today['type']
        fengxiang = today['fengxiang']
        fengli = today['fengli']
        wendu = res['data']['wendu']
        ganmao = res['data']['ganmao']
        content = '今天是%s, %s最高温度%s℃, 最低温度%s℃, %s。%s' % (date, _city, _high, _low, fengxiang, ganmao)
        return content
    except Exception as e:
        print(e)


if __name__ == '__main__':
    print(today_weather('天气'))
