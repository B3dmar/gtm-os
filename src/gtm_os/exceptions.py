"""GTM:OS exception hierarchy."""


class GtmOsError(Exception):
    """Base exception for all GTM:OS errors."""


class SymlinkError(GtmOsError):
    """Raised when a symlink is detected where it shouldn't be."""


class PathTraversalError(GtmOsError):
    """Raised when path traversal is detected in a slug or filename."""
