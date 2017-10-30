import requests
from json import dumps
from .config import config as c

host = "http://%s:%s" % (c['ip'], c['port'])
base_url = host + "/keys"


def post_new_key(data, url=base_url):
    keylist = [k.lstrip() for k in data.split(',')]
    results = {}
    counter = 0
    for key in keylist:
        response = requests.post(
            url,
            headers={"Content-Type": "application/json"},
            data=dumps({'pubkey': key})
        )
        results.update({counter: response.json()})
        counter += 1
    return results
