from requests import get


def ping(url):
    return get(url).ok
