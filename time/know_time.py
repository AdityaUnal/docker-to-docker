import requests


def knowtime(token, url=None):
    if url is None:
        url = 'http://time-server:8080/time'

    headers = {
        "Authorization": token
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        return {"error": str(e)}