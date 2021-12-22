import argparse
import os
from typing import List

from tqdm.auto import tqdm

from .parse_job_page import get_job_description
from .parse_main_page import get_table_from_aas

FILENAME = "aas_jobs.csv"


class style:
    RED = "\033[31m"
    GREEN = "\033[32m"
    RESET = "\033[0m"


def save_table(with_descriptions=False):
    if os.path.exists(FILENAME):
        print(
            style.RED + f"{FILENAME} exists, not overwritting." + style.RESET
        )
    else:
        table = get_table_from_aas()
        if with_descriptions:
            table["Description"] = get_descriptions(table.Link)
        table.to_csv(FILENAME, index=False)
        print(style.GREEN + f"{FILENAME} saved" + style.RESET)
        print("Happy job hunting \U0000263A")


def get_descriptions(links: List[str]):
    return [
        get_job_description(l)
        for l in tqdm(links, desc="Getting job descriptions")
    ]


def get_cli_args():
    parser = argparse.ArgumentParser(
        prog="download_aas_jobs",
        description=f"Downloads the job table from https://jobregister.aas.org/ and saves it in {FILENAME}",
    )
    parser.add_argument(
        "-v",
        action="store_true",
        help="If the job descriptions should also be stored (False by default)",
    )
    args = parser.parse_args()
    return args.v


def main():
    with_descriptions = get_cli_args()
    save_table(with_descriptions)
