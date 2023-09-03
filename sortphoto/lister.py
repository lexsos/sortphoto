import os
from collections import deque
from collections.abc import Generator, Iterable, Set
from pathlib import Path


def list_files(path: Path) -> Generator[Path, None, None]:
    dirs = deque([path])
    while len(dirs):
        current = dirs.pop()
        if not current.is_dir():
            yield current
            continue
        for item in current.iterdir():
            if item.is_dir():
                dirs.appendleft(item)
            else:
                yield item


def filter_files(
        files: Iterable[Path],
        extensions: Set[str],
        case_insensitive: bool = False,
) -> Iterable[Path]:
    exts = extensions
    if case_insensitive:
        exts = frozenset(map(str.lower, extensions))

    def check_ext(path: Path):
        _, ext = os.path.splitext(path)
        if case_insensitive:
            ext = ext.lower()
        return ext in exts

    return filter(check_ext, files)
