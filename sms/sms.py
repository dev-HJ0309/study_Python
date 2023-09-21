import datetime
import hashlib
import hmac
from random import choice

import requests
import string

url = "http://api.coolsms.co.kr/messages/v4/send"
now = str(datetime.datetime.now())
letters = string.ascii_letters
salt = ''.join(choice(letters) for i in range(16))
message = now + salt
api_key = "NCSIVAFREGO5CAIM"
api_secret = "AHYBPVDXORSV5MY0ES4NLFJQZHRXN8QC"
signature = hmac.new(api_secret.encode('utf-8'), message.encode('utf-8'), hashlib.sha256)
headers = {
  "Authorization": f"HMAC-SHA256 apiKey={api_key}, date={now}, salt={salt}, signature={signature.hexdigest()}",
  "Content-Type": "application/json"
}
data = {"strict":False,"message":{"to":"01062897138","from":"01062897138","text":"테스트문자","type":"SMS"}}

response = requests.post(url, headers=headers, json=data)
print(response.status_code)
print(response.text)