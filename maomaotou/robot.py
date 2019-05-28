#coding=utf8
import json
import requests

def robot_reply(text):
    api_url = 'http://openapi.tuling123.com/openapi/api/v2'
    data = {
        "reqType":0,
        "perception": {
            "inputText": {
                "text": text
            }
        },
        "userInfo": {
            "apiKey": "521107a53c914e728aa1bf29823884fa",
            "userId": "testUserId"
        }
    }
    try:
        r = requests.post(api_url, data=json.dumps(data))
        res = r.json()
        for result in res['results']:
            if result['resultType'] == 'text':
                return result['values']['text']
    except Exception as e:
        print(e)
