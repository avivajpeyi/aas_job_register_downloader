import requests
from bs4 import BeautifulSoup
from http import HTTPStatus

MAIN = "https://jobregister.aas.org/"


def download_page()->BeautifulSoup:
    resp = requests.get(MAIN)
    if resp.status_code == HTTPStatus.OK:
        return BeautifulSoup(resp.text, 'html.parser')
    raise requests.HTTPError(resp)
