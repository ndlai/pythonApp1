import requests


def myreq():
    v = requests.get('http://www.baidu.com')
    return v
