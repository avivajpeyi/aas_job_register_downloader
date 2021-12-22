from typing import Dict, List

import pandas as pd
from bs4 import BeautifulSoup

from .html_parser import Table, download_page

MAIN = "https://jobregister.aas.org"

JOB_IDS = [
    "FacPosNonTen",
    "FacPosTen",
    "PostDocFellow",
    "PreDocGrad",
    "SciEng",
    "SciMgmt",
    "SciTechStaff",
    "Other",
]


def get_job_types(page: BeautifulSoup) -> Dict[str, str]:
    return {
        tag["id"]: tag.get_text()
        for tag in page.find_all(id=True)
        if tag["id"] in JOB_IDS
    }


def get_tables_from_aas():
    page = download_page(MAIN)
    job_types = get_job_types(page)
    tables = get_tables(page)
    tables_dict = {}
    for (job_id, job_type), table in zip(job_types.items(), tables):
        table["Job Type"] = job_type
        tables_dict[job_id] = table
    return tables_dict


def get_table_from_aas():
    tables_dict = get_tables_from_aas()
    return pd.concat([t for t in tables_dict.values()])


def get_tables(page: BeautifulSoup) -> List[Table]:
    html_tables = page.find_all("table")
    return [Table.from_bs4(t, link_base=MAIN) for t in html_tables]
