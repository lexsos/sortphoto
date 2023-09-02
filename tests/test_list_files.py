import os
from pathlib import Path

from sortphoto.lister import list_files

TEST_DIR = os.path.join(os.path.dirname(__file__), "dirs")


def test_list_dir():
    expected = {
        Path(os.path.join(TEST_DIR), "1/1.txt"),
        Path(os.path.join(TEST_DIR), "2/2.txt"),
    }
    assert set(list_files(Path(TEST_DIR))) == expected
