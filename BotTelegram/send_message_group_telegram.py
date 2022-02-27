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

send_msg(TOKEN, GROUP_ID, msg)
