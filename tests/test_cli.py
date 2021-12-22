import unittest
from aas_job_register_downloader.cli import main
import pytest
import os
from unittest.mock import patch
import sys

CLEAN_AFTER = True


class TestCli(unittest.TestCase):
    def setUp(self) -> None:
        self.outdir = "out_test"
        self.cwd = os.getcwd()
        os.makedirs(self.outdir, exist_ok=True)
        os.chdir(self.outdir)

    def tearDown(self) -> None:
        os.chdir(self.cwd)
        if CLEAN_AFTER:
            import shutil

            shutil.rmtree(self.outdir)

    @pytest.mark.slow
    def test_with_descriptions(self):
        testargs = ["-v"]
        with patch.object(sys, "argv", testargs):
            main()

    def test_without_descriptions(self):
        main()


if __name__ == "__main__":
    unittest.main()
