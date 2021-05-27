import json
import requests
import os

MSG_TYPES=['1','4']

def check_credits(MSG_TYPE):
    TOKEN=os.environ.get('TOKEN')
    # MSG_TYPE=os.environ.get('MSG_TYPE')
    THRESHOLD=os.environ.get('THRESHOLD')

    queryParameters = {'type': MSG_TYPE, 'authkey': TOKEN}
    credits=requests.get('https://control.msg91.com/api/balance.php', params=queryParameters).text
    print("The credit is "+credits)
    
    if int(credits) < int(THRESHOLD):
        print("Credits is below the threshold "+THRESHOLD+" Sending a notification")
        notify_slack(MSG_TYPE,credits,THRESHOLD)


def notify_slack(MSG_TYPE,credits,THRESHOLD):
    SLACK_URL=os.environ.get('SLACK_URL')
    # payload = {'text':'The MSG91 credits is '+credits+'! Please check ASAP'}
    payload={
        'attachments': [
            {
                'color': '#E01E5A',
                'author_name': 'MSG91 Credits Alert',
                'author_icon': 'https://msg91.com/wp-content/uploads/2020/07/msg91_logo.svg',
                'title': 'The MSG91 credits for msg type '+MSG_TYPE+' is '+credits+'! Please check ASAP',
                'text': 'Credits allocated to our account in MSG91 which is our SMS delivery partner is low. The threshold was '+THRESHOLD+'. Please contact relevant the relevant owner for recharging it.',
                'fields': [
                    {
                        'title': 'Priority',
                        'value': 'HIGH',
                        'short': 'false'
                    }
                ],
                'ts': 123456789
            }
        ]
    }
    headers = {'Content-type': 'application/json'}
    slack_response=requests.post(SLACK_URL, headers=headers, json=payload)
    print("Sent a notification to slack webhook url. The response was "+slack_response.text)
if __name__ == '__main__':
    for MSG_TYPE in MSG_TYPES:
        print("Checking credits for msg type "+MSG_TYPE)
        check_credits(MSG_TYPE)