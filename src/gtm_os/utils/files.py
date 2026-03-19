"""Safe file operations that reject symlinks.

This module provides symlink-safe versions of common file operations
to prevent symlink attacks (TOCTOU vulnerabilities).
"""

import contextlib
import logging
import os
import tempfile
from pathlib import Path

from gtm_os.exceptions import SymlinkError

logger = logging.getLogger(__name__)

__all__ = [
    "SymlinkError",
    "safe_exists",
    "safe_mkdir",
    "safe_read_text",
    "safe_rmdir",
    "safe_unlink",
    "safe_write_text",
]


def safe_write_text(path: Path, content: str) -> None:
    """Write text to a file atomically, rejecting symlinks."""
    if path.is_symlink():
        logger.warning("Attempted write to symlink: %s", path)
        raise SymlinkError(f"Refusing to write to symlink: {path}")
    fd = None
    tmp_path = None
    try:
        fd, tmp_path = tempfile.mkstemp(dir=path.parent, suffix=".tmp")
        os.write(fd, content.encode())
        os.close(fd)
        fd = None
        os.replace(tmp_path, path)
        tmp_path = None
    finally:
        if fd is not None:
            os.close(fd)
        if tmp_path is not None:
            with contextlib.suppress(OSError):
                os.unlink(tmp_path)


def safe_read_text(path: Path) -> str:
    """Read text from a file, rejecting symlinks."""
    if path.is_symlink():
        logger.warning("Attempted read from symlink: %s", path)
        raise SymlinkError(f"Refusing to read from symlink: {path}")
    return path.read_text()


def safe_exists(path: Path) -> bool:
    """Check if path exists and is not a symlink."""
    if path.is_symlink():
        return False
    return path.exists()


def safe_unlink(path: Path) -> None:
    """Delete a file, rejecting symlinks."""
    if path.is_symlink():
        logger.warning("Attempted unlink of symlink: %s", path)
        raise SymlinkError(f"Refusing to delete symlink: {path}")
    path.unlink()


def safe_rmdir(path: Path) -> None:
    """Remove an empty directory, rejecting symlinks."""
    if path.is_symlink():
        logger.warning("Attempted rmdir of symlink: %s", path)
        raise SymlinkError(f"Refusing to remove symlink directory: {path}")
    path.rmdir()


def safe_mkdir(path: Path, parents: bool = False, exist_ok: bool = False) -> None:
    """Create a directory, rejecting symlinks."""
    if path.is_symlink():
        logger.warning("Attempted mkdir on symlink: %s", path)
        raise SymlinkError(f"Refusing to create directory at symlink: {path}")
    path.mkdir(parents=parents, exist_ok=exist_ok)
