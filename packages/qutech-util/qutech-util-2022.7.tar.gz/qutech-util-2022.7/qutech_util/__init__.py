"""This is the new name of the qutil module which is just an alias to qutil for backwards compatibility reasons."""
import sys
import qutil

from qutil import *

__all__ = qutil.__all__
__version__ = qutil.__version__
sys.modules[__name__] = qutil

del qutil
del sys
