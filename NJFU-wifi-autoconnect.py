import requests

account = "w200350418@cmcc"
password = '063515'

url = 'http://10.11.1.3/a70.htm'
params = {
    "DDDDD": account,
    "upass": password,
    "R1": "0",
    "R2": "",
    "R3": "0",
    "R6": "0",
    "para": "00",
    "para": "00",
    "0MKKey": "123456",
    "buttonClicked": "",
    "redirect_url": "",
    "err_flag": "",
    "username": "",
    "password": "",
    "user": "",
    "cmd": "",
    "Login": "",
    "v6ip": ""
}

res = requests.post(url = url, data = params)
print(res.text)
