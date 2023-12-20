#!/usr/bin/env python3

import redis
from uuid import uuid4
from typing import Union, Callable, Optional

"""cache class initializtion"""


class Cache:
    """class cache that creates methods for class"""
    def __init__(self) -> None:
        """Initialize cache class"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """set new value on key and store them in redis db"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """get value associated with the key from redis db"""
        value = self._redis.get(key)
        if fn:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """parametrize Cache.get method according to type passed"""
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: str) -> int:
        """parametrize Cache.get method according to type passed"""
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
