import base64
import uuid
from pathlib import Path
from typing import Optional


def generate_uuid():
    """Generates a uuid 4 string, in this context for tracking each run of the experiment
    Returns:
        an ascii friendly uuid4 string.
    """
    return base64.urlsafe_b64encode(uuid.uuid4().bytes).rstrip(b"=").decode("ascii")


def init_path(path: Optional[Path] = None) -> Path:
    """Convert the string to a path object."""
    if path is None:
        return Path.home()
    return Path(path).expanduser().resolve()


def get_log_path(path: Optional[Path] = None) -> Path:
    """Returns the log path."""
    if path is None:
        path = init_path(path) / '.qgofer' / 'logs'
        path.mkdir(parents=True, exist_ok=True)
    return Path(path).expanduser().resolve()
