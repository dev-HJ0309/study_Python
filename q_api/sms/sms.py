import json
import platform
import requests
import config
import auth


default_agent = {
    'sdkVersion': 'python/4.2.0',
    'osPlatform': platform.platform() + " | " + platform.python_version()
}


url = "http://api.coolsms.co.kr/messages/v4/send"
headers = auth.get_headers('NCSIVAFREGO5CAIM', 'AHYBPVDXORSV5MY0ES4NLFJQZHRXN8QC')

data = {
    "message": {
        "to": "01062897138",
        "from": "01062897138",
        "text": "되어라"
    }
}
print(json.dumps(data, ensure_ascii=False))
response = requests.post(config.get_url('/messages/v4/send'),
                         headers=auth.get_headers(config.api_key, config.api_secret),
                         json=data)
print(response.status_code)
print(response.text)
