"""Caching to the insane level. File level."""
import pickle
from hashlib import sha256
from pathlib import Path
from typing import Any

CACHEDIR = Path(__file__).parent / "__cache__"


def _hash_key(key: object) -> str:
    return sha256(repr(key).encode("ascii", errors="backslashreplace")).hexdigest()


def set(scope: str, key: object, value: object) -> None:
    """Do stuff with raw hash dict"""
    if not (CACHEDIR / scope).is_dir():
        (CACHEDIR / scope).mkdir(parents=True)
    filename = _hash_key(key) + ".pkl"
    if not (CACHEDIR / scope / filename).is_file():
        (CACHEDIR / scope / filename).touch()
    try:
        (CACHEDIR / scope / filename).write_bytes(pickle.dumps(value))
    except AttributeError:  # Cannot pickle
        (CACHEDIR / scope / filename).unlink()


def get(scope: str, key: object) -> Any:
    """Do stuff with raw hash dict"""
    if not (CACHEDIR / scope).is_dir():
        raise KeyError

    filename = _hash_key(key) + ".pkl"
    if not (CACHEDIR / scope / filename).is_file():
        raise KeyError
    return pickle.loads((CACHEDIR / scope / filename).read_bytes())
