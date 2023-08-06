import requests
import base64



def OCRBaidu(fig_data):
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/general_basic"

    img = fig_data

    params = {"image":img}
    access_token = '24.6e77562708a76fdcfdf2e1c55a9c2105.2592000.1659753230.282335-23937918'
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print('BaiduOCR Result: ')
    
        res = ''
        for sub_words in response.json()['words_result']:
            res += sub_words['words']
        print(res)

    return res
