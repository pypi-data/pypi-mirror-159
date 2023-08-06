import requests
import base64
import json


def OCRAli(fig_data):

    url = "https://ocrapi-advanced.taobao.com/ocrservice/advanced"

    headers = {
    'Content-Type': 'application/json; charset=UTF-8',
    'Authorization': 'APPCODE 01ce75bd06b6482e8b954398f3874485'
    }

    img = fig_data

    payload = {"img": img}

    payload_json = json.dumps(payload)


    response = requests.request("POST", url, headers=headers, data=payload_json)

    res = ""
    print("before ali processing")

    if response: 
        print('AliOCR Result: ')

        res = json.loads(response.text)['content']
        print(res)

    return res

