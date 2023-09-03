import re
from datetime import date
from typing import Optional

_PATTERNS = (
    r"(?P<day>[0123][0-9])-(?P<month>[01][0-9])-(?P<year>[12][0-9][0-9][0-9])",
    r"(?P<year>[12][0-9][0-9][0-9])-(?P<month>[01][0-9])-(?P<day>[0123][0-9])",
    r"(?P<year>[12][0-9][0-9][0-9])(?P<month>[01][0-9])(?P<day>[0123][0-9])",
)
_EXPRESSIONS = tuple(re.compile(pattern) for pattern in _PATTERNS)


def pars_date(raw_data: str) -> Optional[date]:
    for expr in _EXPRESSIONS:
        s = expr.search(raw_data)
        if not s:
            continue
        try:
            return date(**{k: int(v) for k, v in s.groupdict().items()})
        except ValueError:
            continue
    return None
