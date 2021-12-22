from .parse_main_page import get_table_from_aas
from .parse_job_page import get_job_description
from tqdm.auto import tqdm
from typing import List
import os
import sys

FILENAME = "aas_jobs.csv"


def save_table(with_descriptions=False):
    if os.path.exists(FILENAME):
        raise FileExistsError(f"{FILENAME} exists, not overwritting.")
    table = get_table_from_aas()
    if with_descriptions:
        table["Descriptions"] = get_descriptions(table.Link)
    table.to_csv(FILENAME, index=False)


def get_descriptions(links: List[str]):
    return [
        get_job_description(l)
        for l in tqdm(links, desc="Getting job descriptions")
    ]


def main():
    if sys.argv[-1] == "-v":
        save_table(with_descriptions=True)
    save_table(with_descriptions=False)
