from datetime import date

import pytest

from sortphoto.date_parser import pars_date


@pytest.mark.parametrize(
    "data,expected",
    [
        ("2023-09-03T15:17:20+00:00", date(2023, 9, 3)),
        ("1990-01-01T15:17:20+00:00", date(1990, 1, 1)),
        ("2000-01-01T15:17:20+00:00", date(2000, 1, 1)),
        ("2000-12-31T15:17:20+00:00", date(2000, 12, 31)),
    ]
)
def test_pars_date_iso_8601(data, expected):
    assert pars_date(data) == expected


@pytest.mark.parametrize(
    "data,expected",
    [
        ("20230903", date(2023, 9, 3)),
        ("20000102", date(2000, 1, 2)),
    ]
)
def test_pars_no_separates(data, expected):
    assert pars_date(data) == expected


@pytest.mark.parametrize(
    "data,expected",
    [
        ("text_20230903_text", date(2023, 9, 3)),
        ("text_2000-12-31_text", date(2000, 12, 31)),
    ]
)
def test_pars_inside_text(data, expected):
    assert pars_date(data) == expected


@pytest.mark.parametrize("data", ("2023-13-32", "20231332"))
def test_wrong_date(data):
    assert pars_date(data) is None
