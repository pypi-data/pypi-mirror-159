from functools import wraps

from .cache import Cache


class UnSupportedDataTypeException(Exception):
    pass


class CacheAsync(Cache):
    def __call__(self, *param_arg, **param_kwargs):
        @wraps(param_arg[0])
        async def wrapper(ctx, *args, **kwargs):
            key = self._get_key(ctx, param_arg[0], *args, **kwargs)
            result = self.__get_data(key)

            if result is None:
                result = await param_arg[0](ctx, *args, **kwargs)

                self.__add(key, result)

            return result

        return wrapper
