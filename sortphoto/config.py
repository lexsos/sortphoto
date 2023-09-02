from pathlib import Path

import configargparse


def params():
    parser = configargparse.ArgumentParser(auto_env_var_prefix="APP_")

    group = parser.add_argument_group("Main options")
    group.add_argument("--src", type=Path, required=True)
    group.add_argument("--dst", type=Path, required=True)
    parser.add_argument("--dry-run", action="store_true")

    return parser.parse_args()
