"""
This module contains UI utility functions

Functions
---------
:func:`progressbar` :
    A progress bar for loops

Classes
-------
:class:`GateLayout` :
    Plots a DXF design file of a gate layout and colors the
    gates according to given voltages.

"""

import sys
from typing import Iterable

try:
    import ipynbname
    _NOTEBOOK_NAME = ipynbname.name()
except (ImportError, IndexError, FileNotFoundError):
    _NOTEBOOK_NAME = ''

try:
    if _NOTEBOOK_NAME:
        from tqdm import tqdm_notebook as tqdm
    else:
        # Either not running notebook or not able to determine
        from tqdm import tqdm
except ImportError:
    tqdm = None

__all__ = ['progressbar']


def _simple_progressbar(iterable: Iterable, prefix: str = "Computing: ",
                        size: int = 25, file=sys.stdout):
    """https://stackoverflow.com/a/34482761"""
    count = len(iterable)

    def show(j):
        x = int(size*j/count)
        file.write("\r{}[{}{}] {} %".format(prefix, "#"*x, "."*(size - x),
                   int(100*j/count)))
        file.flush()

    show(0)
    for i, item in enumerate(iterable):
        yield item
        show(i + 1)

    file.write("\n")
    file.flush()


def progressbar(iterable: Iterable, *args, **kwargs):
    """
    Progress bar for loops. Uses tqdm if available or a quick-and-dirty
    implementation from stackoverflow.

    Usage::

        for i in progressbar(range(10)):
            do_something()
    """
    if tqdm is not None:
        return tqdm(iterable, *args, **kwargs)
    else:
        return _simple_progressbar(iterable, *args, **kwargs)
