import requests
import json


def OCRLocal(fig_data):
  url = "http://10.117.233.11/ocr"

  img = fig_data

  payload = {"img_base64": img}

  payload_json = json.dumps(payload)

  headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
  }

  # print("here")
  response = requests.request("POST", url, headers=headers, data=payload_json)
  if response:
    print('LocalOCR Result: ')
    print(response.text)
  return response.text




