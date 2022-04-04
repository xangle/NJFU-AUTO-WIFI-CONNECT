import requests
import json

with open('user.json', 'r') as f:
    info = json.loads(f.read())

account = info['account']
password = info['password']

url = 'http://10.11.1.3/a70.htm'
params = {
    "DDDDD": account,
    "upass": password,
    "R1": "0",
    "R3": "0",
    "R6": "0",
    "para": "00",
    "para": "00",
    "0MKKey": "123456"
}

res = str(requests.post(url = url, data = params).text)
if '成功' in res:
    print('校园网已自动登录')
else:
    print('校园网登录失败')
