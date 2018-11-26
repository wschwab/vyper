import sys as _sys
import pkg_resources as _pkg_resources


if (_sys.version_info.major, _sys.version_info.minor) < (3, 6):
    # Can't be tested, as our test harness is using python3.6.
    raise Exception("Requires python3.6+")  # pragma: no cover


try:
    __version__ = _pkg_resources.get_distribution('vyper').version
except _pkg_resources.DistributionNotFound:
    __version__ = '0.0.0development'

from vyper.compiler import compile  # noqa
