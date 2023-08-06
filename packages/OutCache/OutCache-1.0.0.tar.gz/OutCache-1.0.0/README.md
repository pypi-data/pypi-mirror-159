[![PyPI version](https://badge.fury.io/py/OutCache.svg)](https://pypi.org/project/OutCache)
# OutCache
Function output cacher

### Regular usage:

```python
from outcache import Cache


@Cache(minutes=1)
def get_profile(email: str, username: str):
    my_dict = {"email": email, "username": username}

    return my_dict

profile = get_profile("example@example.com", username="example")
```

### Async usage
```python
from outcache import CacheAsync

@CacheAsync(minutes=1)
async def get_profile(email: str, username: str):
    my_dict = {"email": email, "username": username}

    return my_dict

profile = await get_profile("example@example.com", username="example")
```