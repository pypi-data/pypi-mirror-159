"""
Chopin Compositions
~~~~~~~~~~~~~~~~~~~

:copyright: (c) 2021-present ster
:license: Mit, see LICENSE for more details.

"""

__title__ = "chopin"
__author__ = "ster"
__license__ = "MIT"
__copyright__ = "Copyright 2021-present ster"
__version__ = "0.2.0"

from .chopin import Chopin
from .compositions import Composition
from .contents import Content

__all__ = (
    "Chopin",
    "Composition",
    "Content",
)
