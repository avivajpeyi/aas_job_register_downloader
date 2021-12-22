from http import HTTPStatus

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from bs4.element import Tag


def download_page(url) -> BeautifulSoup:
    resp = requests.get(url)
    if resp.status_code == HTTPStatus.OK:
        return BeautifulSoup(resp.text, "html.parser")
    raise requests.HTTPError(resp)


class Table(pd.DataFrame):
    @classmethod
    def from_bs4(cls, table_html: Tag, link_base=""):
        rows = table_html.find_all("tr")
        header = list(rows.pop(0).stripped_strings)
        contents = [list(row.stripped_strings) for row in rows]
        contents = np.array(contents).T.tolist()
        if link_base != "":
            links = [
                f"{link_base}{a.get('href')}" for a in table_html.find_all("a")
            ]
            header.append("Link")
            contents.append(links)
        data = {header[i]: contents[i] for i in range(len(header))}
        return cls(data)
