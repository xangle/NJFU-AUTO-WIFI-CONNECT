import requests

account = "account"
password = 'pwd'

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

res = requests.post(url = url, data = params)
print(res.text)
