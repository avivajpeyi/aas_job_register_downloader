import unittest
from aas_job_register_downloader.parse_main_page import get_table_from_aas
from aas_job_register_downloader.parse_job_page import get_job_description


class TestJobPageParser(unittest.TestCase):
    def test_job_description_getter(self):
        table = get_table_from_aas()
        job_url = table["Link"].iloc[0]
        description = get_job_description(job_url)
        self.assertIsInstance(description, str)


if __name__ == "__main__":
    unittest.main()
