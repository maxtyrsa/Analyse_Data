#Google sheet
import pandas as pd 
import requests 
from urllib.parse import urlencode 
 
# используем api 
base_url = 'https://cloud-api.yandex.net/v1/disk/public/resources/download?' 
public_key = url
 
# получаем url 
final_url = base_url + urlencode(dict(public_key=public_key)) 
response = requests.get(final_url) 
download_url = response. json() ['href']
 
# загружаем файл в df 
download_response = requests.get(download_url) 
df = pd.read_csv(download_url, sep='\t') 



#API Telegram
import requests
import json
from urlib.parse import urlencode

token = 'your token'
chat_id = 'your id'

message = 'send text'

params = {'chat_id': chat_id, 'message': text}
base_url = f'https://api.telegram.org/bot{token}/'
url = base_url + 'sendMessage?' + urlencode(params)

resp = requests.get(url)

