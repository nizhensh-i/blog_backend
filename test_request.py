import os

import requests
# remote_url = os.getenv('ROMOTE_HOST')
# base_url = f'http://{remote_url}:4289'

remote_url =  'http://192.168.1.13'

base_url = f'http://{remote_url}:8081'
user = '123'
password = '123'

r = requests.post(base_url+'/auth/login',json={'uiAccountName':user, 'uiPassword':password})
token = r.json()['token']
print(token)


r1 = requests.get(base_url+'/user_posts', headers={'Authorization':token})
print(r1)

