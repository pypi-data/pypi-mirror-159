"""
define exception classes for chopin

"""

__all__ = (
    "ChopineException",
    "DownloadFails",
    "FileRemoveFails",
)

class ChopinException(Exception):
    """Base exception class for chopin

    Ideally speaking, this could be caught to handle any exceptions raised from this library.

    """
    pass

class DownloadFails(ChopinException):
    """Called when download was unsuccessful."""
    pass

class FileRemoveFails(ChopinException):
    """Called when file removing was unsuccessful."""
    pass

class InvalidHashValue(ChopinException):
    """Called when hash value is invalid."""
    pass
