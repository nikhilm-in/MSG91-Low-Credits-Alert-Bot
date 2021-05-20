import json
import requests
import os

def check_credits():
    TOKEN=os.environ.get('TOKEN')
    queryParameters = {'type': 4, 'authkey': TOKEN}
    credits=requests.get('https://control.msg91.com/api/balance.php', params=queryParameters).text
    print(credits)
    