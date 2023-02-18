"""Main module."""
from __future__ import annotations

from pathlib import Path
from typing import Any, Dict


class Q:
    """Qgofer your personal assistant."""

    __slots__ = (
        "_home",
        "_qgofer",
        "_qgofer_config",
        "_qgofer_cache",
        "_qgofer_cache_db",
    )
    _instances: Dict[Any, Any] = {}

    def __new__(cls, home) -> Q:
        if cls not in cls._instances:
            cls._instances[cls] = super(Q, cls).__new__(cls)
        return cls._instances[cls]

    def __init__(self, home: Path = Path.home()):
        self._home = home
        self._qgofer = self._home / '.qgofer'
        self._qgofer.mkdir(parents=True, exist_ok=True)
        self._qgofer_config = self._qgofer / 'config.toml'
        self._qgofer_config.touch(exist_ok=True)
        self._qgofer_cache = self._qgofer / 'cache'
        self._qgofer_cache.mkdir(parents=True, exist_ok=True)
        self._qgofer_cache_db = self._qgofer_cache / 'qgofer.db'
        self._qgofer_cache_db.touch(exist_ok=True)

    @property
    def home(self) -> Path:
        return self._home

    @property
    def qgofer(self) -> Path:
        return self._qgofer

    @property
    def qgofer_config(self) -> Path:
        return self._qgofer_config

    @property
    def qgofer_cache(self) -> Path:
        return self._qgofer_cache

    @property
    def qgofer_cache_db(self) -> Path:
        return self._qgofer_cache_db

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.home})"

    def __str__(self) -> str:
        return "Qgofer your personal assistant"
