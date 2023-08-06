import copy
from datetime import datetime, timedelta
from functools import wraps
from typing import List, Optional, Callable

from .cachable import Cachable


class UnSupportedDataTypeException(Exception):
    pass


class Cache:
    _cache: List[Cachable] = []

    def __init__(self, hours: float = None, minutes: float = None, seconds: float = None):
        self._time = 0

        if hours is not None:
            self._time += hours * 60 * 60

        if minutes is not None:
            self._time += minutes * 60

        if seconds is not None:
            self._time += seconds

    def __call__(self, *param_arg, **param_kwargs):
        @wraps(param_arg[0])
        def wrapper(ctx, *args, **kwargs):
            key = self._get_key(ctx, param_arg[0], *args, **kwargs)
            result = self._get_data(key)

            if result is None:
                result = param_arg[0](ctx, *args, **kwargs)

                self._add(key, result)

            return result

        return wrapper

    @staticmethod
    def _get_key(ctx: object, func: Callable, *args, **kwargs) -> str:
        key_args = [str(arg) for arg in args]
        key_kwargs = []

        for key, value in kwargs.items():
            key_kwargs.append(f"{key}={value}")

        return f"{id(ctx)}/{func.__name__}/{'/'.join(key_args)}/{'/'.join(key_kwargs)}"

    def _add(self, key: str, data: object) -> None:
        self._cache.append(
                Cachable(
                        datetime.now() + timedelta(seconds=self._time),
                        key,
                        copy.deepcopy(data)
                )
        )

    def _get(self, key: str) -> Optional[Cachable]:
        for cachable in self._cache:
            if cachable.key == key:
                return cachable

        return None

    def _clean_cache(self) -> None:
        for cachable in self._cache.copy():
            if cachable.is_expired:
                self._cache.remove(cachable)

    def _get_data(self, key: str) -> Optional[object]:
        self._clean_cache()
        cachable = self._get(key)

        if cachable is None:
            return None

        return cachable.data
