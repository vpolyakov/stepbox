import requests


def request_content(url, func, *args):
    response = requests.get(url=url)
    response.raise_for_status()
    return func(response, *args)
