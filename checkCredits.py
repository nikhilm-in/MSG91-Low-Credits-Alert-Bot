import json
import requests
import os

def check_credits():
    TOKEN=os.environ.get('TOKEN')
    MSG_TYPE=os.environ.get('MSG_TYPE')
    THRESHOLD=os.environ.get('THRESHOLD')

    queryParameters = {'type': MSG_TYPE, 'authkey': TOKEN}
    credits=requests.get('https://control.msg91.com/api/balance.php', params=queryParameters).text
    print(credits)
    
    if credits > THRESHOLD:
        notify_slack(credits)


def notify_slack(credits):
    SLACK_URL=os.environ.post('SLACK_URL')
    payload = {'text':'Hello, World!'}
    headers = {'Content-type': 'application/json'}
    requests.post(SLACK_URL, headers=headers, data=payload)

if __name__ == '__main__':
    check_credits()