import unittest
from aas_job_register_downloader.parse_main_page import get_table_from_aas
import os

CLEAN_AFTER = True


class TestMainPageParser(unittest.TestCase):
    def setUp(self) -> None:
        self.outdir = "out_test"
        os.makedirs(self.outdir, exist_ok=True)

    def tearDown(self) -> None:
        if CLEAN_AFTER:
            import shutil

            shutil.rmtree(self.outdir)

    def test_table_generation(self):
        table = get_table_from_aas()
        table.to_csv(f"{self.outdir}/aas_table.csv")


if __name__ == "__main__":
    unittest.main()
