"""Main module."""
from __future__ import annotations

import os
from asyncio import run as async_run
from pathlib import Path

if False:  # TYPE_CHECKING
    from typing import AsyncGenerator, Any, Dict, Generator, Tuple

import aiofiles

from .logger import get_logger
from .rake import RAKE
from .utils import get_log_path, init_path

home_dir = init_path()
log_path = get_log_path()
logger = get_logger(log_path=log_path)

supported_extensions = ['.txt']
folders_to_index = [
    'Documents',
    'Downloads',
    'Desktop',
    'Music',
    'Videos',
    'Pictures',
    'Movies',
    'OneDrive',
    'Dropbox',
    'Google Drive',
]
rake = RAKE()


class App:
    """The main appliation class for managing the entirety of qgofer.

    Attributes:
        home: The home directory of the user, defaults to Path.home()
        root_dir: The root directory to index, defaults to Path.home()
    """

    __slots__ = (
        "_home",
        "_root_dir",
        "_qgofer",
        "_qgofer_config",
        "_qgofer_cache",
        "_qgofer_cache_db",
        "_qgofer_logs",
    )
    _instances: Dict[Any, Any] = {}

    def __new__(cls, home, root_dir) -> App:
        """Create a new instance of the class. by using the singleton pattern."""
        if cls not in cls._instances:
            cls._instances[cls] = super(App, cls).__new__(cls)
        return cls._instances[cls]

    def __init__(self, home: Path = Path.home(), root_dir: Path = Path.home()):
        """Initialize the class. using home and root_dir as the home and root directory of qgofer."""
        self._home = home
        self._root_dir = root_dir
        self._qgofer = self._home / '.qgofer'
        self._qgofer.mkdir(parents=True, exist_ok=True)
        self._qgofer_config = self._qgofer / 'config.toml'
        self._qgofer_config.touch(exist_ok=True)
        self._qgofer_cache = self._qgofer / 'cache'
        self._qgofer_cache.mkdir(parents=True, exist_ok=True)
        self._qgofer_cache_db = self._qgofer_cache / 'qgofer.db'
        self._qgofer_cache_db.touch(exist_ok=True)
        self._qgofer_logs = self._qgofer / 'logs'
        self._qgofer_logs.mkdir(parents=True, exist_ok=True)

    @property
    def home(self) -> Path:
        """Return the home directory of the user."""
        return self._home

    @property
    def qgofer(self) -> Path:
        """Return the qgofer directory."""
        return self._qgofer

    @property
    def qgofer_config(self) -> Path:
        """Return the qgofer config file."""
        return self._qgofer_config

    @property
    def qgofer_cache(self) -> Path:
        """Return the qgofer cache directory."""
        return self._qgofer_cache

    @property
    def qgofer_cache_db(self) -> Path:
        """Return the qgofer cache database."""
        return self._qgofer_cache_db

    def __repr__(self) -> str:
        """Return the representation of the class."""
        return f"{self.__class__.__name__}({self.home})"

    def __str__(self) -> str:
        """Return the string representation of the class."""
        return "Qgofer your personal assistant"


def _index_folder(path: Path) -> Generator[Path, None, None]:
    """Index the folder."""
    path = Path(path).expanduser().resolve()
    try:
        for item in path.iterdir():
            if item.name.startswith('.'):
                continue
            if item.is_dir():
                if item.name in folders_to_index:
                    yield from _index_folder(item)
            elif item.is_file():
                if item.suffix in supported_extensions:
                    yield item
    except (PermissionError, FileNotFoundError) as err:
        logger.error(err)


# TODO: Clean up this function
def process_index_list(app: App) -> App:
    """Process the index list."""

    async def _read_index_list(app: App) -> AsyncGenerator[Path, None]:
        """Read the index list."""
        async with aiofiles.open(app._qgofer_cache / "inde_list.txt", "r", encoding="utf-8") as f:
            async for line in f:
                yield Path(line.strip())

    async def _process_files(app: App) -> AsyncGenerator[Tuple[str, Path], None]:
        """Process the index list."""
        async for item in _read_index_list(app):
            async with aiofiles.open(item, "r", encoding="utf-8") as f:
                content = await f.read()
                yield content, item

    async def _gen_meta(app: App) -> AsyncGenerator[Tuple[Any, float, float, Path], None]:
        """Generate the meta data."""
        async for content, file in _process_files(app):
            kw = rake.exec(content)
            m_time = os.path.getmtime(file)
            c_time = os.path.getctime(file)
            print(kw, m_time, c_time, file)
            yield kw, m_time, c_time, file

    async def _process_meta(app: App) -> None:
        """Process the meta data."""
        async for kw, m_time, c_time, file in _gen_meta(app):
            print(kw, m_time, c_time, file)

    async_run(_process_meta(app))

    return app


def create_index_list(app: App) -> App:
    """Index the folders."""
    # A list to be populated with async tasks.
    for item in _index_folder(app._root_dir):
        with open(app._qgofer_cache / "inde_list.txt", "a", encoding="utf-8") as f:
            f.write(f"{item}\n")
    return app
