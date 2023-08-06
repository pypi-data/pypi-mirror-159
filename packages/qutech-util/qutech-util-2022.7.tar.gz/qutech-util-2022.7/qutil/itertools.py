"""Import everything from itertools, more_itertools and some custom functions """
import warnings
from typing import Iterable, Any, Type, Tuple, Iterator

from itertools import *
from more_itertools import *


def separate_iterator(it: Iterable, sep: Any) -> Iterator:
    """separate_iterator('abcde', ',') --> a , b , c , d , e

    The same as :func:`~more_itertools.intersperse(sep, it, n=1)`. Only here for backwards compability.
    """
    warnings.warn(f"{__name__}.separate_iterator is just a wrapper around intersperse.",
                  DeprecationWarning,
                  stacklevel=2)
    return intersperse(sep, it, n=1)


def flatten_nested(it: Iterable, dtypes: Tuple[Type[Iterable], ...] = (list,)) -> Iterator:
    """Flattens the given arbitrarily nested iterable. By default, only lists are flattened. Use the optional `dtypes`
    argument to flatten other iterables as well.

    Similar to :func:`~more_itertools.collapse` which works with a blacklist instead of a whitelist.

    Parameters
    ----------
    it: :class:`~typing.Iterable` to flatten
    dtypes: Types that get flattened.

    Returns
    -------
    Objects that are not of a type in `dtypes`
    """
    if isinstance(it, dtypes):
        for x in it:
            yield from flatten_nested(x, dtypes)
    else:
        yield it


del Iterable, Any, Type, Tuple, Iterator
del warnings
