from pathlib import Path

from sortphoto.lister import filter_files

FILES = (
    Path("/1.jpg"),
    Path("/2.jpeg"),
    Path("/3.py"),
    Path("/4.JPG"),
)


def test_filter_by_extension():
    assert set(filter_files(FILES, {".py"})) == {Path("/3.py")}


def test_several_by_extension():
    assert set(filter_files(FILES, {".jpg", ".jpeg"})) == {
        Path("/1.jpg"), Path("/2.jpeg"),
    }


def test_case_insensitive():
    assert set(filter_files(FILES, {".jpg"}, True)) == {
        Path("/1.jpg"), Path("/4.JPG"),
    }
