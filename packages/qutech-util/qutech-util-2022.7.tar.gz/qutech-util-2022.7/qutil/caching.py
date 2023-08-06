"""Programming tools"""
import shelve
from typing import Callable, Mapping, AbstractSet, Any
import inspect
import tempfile
import os.path
import itertools
import functools
import pathlib
import dbm

import numpy as np

from qutil.itertools import separate_iterator

__all__ = ["file_cache", "lru_cache"]


def to_str_key(obj: Any) -> str:
    """Convert to a string representation that is unique except for
    - lists and ndarrays are treated the same

    :param obj:
    :return:
    """
    if isinstance(obj, tuple):
        return f'({",".join(map(to_str_key, obj))})'
    if isinstance(obj, np.ndarray):
        return to_str_key(obj.tolist())
    elif isinstance(obj, list):
        return f'[{",".join(map(to_str_key, obj))}]'
    elif isinstance(obj, Mapping):
        return '{%s}' % ",".join(f"{to_str_key(key)}: {to_str_key(value)}" for key, value in obj.items())
    elif isinstance(obj, (set, frozenset)):
        return f'{{{",".join(sorted(map(to_str_key, obj)))}}}'
    elif isinstance(obj, (int, float, complex, str, bytes, pathlib.Path)) or obj is None:
        return repr(obj)
    else:
        try:
            if eval(repr(obj)) == obj:
                return repr(obj)
        except RuntimeError:
            pass
        raise TypeError('not handled: ', type(obj))


class CachingWrapper:
    """This object wraps a callable and caches the results in a dbm database on the file system (by default in the temp
    folder). The key is generated via to_key which means that large arguments need a large time to process."""

    DEFAULT_ROOT = os.path.join(tempfile.gettempdir(), 'qutil_cache')

    def __init__(self, func, storage_path=None):
        self._func = func

        if storage_path is None:
            storage_path = os.path.join(self.DEFAULT_ROOT, self.get_full_function_name(func))

        self.storage_path = storage_path

    def __call__(self, *args, **kwargs):
        key = to_str_key((args, kwargs))
        
        folder = pathlib.Path(self.storage_path).parent
        if not folder.exists():
            folder.mkdir()

        with shelve.open(self.storage_path) as db:
            if key in db:
                result = db[key]
            else:
                result = self._func(*args, **kwargs)
                db[key] = result
        return result

    def clear(self):
        with shelve.open(self.storage_path) as db:
            db.clear()

    @classmethod
    def get_full_function_name(cls, func) -> str:
        return f"{inspect.getmodule(func).__name__}.{func.__name__}"

    @classmethod
    def clear_all_default_caches(cls):
        """Clear all caches that are in the default cache directory"""
        root = pathlib.Path(cls.DEFAULT_ROOT)
        if root.exists():
            for bak in root.glob('*.bak'):
                base_name = bak.with_suffix('')

                try:
                    shelve.open(str(base_name), 'r')
                except dbm.error:
                    print('Cannot open', bak.stem, 'and will not delete.')
                else:
                    bak.unlink()
                    base_name.with_suffix('.dir').unlink()
                    base_name.with_suffix('.dat').unlink()


def file_cache(func: Callable) -> Callable:
    return CachingWrapper(func)


lru_cache = functools.lru_cache
