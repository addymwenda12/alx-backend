#!/usr/bin/env python3

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class. Inherits from BaseCaching. Has no limit.

    Methods:
        put(key, item): Add an item in the cache.
        get(key): Get an item by key.
    """
    def put(self, key, item):
        """
        Add an item in the cache

        Args:
            key: The key of the item.
            item: The item to be added.

        Returns:
            None
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key

        Args:
            key: The key of the item.

        Returns:
            The item associated with the key, or None if the key is not found.
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
