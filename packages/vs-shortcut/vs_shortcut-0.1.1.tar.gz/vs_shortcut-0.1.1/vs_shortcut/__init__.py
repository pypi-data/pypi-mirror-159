"""
    vs_shortcut - Microsoft Visual Studio shortcut for Anaconda-navigator
    =====================================================================

    Provides an application shortcut for Microsoft Visual Studio in
    Anaconda-navigator to prevent environment bugs. The shortcut includes an
    icon and a description just like spyder IDE or VSCode.

"""

__author__ = "Maxime Tousignant-Tremblay"
__copyright__ = "Copyright © 2022 Maxime Tousignant-Tremblay"
__license__ = "AGPL-3.0"
__status__ = "Prototype"

# Standard library
from importlib.metadata import PackageNotFoundError  # pragma: no cover

# Local import
from ._version import get_versions  # pragma: no cover


try:
    vinfo: dict[str, str] = get_versions()
    __version__ = vinfo["version"]
except PackageNotFoundError:  # pragma: no cover
    __version__ = "unknown"
finally:
    del vinfo, get_versions, PackageNotFoundError
