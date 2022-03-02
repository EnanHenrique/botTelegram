#! /usr/bin/env python3

from credentials import TOKEN
from credentials import GROUP_ID

from utils import save_log

from requests import get
from pytz import timezone
from datetime import datetime

brazil_timezone = timezone('Brazil/East')

now = datetime.now(brazil_timezone)
date = now.strftime(r'%Y-%m-%d')
time = now.strftime(r'%H-%M-%S')

full_date = date + " " + time

msg = f'Message received on {full_date}'
img = open(r'C:\Users\SETH\Desktop\HOMOLOG - GP4\API TELEGRAM\UNLOCK-Logo.png', 'rb')

def send_msg(token, group_id, message):
    API_URL = f'https://api.telegram.org/bot{token}/sendMessage?chat_id=@{group_id}&text={message}'
    response = get(API_URL)

    status = response.status_code

    if status == 200:
        print('Message sent successfully!')
        save_log(full_date, f'{message}', status, {'status': {response.status_code}})
    else:
        print(f'Error on sendind message! {response.json()}')
        save_log(full_date, response.json(), status)

def send_photo(token, group_id, photo):
    API_URL = f'https://api.telegram.org/bot{token}/sendPhoto?chat_id=@{group_id}'
    response = get(API_URL, files={'photo': img})

    status = response.status_code

    if status == 200:
        print('Photo sent successfully!')
        save_log(full_date, f'{photo}', status, {'status': {response.status_code}})
    else:
        print(f'Error on sendind message! {response.json()}')
        save_log(full_date, response.json(), status)

send_msg(TOKEN, GROUP_ID, msg)
send_photo(TOKEN, GROUP_ID, img)
