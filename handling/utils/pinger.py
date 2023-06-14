from requests import get


def ping(url):
    try:
        return get(url, timeout=5).ok
    except:
        return False
