import requests
from json import dumps

host = "http://127.0.0.1:5000"
base_url = host + "/keys"


def post_new_key(data, url=base_url):
    to_send = dumps({'pubkey': data})
    response = requests.post(
        url,
        headers={"Content-Type": "application/json"},
        data=to_send
    )
    return response.json()
